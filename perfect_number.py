# This is for calculate perfect number

while True:
    number = int(input("please enter your number: "))
    sum = 0
    for i in range(1, number):
        if ((number % i) == 0):
            sum += i
    if sum == number:
        print("this number ==>", sum, "is perfect number")


    else:
        print("this number ==>", number, "is not perfect number")

    continue_q=input("continue? yes or no :  ")
    if (continue_q == "no"):
        break
    elif(continue_q == "yes"):
        continue
    else:
        print(" !!!!!!!!!! wrong input !!!!!!!!!")
        break
