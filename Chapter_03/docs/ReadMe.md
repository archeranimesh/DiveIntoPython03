# Chapter 03 | Comprehensions #
## Dive Into Python 03 | Mark Pilgrim ##

Comprehensions are the real power of Python, and a lot of thought of concept in it. It may look complicated to begin with, but once have a hang of it, It becomes a swiss army knife useful for many scenerio.
In Python we have these Comprehensions.
* List Comprehensions
* Dict Comprehensions
* Set Comprehensions

We also will look through some important module in Python.
* `os` module.
* `glob` module.

## Files and Directory. ##
* Python comes with a `os` module which stands for Operating System.
    * This modules have functions to help with manipulate local directory, file, process and environment variables.
    * This modules does it best to give abstraction from the Operating system on which it is run.
* Few important function in this module.
    * `.getcwd()` : Provides the path from where the code is executed.
    * `.chdir()` : We can change the directory to the path mentioned in the arguments.
        * `chdir()` takes path as an arguments, where it does not matter which `\` or `\` is used to denote the path
    * `.path.join()` : takes n arguments and joining them to form a path.
    * `.path.expanduser('~')` : will expand to point to the user home directory.
    * `.path.split()` : splits the path passed as an arguments to directory and the filename. It returns a tuple.
    * `.path.splitext()` : splits the file name passed as an arguments to base name and extension.
    * `.path.realpath('filename')` : returns the complete path of the file.
    * `.stat('filename')` : provides metadata for a particular file
* We also have `glob` module to get content of the directory.
    * Wildcards are also supported in this.
    * `glob.glob('*.py')` returns a list of file with `.py` extension.

## List Comprehensions  ##
* List Comprehensions maps one list into another list by applying a function to each element.
    * `[elem * 2  for elem in a_list ]`
        * The above code may look complex, but we can drill it down in steps.
        * `[]` the surrounding brackets tells that this is a list.
        * In all Comprehensions start reading code from the `for` loop.
            * In above code, we are iterating over `a_list` and assigning each element to `elem`
            * finally multiplying each `elem` with `2` and storing into the list.
* List Comprehensions can also filter elements, so that we store only partial list.
    * `[elem * 2 for elem in a_list if elem % 2 == 0 ]`
        * Again the above, start from the `for` loop, iterating over a list and assiging to each `elem`
        * Each `elem` is then checked with the `if` condition, which ever element passes the test,
            * `if` is always evaluated for each element.
        * Multiply the `elem` with `2` and store it.
* The above are basic building blocks we can create a very complicated list Comprehensions.


## Dictionary Comprehensions ##
* It is same as a List Comprehensions, and creates a Dictionary.
* `{f:os.stat(f) for f in glob.glob('*.py') }`
    * In the above code, the surrounding `{}` tells this is a Dictionary.
    * The Comprehensions starts from `for` loop, where we are taking each file returned by `glob.glob('*.py')`
    * Then each `f` file is used to create a key, value pair with `f` being the file name, and `:` the `os.stat(f)` as the value.
* `{f:os.stat(f) for f in glob.glob('*.py') if os.stat(f).st_size > 500}`
    * Everything is same as above, just the `if` condition is executed for each `f` given by the `for` loop and then filtered based on its size.
* For a Dictionary containing immutable values, we can use this Comprehensions to convert to a value,key dict.
    * {value:key for key, value in a_dict.items()}

## Set Comprehensions ##
* Set Comprehensions is same as a Dictionary Comprehensions, with the only difference being it stores only values.
* `{x ** 2 for x in a_set }`
    * Iterate through a set and store each elements to the power of `2`.
* `{x **2 for x in a_set if x % 2 == 0 }`
    * Iterate through each element of the set, filter it if `x` is divisible by `2` and then store the square of the number.
* Set Comprehensions also works on list and converts it to a set.
