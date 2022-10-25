#this project for fill list and find positive number
list=[]
list_pos=[]
for i in range(0,10):
    number=float(input("please enter  numbers for find positive numbers : "))
    list.append(number)
    if list[i]>0 :
        list_pos.append(list[i])
list_pos.sort()
print("your number ",list)
print("your positive number ",list_pos)
