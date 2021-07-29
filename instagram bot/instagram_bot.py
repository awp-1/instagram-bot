from selenium import webdriver 
from time import sleep

driver = webdriver.Chrome(executable_path="/webDriver/chromedriver")
def login(username,password,search):    
   
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
    """
    driver.find_element_by_xpath(("//input[@placeholder=\"Search\"]"))\
        .send_keys((search))
    driver.get("https://instagram.com/" + search +"/")
    driver.find_element_by_xpath('//button[text()="Follow"]')\
        .click()
    sleep(4)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a')\
        .click()
    sleep(2)
"""

def get_unfollowers(username):
    
    driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(username))\
       .click()
    sleep(2)
    driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
       .click()
    following=get_name()
    driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
       .click()
    followers = get_names()
    not_following_back = [user for user in following if user not in followers]
    print(not_following_back)
    
    
def get_name():
   
    sleep(2)
    
    scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
    last_ht, ht = 0, 1
    while last_ht != ht:
       last_ht = ht
       sleep(1)
       ht = driver.execute_script("""
              arguments[0].scrollTo(0, arguments[0].scrollHeight); 
              return arguments[0].scrollHeight;
              """, scroll_box)
    links = scroll_box.find_elements_by_tag_name('a')
    names = [name.text for name in links if name.text != '']
      # close button
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
         .click()
    return names
            
    
    
def get_names():
   
    sleep(2)
    sugs = driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
    
    driver.execute_script('arguments[0].scrollIntoView()', sugs)
    sleep(2)
    scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
    last_ht, ht = 0, 1
    while last_ht != ht:
       last_ht = ht
       sleep(1)
       ht = driver.execute_script("""
              arguments[0].scrollTo(0, arguments[0].scrollHeight); 
              return arguments[0].scrollHeight;
              """, scroll_box)
    links = scroll_box.find_elements_by_tag_name('a')
    names = [name.text for name in links if name.text != '']
      # close button
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
         .click()
    return names
        
       
        
       
        

#username = input('Input username:')
#password = input('Input password:')

login('_un_kn_own_1234','unknown@3','shekhar_anand')#always use real id
get_unfollowers('_un_kn_own_1234')



#code to follow random
#for i in range(3):
#    for i in range(2):
 #       driver.find_element_by_xpath('//button[text()="Follow"]')\
  #          .click()
   #     sleep(2)
    #driver.refresh()