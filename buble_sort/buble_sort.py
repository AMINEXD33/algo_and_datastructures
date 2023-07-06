def buble_sort(list):
	change = True
	end_at = len(list)-1
	while change:
		change = False
		for x in range(0, end_at):
			try :
				if list[x]>list[x+1]:
					tmp = list[x]
					list[x] = list[x+1]
					list[x+1] = tmp
					change = True
			except:pass
		end_at -= 1
		if end_at == 1 : break
	return list

sorted = buble_sort([1,2,3,7,0,120,3,4,5,6,790,22]) # small test case 
print(sorted)

#O(n^2) time complexity 
#O(1) space complexity