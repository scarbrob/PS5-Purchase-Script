'''
@author Ben Scarbrough
@date 11/19/20

I created this script to help my friend get a PS5 off of the Walmart website (#frickthebots).
This script will only work if your address and prefered payment method are saved in your Walmart account as the default option.
'''

from selenium import webdriver
from time import sleep
import random

email = "putEmailHere" # replace the text inside the quotes with your full email.
pw = "putPasswordHere" # replace the text inside the quotes with your password.
cvv = "putCardCVVHere" # replace the rext inside the quotes with cards your CVV code.

try:
    driver = webdriver.Chrome()
    driver.get('https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815')

    while True:
        try:
            addToCart = driver.find_element_by_xpath('//*[@id="add-on-atc-container"]/div[2]/section/div[1]/div[3]/button')
            addToCart.click()
            break
        except:
            sleep_number = random.randint(10,25)
            print('Add to cart button not found. Refreshing in', sleep_number, 'seconds.')
            sleep(sleep_number)
            driver.refresh()
            #print("[1] Trying to add to cart...")

    # Do the view cart button
    while True:
        try:
            viewCart = driver.find_element_by_xpath('//*[@id="cart-root-container-content-skip"]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div[1]/div[1]/button')
            viewCart.click()
            break
        except:
            pass
            #print("[2] Trying to click view cart...")

    # Do the check out button
    while True:
        try:
            checkOut = driver.find_element_by_xpath('//*[@id="cart-root-container-content-skip"]/div/div/div[1]/div[2]/div/div/div[2]/div/div/button[1]')
            checkOut.click()
            break
        except:
            pass
            #print("[3] Trying to click check out...")

    # Do the email text
    while True:
        try:
            emailAddress = driver.find_element_by_xpath('//*[@id="sign-in-email"]')
            emailAddress.send_keys(email)
            break
        except:
            pass
            #print("[4] Trying to add email address text...")

    # Do the password text
    while True:
        try:
            accountPass = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[4]/div/section/div/section/form/div[2]/div/div[1]/label/div[2]/div/input')
            accountPass.send_keys(pw)
            break
        except:
            pass
            #print("[5] Trying to add password text...")

    while True:
        try:
            signIn = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[4]/div/section/div/section/form/div[5]/button')
            signIn.click()
            break
        except:
            pass
            #print("[6] Trying to click sign in...")

    while True:
        try:
            deliveryContinue = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div/div[2]')
            deliveryContinue.click()
            break
        except:
            pass
            #print("[7] Trying to click continue on type of delivery...")

    while True:
        try:
            addressConfirm = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/button')
            addressConfirm.click()
            break
        except:
            pass
            #print([8] Trying to click confirm address...)

    while True:
        try:
            cvvSend = driver.find_element_by_xpath('//*[@id="cvv-confirm"]')
            cvvSend.send_keys(cvv)
            break
        except:
            pass
            #print([9] Trying to confirm CVV value...)


    while True:
        try:
            reviewOrder = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/button')
            reviewOrder.click()
            break
        except:
            pass
            #print([10] Trying to click review order...)

    while True:
        try:
            placeOrder = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div/button')
            placeOrder.click()
            break
        except:
            #print([11] Trying to place the order...)
            pass

    print("***!!!Success!!!*** Check your email for order confirmation.")
except:
    print("Something went wrong... try again?")
