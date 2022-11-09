# Pyfarmsay

Expanding on the exiting package, [pycowsay](https://pypi.org/project/pycowsay/), pyfarmsay does not only feature a talking 
cow, but an entire talking farm! Our beautiful farm features a talking cow, pig, chicken, dog, penguin, and sheep. 

## Install 
To install our package on your local machine, run the following command

```
pip install pyfarmsay 
```

To install into a virtual environment, make sure you install pipenv by running the following:
```
pip install pipenv
```
and then using the following command to install our package into an isolated virtual environment. 
```
pipenv install pyfarmsay 
```

This will create a virtual environment, which you can access by running ```pipenv shell```

## Run 
Once pyfarmsay is installed on your machine, you can use it from the command line or from within a python file. 
### From the Command Line
To run the package from the command line, all you have to do is invoke the package name, followed by the animal of your choice and your desired message:
```
pyfarmsay [ANIMAL] [MESSAGE]
```
for example, 

```
pyfarmsay cow i say moo
```
will output

```
 -----------
< i say moo >
 -----------
    \
     \
      ^__^
      (oo)\_______
      (__)\       )\/\
          ||----w |
          ||     ||

```

### Import into a python module
Use the following import statement at the very top of your .py file to use the functions from within your module. 
```
from pyfarmsay import pyfarmsay
```
or 

```
from pyfarmsay.pyfamrsay import [function name]
```

## Link to PyPI package
