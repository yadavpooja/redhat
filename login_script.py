#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Problem: Create a selenium or python test script to login
web page with username and password."""

"""script to check login on github with username and password
author: Pooja Yadav
email: ypooja510@gmail.com"""

import requests
import getpass

n = 0
while n < 3:
    user = raw_input("Please enter your github username: ")
    password = getpass.getpass("Please enter your github password: ")
    r = requests.get('https://api.github.com/user',auth=(user,password))
    result = r.status_code
    if result == 200:
        print "Login successful."
        break
    else:
        print "Login unsuccessful.\nPlease enter a valid username and password.\n"
        n += 1
        if n == 3:
            print "You have exceeded the Maximum number of Login Attempts."


