from textwrap import wrap
from util import animalsay, INDENT_DEFAULT, MAXWIDTH_DEFAULT
import animals 

def cowsay(message, maxwidth=MAXWIDTH_DEFAULT, indent=INDENT_DEFAULT):
    return animalsay(wrap(message, maxwidth), animal=COW, indent=indent)

def pigsay(message, maxwidth=MAXWIDTH_DEFAULT, indent=INDENT_DEFAULT):
    return animalsay(wrap(message, maxwidth), animal=PIG, indent=indent)

def chickensay(message, maxwidth=MAXWIDTH_DEFAULT, indent=INDENT_DEFAULT):
    return animalsay(wrap(message, maxwidth), animal=CHICKEN, indent=indent)

def sheepsay(message, maxwidth=MAXWIDTH_DEFAULT, indent=INDENT_DEFAULT):
    return animalsay(wrap(message, maxwidth), animal=SHEEP, indent=indent)

def penguinsay(message, maxwidth=MAXWIDTH_DEFAULT, indent=INDENT_DEFAULT):
    return animalsay(wrap(message, maxwidth), animal=PENGUIN, indent=indent)

def dogsay(message, maxwidth=MAXWIDTH_DEFAULT, indent=INDENT_DEFAULT):
    return animalsay(wrap(message, maxwidth), animal=DOG, indent=indent)


