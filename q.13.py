# num=int(input("enter the number"))
# if num%5==0:
#     print("hallo")
# else:
#     print("bye")


# num=int(input("enter the number"))
# if num%7==0:
#     print("divible hai")
# else:
#     print("not divisible")


# age=int(input("enter the age of user"))
# if age>=18:
#     print("eligible to voting")
# else:
#     print("not eligible to voting")


# number_of_class=int(input("enter the number of class"))
# if number_of_class>=1 and number_of_class<=12:
#     print("it is your class number")
#     percentage_of_attendence=int(input("enter the wich percent attend the class "))
#     if percentage_of_attendence<75:
#         print("not allow to sit in the exam")
#     else:
#         print("you can sit in the exam")
# else:
#     print("that class not avalable in school")





a=int(input("enter the number of age"))
b=int(input("enter the number of age"))
c=int(input("enter the number of age"))
if a>b and a>c:
    print("oldest age is :",a)
    if b>c:
        print("yungest is ",b)
        print("among is",c)
    if c>b:
        print("yugest age is",c)
        print("among age is",b)
elif b>a and b>c:
    print("oldest age is",b)
    if a>c:
        print("yungest age is",a)
        print("among age is",c)
    if c>a:
        print("yungest age is ",c)
        print("among age is",a)
elif c>a and c>b:
    print("oldest age is",c)
    if a>b:
        print("yungest age is",a)
        print("among age is ",b)
    if b>a:
        print("yungest age is ",b) 
        print("among age is",a)


