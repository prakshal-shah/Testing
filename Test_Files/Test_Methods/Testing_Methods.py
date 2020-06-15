import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from Test_Files.Locators.Locators import *


def desired_caps():
    # Desired Capabilities of my mobile
    desired_capabilities = {
        "deviceName": "1",
        "platformName": input("Enter Platform Name:"),
        "udid": input("Enter Udid no."),
        "platformVersion": "7.0",
        "appPackage": "com.bose.bosemusic",
        "appActivity": "com.bose.madrid.SplashScreenActivity"
    }
    global drivers
    drivers = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)


# Class for Signup, it contains all SignUp functions
class Sign_up:

    # Method for sign up
    def sign_up_btn(self):
        time.sleep(2)
        # Click on Sign up button
        drivers.find_element_by_id(sign_up_btn).click()
        time.sleep(35)

        # Clicking on Sign in with email
        drivers.find_element_by_xpath(sign_in_email).click()

    # Method to fill details
    def fill_signup_details(self):
        # Writing Email ID
        drivers.find_element_by_xpath(txt_email).send_keys("abcc43@gmail.com")
        time.sleep(1)

        # Writing Password
        drivers.find_element_by_xpath(txt_password).send_keys("Prak@123")

        # Writing User Name
        drivers.find_element_by_xpath(txt_username).send_keys("Prakshal")

        # Writing Last name
        drivers.find_element_by_xpath(txt_last_name).send_keys("Shah")

        # Opening Dropdown
        drivers.find_element_by_xpath(drop_down).click()
        time.sleep(3)

        touch = TouchAction(drivers)

        # Looping elements until India not shown into frame (15 times)
        for i in range(15):
            touch.press(x=475, y=1551).move_to(x=459, y=284).release().perform()
            time.sleep(2)

        # Selecting the India from Dropdown menu
        drivers.find_element_by_xpath(drp_dwn_india).click()

        # click on SignUp button
        drivers.find_element_by_xpath(sign_up).click()

    # Method to Check all privacy radio button and click oon I Agree
    def privacy_policy(self):
        # Terms of use
        drivers.find_element_by_xpath(terms_of_use).click()

        # Privacy Policy
        drivers.find_element_by_xpath(privacy_policy).click()

        # End User Licence Agreement
        drivers.find_element_by_xpath(licence_agreement).click()

        # I Agree
        drivers.find_element_by_xpath(i_agree).click()


# Function to open Profile
def open_profile():
    # Opening the profile
    drivers.find_element_by_id(profile).click()


# Function for Signout
def sign_out_btn():
    # Scrolling to the end for signout
    touch = TouchAction(drivers)
    touch.press(x=484, y=1835).move_to(x=546, y=267).release().perform()
    drivers.find_element_by_id(sign_out).click()


# Function to Allow permissions
def allow_permissions():
    # Allow notificaton
    drivers.find_element_by_id(allow_notification).click()
    time.sleep(10)
    # Allow Location
    drivers.find_element_by_id(allow_location).click()
    time.sleep(3)

    # Allowing from popup
    drivers.find_element_by_id(location_pop_up).click()
    time.sleep(5)


# Class for Login contains all Login functions
class Login:

    # Method for login
    def sign_in_btn(self):
        # Clicking on 'Sign in'
        drivers.find_element_by_id(sign_in_btn).click()
        time.sleep(30)
        # Clicking on 'Sign in with Email'
        drivers.find_element_by_xpath(sign_in_email_1).click()

    # Method to write Login details
    def fill_login_details(self):
        # Writing Login ID
        drivers.find_element_by_xpath(txt_email).send_keys("abcc@gmail.com")

        # Writing Password
        drivers.find_element_by_xpath(txt_password).send_keys("Prak@123")

        # Clicking on Sign in
        drivers.find_element_by_xpath(sign_in).click()