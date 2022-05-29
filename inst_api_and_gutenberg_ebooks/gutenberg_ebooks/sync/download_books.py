from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from logzero import logger, logfile
import logging
import logzero


#


# local pc dirs
ABS_PATH_TO_CHROMEDRIVER = '/home/nick/PycharmProjects/gutenberg_ebooks/data/input/chromedriver'
logfile("/home/nick/PycharmProjects/gutenberg_ebooks/data/logging/download/download_logfile.log")
DOWNLOAD_DIR = '/home/nick/PycharmProjects/gutenberg_ebooks/data/output/zip'

# dirs for server
# ABS_PATH_TO_CHROMEDRIVER = '/home/ubuntu/gutenberg_ebooks/data/input/chromedriver'
# logfile("/home/ubuntu/gutenberg_ebooks/data/logging/download/download_logfile.log")
# DOWNLOAD_DIR = '/home/ubuntu/gutenberg_ebooks/data/output/zip'


my_formatter = logging.Formatter('%(filename)s - %(asctime)s - %(levelname)s: %(message)s')
logzero.formatter(my_formatter)

LINK = 'https://www.gutenberg.org/files/'

START_BOOK_FROM = 501
HOW_MUCH_BOOKS_DOWNLOAD = 8


def parse_posts_links():

    chrome_options = Options()
    # specify headless mod for browser
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument('--no-sandbox')
    # specify directory for download
    prefs = {'download.default_directory': DOWNLOAD_DIR}
    chrome_options.add_experimental_option('prefs', prefs)

    with webdriver.Chrome(executable_path=ABS_PATH_TO_CHROMEDRIVER, options=chrome_options) as browser:

        for no_book in range(START_BOOK_FROM, START_BOOK_FROM + HOW_MUCH_BOOKS_DOWNLOAD):

            try:
                book_link = LINK + str(no_book) + '/'
                browser.get(book_link)

                # ВАЖНО: подсказка, когда захотим применить ниже метод, тогда надо отправлять на асинк - ты хочешь применять его \
                # потому что знаешь что не сразу получишь ответ, надо ждать.
                browser.implicitly_wait(5)

                element_1 = '//a[@href="' + str(no_book) + '-0.zip"]'
                element_2 = '//a[@href="' + str(no_book) + '.zip"]'
                try:
                    browser.find_element_by_xpath(element_1).click()
                    print(f'File {str(no_book)}-0.zip was download')
                except:
                    try:
                        browser.find_element_by_xpath(element_2).click()
                        print(f'File {str(no_book)}.zip was download')
                    except:
                        logger.info(f'Error, there is no one element {element_1} and {element_2}')

            except Exception as e:
                logger.error('There is no xpath to download book.zip', e)


parse_posts_links()


# Error, there is no one element //a[@href="40-0.zip"] and //a[@href="40.zip"]  - случай пдф
# Error, there is no one element //a[@href="89-0.zip"] and //a[@href="89.zip"]  - случай пдф
# Error, there is no one element //a[@href="181-0.zip"] and //a[@href="181.zip"]  - случай картинки
