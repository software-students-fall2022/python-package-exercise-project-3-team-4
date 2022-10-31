from textwrap import wrap

from util import animalsay, INDENT_DEFAULT
import animals

def cowsay(message, maxwidth=100, indent=INDENT_DEFAULT):
    return animalsay(wrap(message, maxwidth), animal=animals.COW, indent=indent)

def pigsay(message, maxwidth=100, indent=INDENT_DEFAULT):
    return animalsay(wrap(message, maxwidth), animal=animals.PIG, indent=indent)

print(pigsay("hi friends"))