#############################
#                            #
#      Step2success.in       #
#        copyright           #
##############################           
# Selenium is used for Gui testing as well as we can use it for web scrapping and web automation to fill up forms in complex sites and tools.
#pip install selenium        

#improting selenium driver(always copy paste all this function to minimse hassle)


from selenium import webdriver
import time

#importing chrome driver shuold be in same folder 

chrome_options = webdriver.ChromeOptions()


#path where driver is stored

driver=webdriver.Chrome(executable_path=r"chromedriver.exe")

#url which nned to be open

driver.get("https://step2success.in/registration-page-demo/")
print('Opening URl in chrome driver')
time.sleep(5)





f_name=driver.find_element_by_id("first_name")
f_name.send_keys("Ankit")
print('found id now sending keys')


l_name=driver.find_element_by_id("last_name")
l_name.send_keys("Kothari")


button=driver.find_element_by_id("register")
button.click()
print('found id of submit button now clicking on it')




#For submit  l_name.click()

