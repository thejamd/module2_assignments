# 1. Write a Python program that matches a string that has an a followed by zero or more b's.
# import re
# pattern= r'ab*'
# str_pattern=input("enter the string:")
# if re.match(pattern,str_pattern):
#     print("match")
# else:
#     print("not match")

# 2. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
# import re
# pattern=r'^[a-zA-Z0-9]+$'
# chara=input("enter the character:")
# if re.match(pattern,chara):
#     print("match")
# else:
#     print("not match")
# 3. Write a python program that matches a string only contain 0-9 as the characters and it must be at least 1 char in length and no more than 6.
# import re
# pattern=r'^[0-9]{1,6}+$'
# str=["123456","123","theja"]
# for i in str:
#   if re.match(pattern,i):
#     print("valid username")
#   else:
#     print("invalid username")
# 4. Write a Python program to find sequences of lowercase letters joined with  an underscore.
# import re
# pattern = r'[a-z]+_[a-z]+'
# test_string = "this_is_a_test_string with_no_match but_this_is_a_match"
# matches = re.findall(pattern, test_string)
# for match in matches:
#     print("Found:", match)
# 5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
# import re
# patern=r'^a.*b$'
# str=input("enter the string:")
# if re.match(patern,str):
#     print("match")
# else:
#     print("not match")
# 6.A website requires the users to input username and password to register.Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length of transaction password: 6
# 6. Maximum length of transaction password: 12
import re
def check_valid(password):
    if 6<=len(password)<=12:
        if re.search("[a-z]",password):
            if re.search("[A-Z]",password):
                if re.search("[0-9]",password):
                    if re.search("[$#@]",password):
                        return True
    return False
password=input("enter the password:")
if check_valid(password):
    print("valid username")
else:
    print("invalid username")

 