from S1E9 import Stark, Character

Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)

try:
    hodor = Character("hodor")
    print(hodor)
except Exception as e:
    print(f"from {__name__} \033[31m{type(e).__name__}\033[0m: {e} ")
