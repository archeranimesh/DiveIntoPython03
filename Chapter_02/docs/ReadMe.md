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

## Lists ##

* Python Lists are arrays on steroids.
* We can create a list like this
    * `a_list = [1, 2, 3, 4]`
* A list can be indexed like this
    * `a_list[0]` returns `1`
* A negative index access item from the end.
    * you can do `len(a_list) - index` to get the positive index.
* Slicing a List
    * We can slice a list, like this, creates a new list, not changing old values.
        * `a_list[1:3]`
    * In the slice if the starts from beginning and end at the last, we can leave that value.
    * When both slice value are left out, we get a copy of original list
* List Extensions
    * We can concate 2 list using a `+` operator.
    * A list is a hetrogeneous array.
    * `append()`, adds a single element to the end of the list.
        * when a list is passed, the complete list is appened as 1 item.
    * `extend()`, modifies the original list with a new item added.
        * when a list is extended, it adds individual items to the existing list.
* Searching
    * `count()`: returns the number of occurences of a item.
    * `in` : tells us `True` or `False`, depending on if the item is in the list or not.
    * `index()` : tells us the index of first occurerence of the item.
        * It throw a `ValueError` if a item is not present
* Removing
    * `del a_list[1]` : deletes the value at index 1
    * `remove()`: removes a particular item from the list.
        * it returns a `ValueError` is the item is not present
    * `pop()`: removes the last items and also returns that item
    * `pop(1)` : removes the item at the index.
    * `pop()` on an empty list gives `IndexError`
* Boolean Context
    * Empty list returns a `False`
    * Every thing else will return a `True`
    * `insert()`, inserts a new item as a defined location.
