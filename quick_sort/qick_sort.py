
def pivote_ (list, start , end):
    
    
    pivote = list[end]
    
    j = start
    i = start-1
    tmp = None
    while j<=end:
        
        if list[j] < pivote :
            print(f"i>{i}, j>{j}, pivote:{pivote}")
            i+=1
            tmp = list[j]
            list[j] = list[i]
            list[i] = tmp
        else: pass 
        j+=1 
    
    i+=1
    tmp = list[i]
    list[i] = pivote
    list[end] = tmp

    
    return i
def quick_sort(list , start , end):
    if start>=end: return 0
    pivote = pivote_(list, start , end)
    quick_sort(list, start , pivote-1)
    quick_sort(list, pivote+1 , end)
list = [1,0,2,3,7,5,10,9,8,6,4,12,40,2,5,53,3,74,346,632,1,0,-1]
quick_sort(list, 0 , len(list)-1)
print(list)



