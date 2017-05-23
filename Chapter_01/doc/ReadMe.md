# Chapter 01 | Your First Python Program #
## Dive Into Python 03 | Mark Pilgrim ##

## Declaring Function ##

* A function can be declared anywhere in the code with the use of `def` keyword.
    * `def approximate_size(size, a_kilobyte_is_1024_bytes=True):`
* A Python function has following charateristics.
    * It does not define any return data type.
    * Every Python function returns some value, if it does not return anything explicitly, it return `None`
* A Python function's does not specify any type for its arguments.
* Python functions can have default values, if the function is called without this arguments, then this is the default value passed.
* A Python function can be called with **Named Arguments**, once you call with a named arguments, all argument to the right should also be named.


## Comments ##

* Documentation is at the heart of Python. 
* Every Python Function will have a *docstring* for documententing a function.
* *docstring* is created with `''' '''`, triple quotes.
* Triple quotes specify a multi line strings, with whitespaces preserved.
* *docstring* is it exists for function should be the first line of code after function defination.

## Import ##

* `import` helps in bringing all the functions and attributes of the module available for use.
    * `import sys`: will enable to use all the `sys` modules fuction and attributes.
* All Python modules are not stored in `.py` files, some built-in modules are directly written in `C` language and is available for use.
* We can add any new directory in the search path for importing module by this code.
    * `sys.path.insert(0,'/path')`


## Object ##

* In Python, everything is a object, even built in data type like `int`, `str`, `float`, `function`, `class`, `object`.
* The defination of objects in Python is very losse, it does not mandate for a objects to
    * Have attributes and methods.
    * Each class to be subclassable.
* Every object in Python can be assigned to a variable or passed as an arguments.
* functions, Modules, Classes, and individual instance of Classes are all first class objects.

## Indentation ##

* Python does not have a explicit begin and end marker for a block of code. like `{}` in some languages.
* A block of code is identified with `:` and indentation.
* Python uses carriage return for statement seperation and indentation to seperate code blocks.

## Exceptions ##

* Exceptions is an indication of some thing went wrong in the code.
* Not all Exceptions are errors, some are use to define the floe of code.
* When an error occurs which is not handled in the code, it prints how the error happened and some extra information to help in debugging.
* Exceptions bubling to the Python Shell means no one in the code handled this exception.
* A Exceptions, can be raised using the `raise` keywords.
* An Exceptions if not handled in one function is bubbled to the calling function and finally going through the complete stack bubbles to the shell.
* An Exceptions is nice way to define the flow of code, if an API is defined in two modules we can check for `ImportError` and then decided which module to use.


## Variables ##
* In Python, a variable can be defined at any place without a declaration.
* Python does not allow to reference a undeclared variable.


## Case Sensitive ##

* Python is Case sensitive.

## Running Scripts ##

* Python has a special way to invoke main.
    * `if __name__ == '__main__':`
* Every module is a object in Python, and they have a built-in attribute called `__name__`, the value of this attribute depends on how the module is used.
    * If we import this module, the attribute `__name__` will have have value as the module name.
    * If the module is run directly as a script, the attribute `__name__` will have a value of `__main__`.
* With this above divergence in the value of `__name__` attribute we can use to call a `main()` method when we execute as a standalone scripts.
