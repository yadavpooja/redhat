#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Problem: Write program  to extract the data from a  web page and check if the given 
Strings is present or not ."""
"""Extract the data from the given webpage ie Introduction to Docker and check
if the entered string is present or not in the data.
author : Pooja Yadav
email: ypooja510@gmail.com"""

import requests
url = "https://opensource.com/resources/what-docker"
webpage = requests.get(url)
data = webpage.text
Flag = True
while Flag:
    input = raw_input("Enter a string to check: ")
    if input in data:
        print "Given string is present.\nEnter exit to quit."
    elif input == "exit":
        print "You quit."
        Flag = False
    else:
        print "Given string not present.\nEnter exit to quit."
