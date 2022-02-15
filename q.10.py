# num=int(input("enter the number of day"))
# if num==1:
#     print("sunday")
# elif num==2:
#     print("monday")
# elif num==3:
#     print("tuesday")
# elif num==4:
#     print("wednesday")
# elif num==5:
#     print("thusday")
# elif num==6:
#     print("friday")
# elif num==7:
#     print("saturday")
# else:
#     print("weekday number bitween 1-7")





# marks=int(input("enter the marks"))
# if marks<=25:
#     print("grade F")
# elif marks>25 and marks<=45:
#     print("grade e")
# elif marks>45 and marks<=50:
#     print("grade d")
# elif marks>50 and marks<=60:
#     print("grade c")
# elif marks>60 and marks<80:
#     print("grade is b")
# elif marks>=80 and marks<=100:
#     print("grade a")


# quantity=int(input("enter number"))
# cost=int(input("enter number"))
# purchase=quantity*cost
# if purchase>1000:
#     bon=purchase//10
#     bonus=purchase-bon
# print("total purchase price: ",purchase)
# print("you get bonus: ",bon)
# print("only you have to pay:",bonus)

# print(500//10)



# num=int(input("enter the number"))
# k=num%10
# if k%3==0:
#     print(k,"divisble")
# else:
#     print(k,"not divisble")






# bike_price=int(input("enter the bike price"))
# if bike_price<=50000:
#     print("5% Tax")
# elif bike_price>50000 and bike_price<=100000:
#     print("10% Tax")
# else:
#     print("15% Tax")





# city_name=str(input("enter the city name"))
# if city_name=="delhi":
#     print("red fort")
# elif city_name=="agra":
#     print("taj mahal")
# elif city_name=="jaipur":
#     print("jal mahal")
# else:
#     print("not difined city")





# num=int(input("enter the number"))
# num2=int(input("enter the nummber"))
# operter=input("enter the opetor")
# if operter=="*":
#     print(num*num2)
# elif operter=="-":
#     print(num-num2)
# elif operter=="/":
#     print(num/num2)
# elif operter=="//":
#     print(num//num2)
# elif operter=="+":
#     print(num+num2)
# else:
#     print("not valid operator")



# char=str(input("enter the charactore"))
# print(len(char))


# name1=str(input("input enter the name"))
# num2=str(input("enter the name"))
# k=num2+"  "+name1
# # j=k.strip()
# print(k)


# import datetime
# variable= datetime.datetime.now()
# print ("Current date and time : ")
# print (variable.strftime("%Y-%m-%d %H:%M:%S"))


# import datetime
# a=datetime.datetime.now()
# print(a.strftime("%Y-%m-%d %H:%M:%S"))


# num=str(input("enter any name"))
# k=num.split()
# print(k[1])



# name=str(input("enter the name"))
# if "is" not in name:
#     k=name+"is"
#     print(k)
# else:
#     k=name
#     print(k)




# day=int(input("enter the number of day"))
# if day<=5:
#     print("Rs 2/day")
# elif day>6 and day<10:
#     print("Rs 3/ day")
# elif day>=10 and day<=15:
#     print("Rs 4/day")
# else:
#     print("Rs 5/day")



# day=str(input("enter the number of day"))
# i=0
# while i<len(day):
#     if day[i] in "123456789":
#         print("int")
#     elif day[i] in "abcdefghijklmnopqrstuvwxyz":
#         print("str")
#     i=i+1






# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=int(input("enter the number"))
# if a>b and a>c:
#     if b>c:
#         print("median value is",b)
#     if c>b:
#         print("mediam value s ",c)

# elif b>a and b>c:
#     if a>c:
#         print("mediam value i",a)
#     if c>a:
#         print("mediam valu is",c)
# elif c>a and c>b:
#     if b>a:
#         print("mediam vale is",b)
#     if a>b:
#         print("mediam alue is",a)




# year=int(input("enter the year"))
# if year%100!=0 and year%400==0 or year%4==0:
#     leap_year=True
#     print("leap yaer")
# else:
#     leap_year=False
#     print("not leap year")
# month=int(input("enter the month"))
# if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#     len_month=31
# elif month==2:
#     if leap_year:
#         len_month=29
#     else:
#         len_month=28
# else:
#     len_month=30
# print(len_month)
# day=int(input("enter the day[1-31]"))
# if len_month>day:
#     day=day+1
# else:
#     day=1
#     if month==12:
#         month=1
#         year=year+1
#     else:
#         month=month+1

# print(day,month,year)





# num=int(input("enter the number"))
# i=1
# for i in range(1,11):
#     k=num*i
#     print(num,"*",i,"=",k)

