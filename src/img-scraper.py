from selenium import webdriver
import urllib.request
import os

# Initiate webdriver, go on URL.
driver = webdriver.Firefox()
desired_url = 'https://stocksnap.io'
driver.get(desired_url)

# List of image links
image_div = driver.find_element_by_id('main')
image_links_list = image_div.find_elements_by_tag_name('a')

# Collecting href of image_links_list
all_hrefs = [link.get_attribute('href') for link in image_links_list]
image_hrefs = [image_href for image_href in all_hrefs if image_href.startswith('https://stocksnap.io/photo')]

for href in image_hrefs:
    # go to link
    driver.get(href)

    # find download button
    download_btn = driver.find_element_by_class_name('download-btn')

    # download into folder

driver.close()
