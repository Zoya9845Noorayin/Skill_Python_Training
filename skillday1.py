            ###set###
# a={10,20,30,40}
# print(a[0])

# a={10,2.5,}
# print(a)

           ###dictionary###
# a={'a':10,'b':20}
# a['c':30]
# print(a)

# a = {'a':[10,20,30],'b':40}
# print(a['a'][1])


              ###slicing###
#positive indexing
# a='Hello'
# print(a[2:3+1:1])
# print(a[2:4])

#negative indexing
# a="Good Moring"
# print(a[-4:-1])
# a='hello'
# print(a[-1:-5])


# a ='Good Morning'
# # print(a[1:5+1:2])
# # print(a[5:11+1:3])
# print(a[-7::3])
# a='Good Morning'
# print(a[-2: -8-1:-3])
# print(len(a[-2: -8-1:-3]))

                ###input types###
# a=input("enter:")
# print(a)
# a=eval(input('enter:'))
# print(a,type(a))

                ###conditional statements###
    #if else#
# a=int(input('enter:'))
# if a%2==0:
#     print("the number is even")

# else: 
#     print("the number is odd")


# //check wher the list length is 5 or not//
# a=eval(input("enter"))
# print(a)
# print(len(a))
# if len(a)==5:
#     print("Length is 5")
# else:
#     print("Length is not 5")


##ASCII VALVU##
# variable=input("enter:")
# print(variable)
# print(ord(variable))

      ##elif##
# ch=input("enter:")

# if"A"<=ch<="Z":
#      print("Upper")
# elif "a"<=ch<="z":
#      print("lower")
# else:
#      print("not an alphabat")


#        ##nestedif##
# un=input("enter:")
# pw=input('enetr:')
# if un=='pagal_insaan':
#     print('correct username')
   
#     if pw=="@1234":
#         print("your account")
        
#     else:
#         print("wrong pasword")
# else:
#     ("enter correct user name")



         ##for loop##
# for i in range(1,51):
#     print(i)

         ##while loop##
# i=1
# while i<=100:
#     print(i)
#     i+=1

# i=2
# while i<=50:
#     print(i)
#     i+=2


# n=int(input('enter num:'))
# rev=0
# while n>0:
#     id=n%10
#     n=n//10
#     rev=rev*10+id
# print(rev) 


            ###for loop###
# l=[0,20,30]
# for i in l:
#     print(i)


# s=input('enter:')
# out=''
# for i in s:
#         if "A"<=chr<="Z":
#                 out+=chr(ord(i)+32)
#         elif'a'<=i<='z':
#                out+=chr(ord(i)-32)
#         else:
#                out+=i
# print(out)


# s=input("enter:")
# rev=''

# for i in s:
#         rev=i+rev
# print(rev)


               ###nested for loop###
# for i in range(1,6):
#     for j in range(1,6):
#         print('*',end='')
#     print()

           ###backward slash###
# for i in range(1,6):
#     for j in range(1,6):
#         if i==j:
#             print('*',end=' ')
#         else:
#             print('@',end=' ')
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if i>=j:
#             print('*',end=' ')
#         else:
#             print('@',end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if i<=j:
#             print('*',end=' ')
#         else:
#             print('@',end=' ')
#     print()




        