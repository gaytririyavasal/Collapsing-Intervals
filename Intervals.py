#  File: Intervals.py

#  Description: The following program collapses all overlapping intervals, prints the non-intersecting intervals such that the lower end of the interval is always increasing, and subsequently prints the intervals in ascending order of interval size.

#  Student Name: Gaytri Vasal

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: 1/28/22

#  Date Last Modified: 1/31/22

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval

def merge_tuples (tuples_list):

    # sorts intervals in ascending order of each interval's lower end
    tuples_list.sort()

    # start at first interval
    element = 0

    # instantiates list to store merged tuples
    mergedtupleslist = []
    
    # loop runs until all remaining intervals have been traversed
    while element < len(tuples_list):
        
        # first assume that interval cannot be collapsed and store in variable
        mergedtuple = tuples_list[element] 

        # assesses whether upper end of this interval collapses with lower end of next interval
        while (element < len(tuples_list) - 1) and (mergedtuple[1] >= tuples_list[element + 1][0]):

            # evaluates whether upper end of this interval is greater than upper end of next interval, and if so, merge from lower end of this interval to upper end of this interval
            if (tuples_list[element + 1][1] <= mergedtuple[1]):
                mergedtuple = (mergedtuple[0], mergedtuple[1])

            # if the condition above is not true, merge from lower end of this interval to upper end of next interval
            else:
                mergedtuple = (mergedtuple[0], tuples_list[element + 1][1])
            # proceed to next interval
            element += 1
            
        else:
            # proceed to next interval
            element += 1
            
        # add collapsed interval to list of merged tuples
        mergedtupleslist.append(mergedtuple)
        
    # return list of non-intersecting intervals, which are sorted such that the lower end of intervals continuously increases
    return mergedtupleslist
    
# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval

def sort_by_interval_size (tuples_list):
    
    # loop through elements in tuples_list -- for each iteration, the next highest
    # value is sorted
    for i in range(len(tuples_list)):
        
        # iterates through portion tuples_list that has not been sorted
        for j in range(len(tuples_list) - i - 1):
              
            # interval of current tuple
            current_diff = tuples_list[j][1]-tuples_list[j][0]
            # interval of next tuple
            next_diff = tuples_list[j+1][1] - tuples_list[j+1][0]
            
            # 1st element of current tuple
            current_start = tuples_list[j][0]
            # 1st element of next tuple
            next_start = tuples_list[j+1][0]
            
            
            # swaps positions if tuple's interval is larger than the next tuple's
            # interval or if the intervals of the tuple and next tuple are the same size
            # and the first value of the tuple is larger than the first value of the next tuple
            if current_diff > next_diff or (current_diff == next_diff and current_start > next_start):
                
                # creates a temporary variable and stores current tuple
                temp = tuples_list[j]
                
                # swaps current tuple with next tuple
                tuples_list[j] = tuples_list[j+1]
                
                # swaps next tuple with current tuple
                tuples_list[j+1] = temp
         
    return tuples_list

# Input: no input
# Output: a string denoting all test cases have passed

def test_cases ():
    
  # test cases are written below
  assert merge_tuples([(1,2)]) == [(1,2)]
  assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
  assert sort_by_interval_size([(3, 6), (4, 8)]) == [(3, 8)]

  return "all test cases passed"

def main():
  # open file intervals.in and begin reading the data to create a list of tuples    
    import sys
    
  # instantiates list to store tuples
    listoftuples = []
    
  # reads number of intervals to be processed
    numberofintervals = sys.stdin.readline()
  # strips this number of any white space at the left and right of it
    numberofintervals = numberofintervals.strip()
    
    for i in range(int(numberofintervals)):
        interval = sys.stdin.readline() # reads in each interval
        interval = (interval.strip()) # strips interval of any white space at the left and right of it
        lst = interval.split( ) # creates list with lower and upper end of each interval
        tuplelst = []
        tuplelst.append(int(lst[0])) # transforms lower end of interval into integer and adds it to new list
        tuplelst.append(int(lst[1])) # transforms upper end of interval into integer and adds it to same list
        tuplepair = tuple(tuplelst) # converts list of interval ends into tuple
        listoftuples.append(tuplepair) # adds tuple to overall list of list of tuples
    
  # merge the list of tuples
    mergedtupleslist = merge_tuples(listoftuples)

  # sort the list of tuples according to the size of the interval
    sortedlist = sort_by_interval_size(merge_tuples(listoftuples))
    
  # run your test cases
    # print(test_cases())

  # write the output list of tuples from the two functions
    print(mergedtupleslist)
    print(sortedlist)
    
if __name__ == "__main__":
  main()
