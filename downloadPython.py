import time
from selenium import webdriver

print("Please note that this will download the latest Python installation executible for you.")
installType = input("Enter the type of installation you require (web/executable): ")

driver = webdriver.Chrome("C:/Personal/Learning/Software/Chromedriver/v.77/chromedriver.exe")  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/')
#time.sleep(3) # Let the user actually see something!

search_box = driver.find_element_by_name('q')
search_box.send_keys('Python download')
search_box.submit()
#time.sleep(3) # Let the user actually see something!

download_page_btn = driver.find_element_by_class_name('LC20lb')
download_page_btn.click()

#time.sleep(3)

download_py = driver.find_element_by_partial_link_text('Download Python')
download_py.click()

#driver.find_element_by_partial_link_text

if installType.lower() == "executable":
    install_file = driver.find_element_by_partial_link_text('Windows x86-64 executable installer')
elif installType.lower() == "web":
    install_file == driver.find_element_by_partial_link_text('Windows x86-64 web-based installer')
else:
    print("You have entered an invalid selection.")


time.sleep(100)
#driver.quit() 