month=int(input("enter the month"))
year=int(input("enter the year"))
if month==1 or month==3 or month==5 or month==8 or month==7 or month==10 or month==12:
    print("in thish month have 31 days")
elif month==4 or month==6 or month==11 or month==9:
    print("in thish month have 30 days")
elif month==2 and year%100!=0 and year%400==0 or year%4==0:
    print("in this month have 29 days")
elif month==2 and year%100==0 and month%400==0 or month%4!=0:
    print("in this month have 28 days")
else:
    print("enter the number bitween 1-12")


