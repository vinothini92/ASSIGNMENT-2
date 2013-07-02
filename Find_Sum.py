def Find_sum(k,nums):
    length = len(nums)
    i = 0
    j = length-1
    for x in range(length):
        if i < j:
            if nums[i]+nums[j] == k:
                break
            elif nums[i]+nums[j] < k:
                i = i+1
            elif nums[i]+nums[j] > k:
                j = j-1 
        else:
             print "not found"
             return 0
    print "Two elements are %d,%d and found at %d,%d and "%(nums[i],nums[j],i,j)
    

def get_input():
    a = []
    while(1):
        x = int(raw_input())
        if(x==-1):
            break
        a.append(x)
    return a


if __name__ == '__main__':
    print "enter the sorted numbers"
    #nums = [4,5,6,7,8]
    nums  = get_input()
    print "enter the element K to find sum in list: "
    k = int(raw_input())
    Find_sum(k,nums)
