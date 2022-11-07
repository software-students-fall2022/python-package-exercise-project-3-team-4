import sys
import farmsay


def main():
    animal = sys.argv[1].lower()
    message = " ".join(sys.argv[2:])

    if animal == "cow":
       return farmsay.cowsay(message)
    elif animal == "pig":
        return farmsay.pigsay(message)
    elif animal == "chicken":
        return farmsay.chickensay(message)
    elif animal == "dog":
        return farmsay.dogsay(message)
    elif animal == "penguin":
        return farmsay.penguinsay(message)
    elif animal == "sheep":
        return farmsay.sheepsay(message)
    else:
        return "animal not in farm :(!"

    

if __name__ == "__main__":
    print(main())


