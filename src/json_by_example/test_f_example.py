import json
from datetime import datetime
from f_example import ComplexEncoder, SignalDecoder

simple_json_data = """{
    "my_datetime": {"__class": "datetime", "y": 2026, "month": 10, "d": 5, "h": 12, "minute": 0, "s": 0},
    "my_complex": {"__class": "complex", "real": 3.0, "imag": 4.0},
    "samples": [
        {"__class": "complex", "real": -2.0, "imag": 5.0},
        {"__class": "complex", "real": 2.0, "imag": 5.0}
    ]
}"""

def run_my_test():
    decoder = SignalDecoder()
    parsed_objects = decoder.decode(simple_json_data)
    
    assert isinstance(parsed_objects["my_datetime"], datetime)
    assert isinstance(parsed_objects["my_complex"], complex)
    assert parsed_objects["my_datetime"].year == 2026
    assert parsed_objects["my_complex"] == complex(3.0, 4.0)

    assert isinstance(parsed_objects["samples"], list)
    assert len(parsed_objects["samples"]) == 2
    assert parsed_objects["samples"][0] == complex(-2.0, 5.0)
    assert parsed_objects["samples"][1] == complex(2.0, 5.0)

    json_string_output = json.dumps(parsed_objects, cls=ComplexEncoder, indent=4)

    assert '"__class": "datetime"' in json_string_output
    assert '"__class": "complex"' in json_string_output

    print("SUCCESS: All assertions passed!")

if __name__ == "__main__":
    run_my_test()
