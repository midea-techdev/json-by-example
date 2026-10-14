elif isinstance(obj, timezone):
            offset_hours = obj.utcoffset(None).total_seconds() / 3600
            return {
                "__class__": "timezone",
                "offset": int(offset_hours)