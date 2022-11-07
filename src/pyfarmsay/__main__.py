import sys
from . import pyfarmsay


def main():
    animal = sys.argv[1].lower()
    message = " ".join(sys.argv[2:])

    if animal == "cow":
       return pyfarmsay.cowsay(message)
    elif animal == "pig":
        return pyfarmsay.pigsay(message)
    elif animal == "chicken":
        return pyfarmsay.chickensay(message)
    elif animal == "dog":
        return pyfarmsay.dogsay(message)
    elif animal == "penguin":
        return pyfarmsay.penguinsay(message)
    elif animal == "sheep":
        return pyfarmsay.sheepsay(message)
    else:
        return "animal not in farm :(!"

    

if __name__ == "__main__":
    print(main())


