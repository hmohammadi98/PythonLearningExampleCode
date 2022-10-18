"""next project Calculation of student grade point average  using list
"""
num1=int(input("please enter number 1:"))
num2=int(input("please enter number2:"))
num3=int(input("please enter number3:"))
number=[num1,num2,num3]
equal=0
for i in range(0,len(number)):
    equal+=number[i]
    average_number=equal/len(number)

print(average_number)
