from pyfarmsay import pyfarmsay

def func():
    """
    Print the output of the functions in pyfarmsay
    """
    print(pyfarmsay.chickensay("hello"))
    print(pyfarmsay.cowsay("hi"))
    print(pyfarmsay.pigsay("nice to see you"))
    print(pyfarmsay.sheepsay("how are you?"))
    print(pyfarmsay.penguinsay("have a nice day"))
    print(pyfarmsay.dogsay("!!!"))
    ## shows how functions behave when there are no arguments
    print(pyfarmsay.farmsay())

if __name__== "__main__":
    func()