from selenium import webdriver 
from time import sleep

driver = webdriver.Chrome(executable_path="/webDriver/chromedriver")
def login(username,password):    
   
    driver.get("https://instagram.com")
    sleep(4)
    driver.find_element_by_xpath(("//input[@name=\"username\"]"))\
        .send_keys((username))
    driver.find_element_by_xpath(("//input[@name=\"password\"]"))\
        .send_keys((password))
    driver.find_element_by_xpath(('//button[@type="submit"]'))\
        .click()
    sleep(5)
    driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")\
        .click()
    sleep(3)
    driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")\
        .click()
    sleep(3)
   # driver.maximize_window()#maxamize
    #like the post
    """
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    scroll dricect to end
   # driver.execute_script("window.scrollBy(0,750)","")
   scroll by pixcel
   
        
        flag = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div[2]/div/article[1]/div[2]/section[1]/span[1]/button') 
        driver.execute_script("arguments[0].scrollIntoView();",flag)
        schroll by elements
    """
    for i in range(3):
        driver.execute_script("window.scrollBy(0,950)","")
        sleep(2)
        
     

       
    
    
    
login('_un_kn_own_1234','unknown@3')#always use real id