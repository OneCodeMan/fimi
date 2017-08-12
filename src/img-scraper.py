from selenium import webdriver
import urllib.request
import os
import uuid

# Initiate webdriver, go on URL.
driver = webdriver.Firefox()
desired_url = 'https://stocksnap.io'
driver.get(desired_url)

# Directory behaviour
dir_exists = False
dir_version = 1

while not dir_exists:
	desired_dir = 'assets/img/stocksnap' + str(dir_version)

	if os.path.exists(desired_dir):
		dir_version += 1
	else:
		os.makedirs(desired_dir)
		dir_exists = True

# List of image links
image_div = driver.find_element_by_id('main')
image_links_list = image_div.find_elements_by_tag_name('a')

# Collecting href of image_links_list
href_target = 'https://stocksnap.io/photo'
all_hrefs = [link.get_attribute('href') for link in image_links_list]
image_hrefs = [image_href for image_href in all_hrefs if image_href.startswith(href_target)]

for (i, href) in enumerate(image_hrefs):

    # go to link
    driver.get(href)

    # get div
    img_div = driver.find_element_by_class_name('img-col')

    # get src
    src = img_div.find_element_by_tag_name('img').get_attribute('src')

    # download into directory
    filename = os.path.join(desired_dir, str(uuid.uuid4()) + '.jpg')
    urllib.request.urlretrieve(src, filename)

driver.close()
