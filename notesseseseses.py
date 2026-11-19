#hunter card notessessseseses

def hello(*args):
    for name in args:
        print(f"Hello {name}!")

def clean(type, data):
    if type == "str":
        return data.strip()