def left_child(i):
    return 2*i+1

def right_child(i):
    return 2*i+2


def kway_merge(list_size,elements):
    Build_heap(elements)
    sub_array_size = len(elements)
    sort_Array = []
    sort_Array.append(elements[0])
    print "Sorted Array in Descending order", sort_Array
<<<<<<< HEAD
    while len(sort_Array)<= list_size*sub_array_size:
        i = sub_array_size-1
        j = 0
        search = elements[j]
        for subarray in nums:
            if search in subarray:
                print "Found: ",subarray
                next_element = subarray.pop(i-1)
                print "next element to be inserted: ",next_element
                elements.remove(elements[0])
                print "after removal: ",elements
                elements.insert(0,next_element)
                print "after inserting: ",elements
                Build_heap(elements)
                sort_Array.append(elements[0])
                i -=1
                print "sort array now: ",sort_Array
=======
    search = elements[0]
    for subarray in nums:
        if search in subarray:
            print "Found",subarray
            next_element = subarray.pop(i+1)
            print next_element
            elements.remove(elements[0])
            elements.insert(0,next_element)
            print "inital array now: ",elements
            Build_heap(elements)
            print "array now: ",elements
            sort_Array.append(elements[0])
            print "sort array now: ",sort_Array

 
>>>>>>> a98ca68f0c4fa78e3c230076053601751d14dc19

def heapify(nums,i,size):
    l = left_child(i)
    r = right_child(i)
    if l <= size and r <= size:
        if r != size:
            if nums[l] >= nums[r]:
                max_element = nums[l]
                max_index = l
            elif nums[l] <= nums[r]:
                max_element = nums[r]
                max_index = r
            if nums[i] >= max_element:
                print nums
                return
            elif nums[i] <= max_element:
                nums[i],nums[max_index] = max_element,nums[i]
                heapify(nums,max_index,size)
        else:
            nums[i],nums[l] = nums[l],nums[i]
            print nums

        
def Build_heap(elements):
    #actual_size = size*s
    size = len(elements)
    print "the size of the List is : %d " %size
    iterate = size//2-1
    for i in range(iterate,-1,-1):
        print "In %d iteration" %i
        heapify(elements,i,size)
    print "heapified array is : " ,elements
    
def get_input():
    a=[]
    while(1):
      x = int(raw_input())
      if(x==-1):
         break
      a.append(x)
    return a
	
if __name__ == '__main__':
    #get input from user
    #print "enter the number of sub-arrays"
    #nums = []
    #k = int(raw_input())
    global nums
    nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    list_size = len(nums)
    array_subsize = len(nums[1])
    print "Input array: ",nums
    '''for i in range(k):
        print "Enter %d Sub-array" %i
        nums.append(get_input())'''
    global initial_array
    initial_array = []
    for i in range(list_size):
        initial_array.append(nums[i][array_subsize-1])
        print initial_array
    kway_merge(list_size,initial_array)

  
    

