## What Can Pandas Do?
    Pandas gives us answers about the data. Like:
        Is there a correlation between two or more columns?
        What is average value?
        Max value?
        Min value?
    Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data.

## Data cleaning
    Data cleaning means fixing bad data in your data set.

    Bad data could be:
        Empty cells
        Data in wrong format
        Wrong data
        Duplicates


## Concat, merge, join
        concat(): Merge multiple Series or DataFrame objects along a shared index or column
        DataFrame.join(): Merge multiple DataFrame objects along the columns
        DataFrame.combine_first(): Update missing values with non-missing values in the same location
        merge(): Combine two Series or DataFrame objects with SQL-style joining
        merge_ordered(): Combine two Series or DataFrame objects along an ordered axis
        merge_asof(): Combine two Series or DataFrame objects by near instead of exact matching keys
        Series.compare() and DataFrame.compare(): Show differences in values between two Series or DataFrame objects

        merge() implements common SQL style joining operations.
            one-to-one: joining two DataFrame objects on their indexes which must contain unique values.
            many-to-one: joining a unique index to one or more columns in a different DataFrame.
            many-to-many : joining columns on columns.

## Differance between .loc and .iloc
    The .loc[] method is a label based method that means it takes names or labels of the index when taking the slices, whereas .iloc[] method is based on the index's position.
    