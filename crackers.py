def check_duplicates(anylist):
	
	for items in anylist:

		for item2 in range(1,len(anylist)-1):

			if items == anylist[item2]:
				return items

			elif items != anylist[item2]:
				return "no duplicates" 


print(check_duplicates(['apple', 'orange', 'banana', 'apple']))
#print(check_duplicates( ['Yoda', 'Moses', 'Joshua', 'Mark']))