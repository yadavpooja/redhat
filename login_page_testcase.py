#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Problem: Write the test plan and create test cases based on automated
login page scenarios. Min 20 test cases ."""

"""script to automate the login page of GitHub. You will need to provide your
credentials of your github account to check valid login."
author: Pooja Yadav
email: ypooja510@gmail.com"""


import unittest
from selenium.webdriver.common.alert import Alert
from selenium import webdriver

def userdata():
    import getpass
    data = open("userdetails.txt","w")
    username = raw_input("Please enter your github username? ")
    password = getpass.getpass("Please enter your git hub password? ")
    data.write(username)
    data.write("\n")
    data.write(password)
    data.close()


class Login_page(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        data1 = open("userdetails.txt","r")
        self.user = data1.readline().strip()
        self.passwd = data1.readline().strip()
        data1.close()

    def test_case01(self):
        # To check webpage opens.
        self.driver.get("https://github.com/")
        self.assertIn("GitHub", self.driver.title)

    def test_case02(self):
        # To check webpage has login button.
        self.driver.get("https://github.com/")
        Sign_in = self.driver.find_elements_by_class_name('site-header-actions-btn')[1]
        sign_text = Sign_in.text
        self.assertEqual("Sign in",sign_text)

    def test_case03(self):
        # To check when we click on login we directed to login page.
        self.driver.get("https://github.com/")
        self.driver.find_elements_by_class_name('site-header-actions-btn')[1].click()
        element1 = self.driver.find_element_by_class_name('auth-form-header')
        ele_text = element1.text
        self.assertEqual("Sign in to GitHub",ele_text)

    def test_case04(self):
        # To check username option is present.
        self.driver.get("https://github.com/login")
        element = self.driver.find_element_by_id("login_field")
        ele_text = element.get_attribute("name")
        self.assertEqual("login",ele_text)

    def test_case05(self):
        # To check password option is present.
        self.driver.get("https://github.com/login")
        password = self.driver.find_element_by_id("password")
        password_text = password.get_attribute("type")
        self.assertEqual("password",password_text)

    def test_case06(self):
        # To check sign in option is present.
        self.driver.get("https://github.com/login")
        ele = self.driver.find_element_by_class_name("btn-primary")
        ele_text = ele.get_attribute('value')
        self.assertEqual("Sign in",ele_text)

    def test_case07(self):
        # To check forgot password option present.
        self.driver.get("https://github.com/login")
        element = self.driver.find_element_by_class_name("label-link")
        ele_text = element.text
        self.assertEqual("Forgot password?",ele_text)

    def test_case08(self):
        # To check option for new user account present.
        self.driver.get("https://github.com/login")
        element = self.driver.find_element_by_class_name("create-account-callout")
        ele_text = element.text
        self.assertEqual("New to GitHub? Create an account.",ele_text)

    def test_case09(self):
        # To check valid login.
        self.driver.get("https://github.com/login")
        element1 = self.driver.find_element_by_id("login_field")
        element1.send_keys(self.user)
        element2 = self.driver.find_element_by_id("password")
        element2.send_keys(self.passwd)
        self.driver.find_element_by_name("commit").click()
        try:
            element = self.driver.find_elements_by_class_name("css-truncate-target")[1]
            ele_text = element.text
            self.assertEqual(self.user,ele_text)
        except IndexError as e:
            self.assertEqual(self.user, 'i don\'t know who you are')

    def test_case10(self):
        # To check forgot password button direct to reset password page.
        self.driver.get("https://github.com/login")
        self.driver.find_element_by_class_name("label-link")
        self.driver.find_element_by_class_name("label-link").click()
        ele = self.driver.find_elements_by_class_name("auth-form")[0]
        ele_text = ele.text
        self.assertEqual("Reset your password\nEnter your email address and we will send you a link to reset your password.",ele_text)

    def test_case11(self):
        # To check password reset page have email id option to reset password.
        self.driver.get("https://github.com/password_reset")
        element = self.driver.find_element_by_class_name("auth-form-body")
        ele_text = element.text
        self.assertEqual("Enter your email address and we will send you a link to reset your password.",ele_text)

    def test_case12(self):
        # To check password reset page have password reset option.
        self.driver.get("https://github.com/password_reset")
        ele = self.driver.find_element_by_class_name("btn-primary")
        ele_text = ele.get_attribute('value')
        self.assertEqual("Send password reset email",ele_text)

    def test_case13(self):
        # To check popup message displayed for invalid email for forgot password.
        self.driver.get("https://github.com/password_reset")
        element1 = self.driver.find_element_by_name("email")
        element1.send_keys("kshfkjsdfj")
        self.driver.find_element_by_name("commit").click()
        alert_element = self.driver.find_elements_by_class_name('container')[1]
        alert_text = alert_element.text
        self.assertEqual("Can't find that email, sorry.",alert_text)

    def test_case14(self):
        # To check popup message displayed when submitted without entering email for forgot password.
        self.driver.get("https://github.com/password_reset")
        element1 = self.driver.find_element_by_name("email")
        element1.send_keys(" ")
        self.driver.find_element_by_name("commit").click()
        alert_element = self.driver.find_elements_by_class_name('container')[1]
        alert_text = alert_element.text
        self.assertEqual("Can't find that email, sorry.",alert_text)


    def test_case15(self):
        # To check login for invaid username and password.
        self.driver.get("https://github.com/login")
        element1 = self.driver.find_element_by_id("login_field")
        element1.send_keys("fgggh")
        element2 = self.driver.find_element_by_id("password")
        element2.send_keys("ggfh")
        self.driver.find_element_by_name("commit").click()
        alert_element = self.driver.find_elements_by_class_name('container')[1]
        alert_text = alert_element.text
        self.assertEqual("Incorrect username or password.",alert_text)


    def test_case16(self):
        # To check login when no username and password entered.
        self.driver.get("https://github.com/login")
        element1 = self.driver.find_element_by_id("login_field")
        element1.send_keys(" ")
        element2 = self.driver.find_element_by_id("password")
        element2.send_keys(" ")
        self.driver.find_element_by_name("commit").click()
        alert_element = self.driver.find_elements_by_class_name('container')[1]
        alert_text = alert_element.text
        self.assertEqual("Incorrect username or password.",alert_text)

    def test_case17(self):
        # To check login for valid username and invalid password.
        self.driver.get("https://github.com/login")
        element1 = self.driver.find_element_by_id("login_field")
        element1.send_keys(self.user)
        element2 = self.driver.find_element_by_id("password")
        element2.send_keys("dfsfs")
        self.driver.find_element_by_name("commit").click()
        alert_element = self.driver.find_elements_by_class_name('container')[1]
        alert_text = alert_element.text
        self.assertEqual("Incorrect username or password.",alert_text)

    def test_case18(self):
        # To check login for invalid username and valid password.
        self.driver.get("https://github.com/login")
        element1 = self.driver.find_element_by_id("login_field")
        element1.send_keys("sdfdgd ")
        element2 = self.driver.find_element_by_id("password")
        element2.send_keys(self.passwd)
        self.driver.find_element_by_name("commit").click()
        alert_element = self.driver.find_elements_by_class_name('container')[1]
        alert_text = alert_element.text
        self.assertEqual("Incorrect username or password.",alert_text)

    def test_case19(self):
        # To check login when only valid username is entered.
        self.driver.get("https://github.com/login")
        element1 = self.driver.find_element_by_id("login_field")
        element1.send_keys(self.user)
        element2 = self.driver.find_element_by_id("password")
        element2.send_keys(" ")
        self.driver.find_element_by_name("commit").click()
        alert_element = self.driver.find_elements_by_class_name('container')[1]
        alert_text = alert_element.text
        self.assertEqual("Incorrect username or password.",alert_text)

    def test_case20(self):
        # To check login when only valid password is entered.
        self.driver.get("https://github.com/login")
        element1 = self.driver.find_element_by_id("login_field")
        element1.send_keys(" ")
        element2 = self.driver.find_element_by_id("password")
        element2.send_keys(self.passwd)
        self.driver.find_element_by_name("commit").click()
        alert_element = self.driver.find_elements_by_class_name('container')[1]
        alert_text = alert_element.text
        self.assertEqual("Incorrect username or password.",alert_text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    userdata()
    unittest.main()
