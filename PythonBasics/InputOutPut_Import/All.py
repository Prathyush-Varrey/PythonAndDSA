'''
In python default Data Type is String
'''

# Taking Input from User
userName = input('Enter Your Name :')
# Printing the output
print("UserName :", userName)
print(type(userName))
'''
Enter Your Name :Prathyush
UserName : Prathyush
<class 'str'>
'''

age = input('Enter Age')
print(age)
print(type(age))

'''
Enter Age10
10
<class 'str'>
'''
# But by type casting we can allow to make it numerical
# Type Casting String to Input
userAge = int(input('Enter User Age:'))
print(userAge)
print(type(userAge))
'''
Enter User Age:10
10
<class 'int'>
'''