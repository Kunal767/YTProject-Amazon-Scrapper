from selenium import webdriver

search_term = input("Enter Your Search Term:- ")

driver = webdriver.Chrome()
driver.get('https://www.amazon.in')

driver.find_element_by_id('twotabsearchtextbox').send_keys(search_term)
driver.find_element_by_id('nav-search-submit-button').click()

products = driver.find_elements_by_xpath('//div[@data-component-type="s-search-result"]')

for product in products:
    product.find_element_by_tag_name('a').click()

    driver.switch_to.window(driver.window_handles[1])
    try:
        title = driver.find_element_by_id('productTitle').text
    except:
        title = "Not Available"
    try:
        mrp = driver.find_element_by_xpath('//span[@class="priceBlockStrikePriceString a-text-strike"]').text
    except:
        mrp = "Not Available"
    try:
        price = driver.find_element_by_id('priceblock_ourprice').text
    except:
        price = "Not Available"
    try:
        discount = driver.find_element_by_xpath('//td[@class="a-span12 a-color-price a-size-base priceBlockSavingsString"]').text
    except:
        discount = "Not Available"
    try:
        availability = driver.find_element_by_id('availability').text
    except:
        availability = "Not Present"

    print(f"Title:- {title}")
    print(f"MRP:- {mrp}")
    print(f"Price:- {price}")
    print(f"Discount:- {discount}")
    print(f"Availability:- {availability}")
    print(f"Url:- {driver.current_url}")

    driver.close()
    driver.switch_to.window(driver.window_handles[0])