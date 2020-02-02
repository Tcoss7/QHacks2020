from selenium import webdriver

searchTerm = "Nike"



def pollCorpCritic(searchTerm):
    url = 'http://www.corporatecritic.org/home.aspx'

    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)

    searchBox = driver.find_element_by_id("txtSearch")
    searchBox.send_keys(searchTerm)

    submit = driver.find_element_by_id("btnSearch")
    submit.click()

    try:
        ethiScoreElement = driver.find_element_by_class_name("resultlistethiscore").text
        print(ethiScoreElement)
        return ethiScoreElement
    except:
        return -1

    driver.close()

pollCorpCritic(searchTerm)
