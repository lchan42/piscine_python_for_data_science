def all_thing_is_obj(object: any) -> int:
    if object:
        obj_type = type(object)
        obj_name = (obj_type.__name__).capitalize()
        if obj_name == "Str":
            obj_name = object + " is in the kitchen"
        if obj_name == "Int":
            print("Type not found")
        else:
            print(f"{obj_name} : {obj_type}")
    return 42
