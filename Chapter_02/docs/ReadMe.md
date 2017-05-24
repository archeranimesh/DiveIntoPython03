# Chapter 02 | Native Datatypes #
## Dive Into Python 03 | Mark Pilgrim ##

Python has a few data type, we will cover some of them here:-
* Booleans
    * Provide the value `True` and `False`
* Numbers
    * Integers, floats, fractions, even commplex numbers.
* Bytes and ByteArray
* Lists
    * Ordered sequence of values.
* Tuple
    * Ordered, immutable sequence of values.
* Sets
    * Unordered values.
* Dictionaries
    * Unordered key,value pairs.

## Booleans ##
* Booleans has two values in Python
    * `True`
    * `False`
* *Boolean Context* : Any Python Expressions can evaluate to boolean value which is called *Boolean Context*
* Booleans can be treated as numbers
    * `True` has the value of `1`
    * `False` has the value of `0`

## Numbers ##
* Python supports two types of numbers
    * Integers
    * Float
* `type()` and `isinstance()` is used to check the it belong to a certain type.
* Mixed operation involving int and floats results in floating value.
* `int()` and `float()` can be used for conversion into each other type.
    * -ive numbers are trunctated with `int()` towards 0
    * Floating point numbers are accurate till 15 decimal places.
    * Integers can be very large as Python 3 does not have a long type.
* The following are the operation possible.
    * `/` : Does a floating point division
    * `//` : Does a integer division
        * Negative integer division rounds up to nearest integers.
    * `**` : Does a exponentation.
    * `%` : Provides us with the remainder.
* In a *Boolean Context* 
    * Non zero integers are all `True`
    * Non zero floating are also `True`, kindly be careful with rounding error.
### Fractions ###

Python also has a provision for Fractions under the module `fractions`
* We define a fraction like this
    * `fractions.Fraction(1, 3)`
* We can perform all mathematical operation possible on Fraction
    * `+`
    * `-`
    * `/`
    * `**`
    * `*`
* Improper frations are reduced to proper fraction.
* Python does not allow a fraction with `0` denominatior.
* In *Boolean Context* all not non zero numerators are `True`

### Trigonometry ###
* Python also supports Trigonometry operations under the `math` module.
* `sin()`, `cos()`, `tan()` all operations are supported.
* Python does not have infinite precision, `tan(Pi/4)` will give `0.99999999` and not `1.0`



