
'''def Remove_dups(length,nos):
    for l in nos:
        if nos.count(l) > 1:
            nos.remove(l)
    print "final array",nos'''
    
def Remove_dups(length,nos):
    i = 0
    while(i<length-1):
        if nos[i] == nos[i+1]:
            print "Duplicates exist:"
            nos.remove(nos[i+1])
            print "After Duplicates removed:",nos
            length = length-1
        i += 1
    print "Final array",nos

def merge(list1, list2):
  i = 0
  j = 0
  output = []
  len1 = len(list1)
  len2 = len(list2)
  while i < len1 or j < len2:
    if i < len1 and j < len2:
      if list1[i] < list2[j]:
        output += [list1[i]]
        i = i+1
      else:
        output += [list2[j]]
        j = j+1
    elif i < len1:
      output += [list1[i]]
      i = i+1
    elif j < len2:
      output += [list2[j]]
      j = j+1
  return output
  
 
def merge_sort(list_nos):
  length = len(list_nos)
  if length <= 1:
    return list_nos
  else:
    mid = length/2
    left = list_nos[0:mid]
    right = list_nos[mid:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left, sorted_right)
  
def get_input():
  a=[]
  while(1):
    x = int(raw_input())
    if(x==-1):
       break
    a.append(x)
  return a
  
def display_result(sorted_nums):
  print sorted_nums


if __name__ == '__main__':
  #get input from user
  nums = [7,2,1,6,7,1,5,6,1,9]
  print "enter the numbers to be sorted and -1 to exit "
  #nums = get_input()
  length = len(nums)
  #sort the list
  sorted_nums = merge_sort(nums)
  #print the sorted list
  print "sorted numbers: "
  display_result(sorted_nums)
  Remove_dups(length,sorted_nums)
