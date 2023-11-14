list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
mergedList=[]
while len(list1) !=0 and len(list2) != 0:
    if list1[0] < list2[0]:
	mergedList.append(list1[0])
	list1.pop(0)
    else:
	mergedList.append(list2[0])
	list2.pop(0)

if len(list1) == 0:
    for i in range(len(list2)):
	mergedList.append(list2[0])
	list2.pop(0)
elif len(list2) == 0:
    for i in range(len(list1)):
	mergedList.append(list1[0])
	list1.pop(0)

print(mergedList)
