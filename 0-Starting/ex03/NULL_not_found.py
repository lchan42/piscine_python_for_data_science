import math


def NULL_not_found(object: any) -> int:

    obj_type = type(object)
    obj_name = type(object).__name__
    known_types = {
        "NoneType":	("Nothing", None),
        "float":	("Cheese", float("NaN")),
        "int":		("Zero", 0),
        "str":		("Empty", ''),
        "bool":		("Fake", False),
    }

    if obj_name in known_types and (
        object == known_types[obj_name][1] or
        obj_name == "float" and math.isnan(object)
    ):
        if obj_name == "str":
            # in case moulinette is being anoying with the extra space
            print(f"{known_types[obj_name][0]}: {obj_type}")
        else:
            print(f"{known_types[obj_name][0]}: {object} {obj_type}")
        return 0
    else:
        print("Type not Found")
        return 1
