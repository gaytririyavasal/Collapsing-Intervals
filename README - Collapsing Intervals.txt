
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

An interval on the number line is denoted by a pair of values like so: (3, 8). Our intervals are closed. So this interval represents all numbers between 3 and 8 inclusive. The first number is always going to be strictly less than the second number. Normally in mathematics we represent a closed interval with square brackets. But in our program we will represent an interval by means of a tuple and tuples in Python are represented with parentheses.

If we have two intervals like (7, 12) and (4, 9), they overlap. We can collapse overlapping intervals into a single interval (4, 12). But the following two intervals (-10, -2) and (1, 5) are non-intersecting intervals and cannot be collapsed.

The aim in this assignment is take a set of intervals and collapse all the overlapping intervals and print the smallest set of non-intersecting intervals in ascending order of the lower end of the interval and then print the intervals in increasing order of the size of the interval.

Input: 

You will need to read from standard input like so:

Mac:
python3 Intervals.py < intervals.in

Windows:
python Intervals.py < intervals.in

The first line in intervals.in will be a single positive integer N (1 ≤ N ≤ 100). This number denotes the number of intervals. This will be followed by N lines of data. Each line will have two integer numbers denoting an interval. The first number will be strictly less than the second number. The intervals will not be in sorted order. Assume that the data file is correct. Here is the format of intervals.in:

15
14 17
-8 -5
26 29
-20 -15
12 15
2 3
-10 -7
25 30
2 4
-21 -16
13 18
22 27
-6 -3
3 6
-25 -14

You will read in each pair of numbers and create a tuple out of them. You will store the tuples in a list. After you have read all the intervals and the list of tuples is complete, you will call the function merge_tuples(). This function will return a list of merged tuples in ascending order of the lower end of the tuples. For the input data file given the function merge_tuples() will return:

[(-25, -14), (-10, -3), (2, 6), (12, 18), (22, 30)]

You will take the output of the function merge_tuples() which is a list of tuples and pass it to the function sort_by_interval_size(). This function will return a list of tuples sorted by increasing order of the size of the intervals. If two intervals are of the same size then you should print the two intervals in ascending order of their lower ends. The list returned will be as follows:

[(2, 6), (12, 18), (-10, -3), (22, 30), (-25, -14)]

Output: 

You will print your output to standard out. Your output will have exactly two lines. The first line will be the output of the function merge_tuples() and the second line will be the output of the function sort_by_interval_size(). For the given input, the output will be as follows:

[(-25, -14), (-10, -3), (2, 6), (12, 18), (22, 30)]
[(2, 6), (12, 18), (-10, -3), (22, 30), (-25, -14)]

