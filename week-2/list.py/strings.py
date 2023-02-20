#!/usr/bin/env python3

#this is a single line comment
#python program to illustarate the use of operators
# Name : Starlex Mugo
# Email : starlexmugo3@gmail.com
# Date : 17th Feb 2023
# File : strings.py

poem = """This is a poem about nothing 
Its funny people laugh about nothing
"""

print(poem)

print(len(poem))

f_name = "Starlex"
s_name = "Mugo"

full_name = f_name + s_name


age = 25 # years
print("my name is" + full_name +"and i am" + str(age) + "years old")

print("My name is {} and i am {} years old".format(full_name,age))