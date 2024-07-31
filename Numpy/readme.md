## Why is NumPy Faster Than Lists?
NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them faster.


## Data types in numpy

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

## The Difference Between Copy and View
    The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
    The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

## Reshape
    Reshape dimention n*m= size of element
    in n dimentional array all the element size should same
    Reshaped array is a view of the original array
    We are allowed to have one "unknown" dimension. We can pass -1 as the value, and NumPy will calculate this number. newarr = arr.reshape(2, 2, -1)
    We can use reshape(-1) to flattening the array.

## Joining NumPy Arrays
    We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.
    We can use stacking to join the arrays.
    Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
    hstack() to stack along rows
    vstack() to stack along columns
    dstack() to stack along height, which is the same as depth.

## Splitting NumPy Arrays
    We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
    We also have the method split() available but it will not adjust the elements when elements are less in source array

## NumPy Searching Arrays
    To search an array, use the where() method.
    There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order. We can use for multiple values as well.

## NumPy Filter Array
    In NumPy, you filter an array using a boolean index list.




