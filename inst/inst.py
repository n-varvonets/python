# -*- coding: utf-8 -*-
from json import loads
from bs4 import BeautifulSoup as BS
from selenium import webdriver
import time
import os
from pyvirtualdisplay import Display

import xmlrpc.client

def parser():
    url = "http://localhost:8069"
    db = 'alex'
    username = 'nickolay.varvonets@1000geeks.com'
    password = 'QQQqqq111'

    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    version = common.version()
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    info_post_for_login = models.execute_kw(db, uid, password, 'instagram.instagram', 'search_read', [[]],
                                            {'fields': ['user_login', 'user_pass', 'qty_posts', 'required_acc_to_find']})[-1]

    os.environ['MOZ_HEADLESS'] = '1'

    ABS_PATH_TO_CHROMEDRIVER = '/home/alex/PycharmProjects/inst/chromedriver'
    ABS_PATH_TO_GECKODRIVER = '/home/alex/PycharmProjects/inst/instascraper/geckodriver'

    LINK = 'https://www.instagram.com/'
    FIELD_PASS = '//*[@id="loginForm"]/div/div[2]/div/label/input'
    FIELD_NAME_PHONE = '//*[@id="loginForm"]/div/div[1]/div/label/input'
    BTN_LOGIN = '//div/span/a[1]/button'
    BTN_LOGIN_FORM = '//*[@id="loginForm"]/div/div[3]/button/div'
    BTN_NOT_NOW = '//*[@id="react-root"]/section/main/div/div/div/div/button'
    SECOND_BTN_NOT_NOW = '/html/body/div[4]/div/div/div/div[3]/button[2]'
    EXTRACT_INFO = '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]'

    display = Display(visible=0, size=(800, 600))
    display.start()

    with webdriver.Chrome(executable_path=ABS_PATH_TO_CHROMEDRIVER) as browser:
        email_username_login = 'nickolay.varvonets@gmail.com'
        my_pass = "Varvonets16"
        required_username_to_search = "varan_dimode"
        qty_req_posts = int(5)
        required_link = f'https://www.instagram.com/{required_username_to_search}'
        try:
            browser.get(LINK)
            time.sleep(3)
            try:
                browser.find_element_by_xpath(BTN_LOGIN).click()
            except Exception as e:
                print(e)

            browser.implicitly_wait(5)
            browser.find_element_by_xpath(FIELD_NAME_PHONE).send_keys(email_username_login)
            browser.find_element_by_xpath(FIELD_PASS).send_keys(my_pass)
            browser.find_element_by_xpath(BTN_LOGIN_FORM).click()
            browser.find_element_by_xpath(BTN_NOT_NOW).click()
            browser.find_element_by_xpath(SECOND_BTN_NOT_NOW).click()

            browser.get(required_link)
            resp = browser.page_source
            soup = BS(resp, 'html.parser')
            scripts = soup.find_all('script')
            data_script = scripts[10]
            content = data_script.contents[0]
            data_object = content[content.find('{"config"'):-1]
            data_json = loads(data_object)
            list_posts = data_json['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media'][
                'edges']

            result = {}
            for n, post in enumerate(list_posts[:qty_req_posts]):
                result[n] = {
                    'ID': post['node']['shortcode'],
                    'url_img': post['node']['thumbnail_src']
                }

            print(result)

        except Exception as e:
            print(e)
        browser.quit()

    collection_id_post = []
    collection_img = []
    for rec in result:
        collection_id_post.append(result[rec]["ID"])
        collection_img.append(result[rec]['url_img'])

    print(collection_img,collection_id_post)

    # models.execute_kw(db, uid, password, 'instagram.instagram', 'write', [[info_post_for_login['id']], {
    #     'id_post': collection_id_post,
    #     'img': collection_img,
    # }])
    #
    # search_read = models.execute_kw(db, uid, password, 'instagram.instagram', 'search_read', [[]], {'fields': ['id_post', 'img']})
    # print(search_read)

parser()
