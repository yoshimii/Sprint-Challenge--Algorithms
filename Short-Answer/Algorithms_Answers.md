#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(N)


b) O(N^2)


c) O(N)

## Exercise II

# track the highest floor: n
# track the lowest floor you can drop from: 2
# find the mid point: high - low / 2
# drop the egg from the mid point
# if it breaks:
    # drop an egg from the floor at low
    # if the egg  breaks return f as floor - 1
    # else climb up one more floor and drop an egg
    # repeat until you break an egg and return that floor - 1
# if it doesn't break update low to be mid point +1
# recalculate midpoint and drop the egg again.
# repeat:
# if it breaks:
    # drop an egg from the floor at low
    # if the egg  breaks return f as floor - 1
    # else climb up one more floor and drop an egg
    # repeat until you break an egg and return that floor - 1

Run time: O(NlogN)