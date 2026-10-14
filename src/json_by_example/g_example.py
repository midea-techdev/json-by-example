import json
from datetime import date,timedelta,timezone

data = """{
    "report": {
        "created": {
            "__class": "date",
            "y": 2025,
            "month": 4,
            "d": 27
        },
        "duration": {
            "__class": "timedelta",
            "days": 2,
            "seconds": 3600,
            "microseconds": 4
        },
        "timezone": {
            "__class": "timezone",
            "offset": 2
        }
    }
}"""
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return {
                "__class": "date",
                "y": obj.year,
                "month": obj.month,
                "d": obj.day
            }
        elif isinstance(obj, timedelta):
            return {
                "__class": "timedelta",
                "days": obj.days,
                "seconds": obj.seconds,
                "microseconds": obj.microseconds
            }
        elif isinstance(obj, timezone):
            offset_hours = obj.utcoffset(None).total_seconds() / 3600
            return {
                "__class": "timezone",
                "offset": int(offset_hours)
            }
        return super().default(obj)
def custom_decoder(dct):
    if "__class" in dct:
        cls_name = dct["__class"]
        if cls_name == "date":
            return date(dct["y"], dct["month"], dct["d"])
        elif cls_name == "timedelta":
            return timedelta(days=dct["days"], seconds=dct["seconds"], microseconds=dct["microseconds"])
        elif cls_name == "timezone":
            return timezone(timedelta(hours=dct["offset"]))
    return dct
if __name__ == '__main__':
    x =json.loads(data, object_hook=custom_decoder) # decoding the JSON string into Python object and returning a dictionary
    print(x) 
    print(type(x)) # <class 'dict'>
    y = json.dumps(x, cls=CustomEncoder, indent=4) # encoding the Python object into JSON string and returning a string
   
    print(y) 
    print(type(y))