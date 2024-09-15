print("******welcome to the number loop******")
starting_point=int(input("enter a starting point"))
ending_point=int(input("enter a ending point"))
updation=int(input("enter updation"))
choice=input("enter choice forward wise=f,reverse wise=r")
choice_1=input("enter choice for print(verticle=v)or print(horizontal=h)")
if choice== 'f':
    for i in range (starting_point,ending_point+1,updation):
        if choice_1== 'v':
           print(i)
        elif choice_1== 'h':
            print(i,end=" ")
        else:
            print("invalid input")
elif choice== 'r':
    for i in range (ending_point,starting_point-1,-updation):
        if choice_1=='v':
           print(i)
        elif choice_1=='h':
            print(i,end=" ")
        else:
             print("invalid input")   
else:
    print("invalid input")
    
print("thank you for using mini project")
print("number loop")
print("create by abhiraj singh chauhan")

