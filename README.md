ASSIGNMENTS-2
=============
Find_sum:
  Given an Sorted List A[0...N].Find the sum of elements for an input K such that A[i]+A[j] = k
  Since given array is already in sorted order technique if the sum of elements of first and last index
   elements is less than increment the start pointer otherwise decrement the end pointer
   
Remove_duplicates:
  Remove duplicates from an Unsorted list.
First sort the list so that all duplicate elements will be adjacent to each other.Time taken to sort the list is O(nlogn)
Next step is to remove all the duplicates in one pass without using another list.The order is preserved and it is in-place
algorithm.
