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
    * `insert()`, inserts a new item as a defined location.
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


## Tuple ##

* A tuple is a Immutable list.
* A tuple is defined in this manner.
    * `a_tuple = (1, 2, 3)`
* Tuple have the items in a defined order and can be accessed with array indexing
    * `a_tuple[0]`
* Negative index, slicing, searching works the same way as list.
* There is no `append()`, `extend()`, `insert()`, `pop()` and `remove()` attributes in tuple.
* A list can be converted to a tuple by calling `tuple()`, and passed to a function to prevent any modification.
* Boolean context also behaves the same manner.
* Few important things to note are
    * Tuple are faster than List
    * Using Tuple makes the code safer, as it provides a write protection
    * Tuples can also be used as Dictionary key values because of its immutable nature.
* Tuple with one item is created like this
    * `a_tuple = (2, )` the comma is added.
* Tuples can be used to assign multiple values
    * `(x, y, z) = ("Hello", "World", "!")`
    * `range()` can be used to intilize multiple values in one place.


## Sets ##

* Sets in Python is an unordered bag of unique values.
* A set can contain any immutable datatype.
* All standard set operation are possible on 2 sets.
    * Union
    * Intersection
    * Set Difference.
* A Set can be constructed like this
    * `a_set = {1}`
    * `a_set = {}` creates a dict and not a set, one item is necessary for a set.
    * `a_set = set()` creates a empty set.
* A set can be created from a list.
    * `a_set = set([1, 2, 3])` it will remove any dupilcate values.
* Modifying a set
    * `add()` : add's a elememt to the set, since set is not ordered we do not have a `append()` method.
    * It will still not add any duplicate values.
    * `update()`: update takes one argument a set, and adds all elements to original set
        * `update()` can be called with any number of argument, causing individual elements to be added to original set.
        * `Update()` can even take a list.
* Removing item from set
    * `discard()` removes an item passed as an argument from the set.
        * if the element is not present it does not throw an error.
    * `remove()` : removes an item from the set, but throws an error `KeyError` is the element is not present.
    * `pop()` ; removes arbitary element from the set, as it is not ordered,
        * `pop()` on an empty set gives `KeyError`
    * `clear()` removes all item from the set.
* Set Operation
    * `in` : returns `True` is the element is present.
    * `union()` returns a set containing all elements from both set
    * `intersection() ` returns a set containing element present in both sets.
    * `symmetric_difference()` returns a set containing all element present excatly one of the sets.
        * All the above 3 operations are symmetric operation.
    * `difference()` returns a set containing present in one set not present in another.
* Search
    * `issubset()` : returns `True` is one set is a subset of others.
    * `issuperset()` : returns `True` if one is super set of other.
* Boolean Context
    * Empty set returns `False`
    * Every thing else is `True`

## Dictionary ##

* Dictionary is an unordered set of key-value pairs.
* Dictionary are optimized for retreving values from a key.
* Dictionary can be created in this manner.
    * `a_dict = {}` empty Dictionary
    * `a_dict = {'server': 'myServer'}` Dictionary with a key value pair.
* Reteriving values
    * `a_dict['server']`returns `myServer`
    * Accessing a Dictionary by value causes a `KeyError`
* Modifying 
    * `a_dict[`server`] = "newserver"` : creates a new value for the key.
    * Keys are case sensitive.
    * Duplicate keys are not possible.
* Dictionary can have mixed values of int and string.
* Boolean Context
    * Empty Dictionary is `False`
    * Every thing else is `True.`

## None ##
* `None` is a special constant in Python. It is not `0`, it also not `False`
* Comparing `None` to anything other than `None` results in `False`

