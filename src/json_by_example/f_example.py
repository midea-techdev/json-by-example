'''
In case we have encoded the complex number into JSON Object as list, it will not be possible
 to decoded or convert to pyth complex datatype
 In this example we want to encode and decode complex and datetime
JSON Object below:

 {
    "signal": {
        "place": "Uppsala",
        "stamp": {
            "__class": "datetime",
            "y": 2025,
            "month": 4,
            "d": 19,
            "h": 16,
            "minute": 23,
            "s": 51
        },
        "samples:": [
            {
                "__class": "complex",
                "real": -2.0,
                "imag": 5.0
            },
            {
                "__class": "complex",
                "real": 3.0,
                "imag": 1.0
            },
            {
                "__class": "complex",
                "real": 2.0,
                "imag": 5.0
            }
        ]
    }
}
 

You can see the samples is a list of complex numbers and we have stamps
Use the examples in the previous files (module)  to Decode and Encode the above JSON file
You can see the Python object structure below.
Try to debug your result so you can inspect and see how dictionary is format from the JSON object String 
'''
class Signal():
    def __init__(self, _place:str, _stamp:datetime, _samples:list[complex]):
        self._place = _place
        self. _stamp = _stamp
        self._samples= _samples

    @property
    def place(self):
        return self._place

    @property
    def stamp(self):
        return self._stamp

    @property
    def samples(self):
        return self._samples



import json
from datetime import datetime

data =  """{
    "signal": {
        "place": "Uppsala",
        "stamp": {
            "__class": "datetime",
            "y": 2025,
            "month": 4,
            "d": 19,
            "h": 16,
            "minute": 23,
            "s": 51
        },
        "samples": [
            {
                "__class": "complex",
                "real": -2.0,
                "imag": 5.0
            },
            {
                "__class": "complex",
                "real": 3.0,
                "imag": 1.0
            },
            {
                "__class__": "complex",
                "real": 2.0,
                "imag": 5.0
            }
        ]
    }
}"""

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return  { 
                     "__class":"complex",
                     "real": obj.real,
                     "imag": obj.imag
                    }
    
        elif isinstance(obj, datetime):
             return {
                       "__class": "datetime",
                       "y": obj.year,
                       "month": obj.month,
                       "d":obj.day,
                       "h": obj.hour,
                       "minute": obj.minute,
                       "s": obj.second
                      }
          
        else: 
            return super().default(obj)
class SignalDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=SignalDecoder.from_dict)  
    @staticmethod
    def from_dict(d):
        if d.get("__class") == "complex":
            return complex(d.get("real"), d.get("imag"))
        elif d.get("__class") == "datetime":
            return datetime(d["y"],d["month"],d["d"],d["h"],d["minute"],d["s"])  
        return d # defaulting if not complex                
                   
if __name__ == '__main__':
    x = json.loads(data, cls= SignalDecoder) # decoding the JSON string into Python object and returning a dictionary
    print(x) 
    y = json.dumps(x, cls=ComplexEncoder, indent=4) # encoding the Python object into JSON string and returning a string
    print(type(y))
    print(y) 
                  
