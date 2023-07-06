import math 
list_ = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,50,111,222,333,444,555,666,11111]
print(len(list_))


def Bsearch(lst, value):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] == value:
            return f"Found {value} at index {mid}"
        elif value < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return f"{value} not found in the list , it should be at {high+1}"
			
			


for x in [Bsearch(list_,1),Bsearch(list_,10),Bsearch(list_,444),Bsearch(list_,11111),Bsearch(list_,9999999),Bsearch(list_,0)]:
	print(x)
	print('---------------')

        


