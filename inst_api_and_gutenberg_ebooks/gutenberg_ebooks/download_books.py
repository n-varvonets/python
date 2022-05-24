from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ABS_PATH_TO_CHROMEDRIVER = '/home/nick/PycharmProjects/gutenberg_ebooks/data/input/chromedriver'
LINK = 'https://www.gutenberg.org/files/'
DOWNLOAD_DIR = '/home/nick/PycharmProjects/gutenberg_ebooks/data/output/zip'

HOW_MUCH_BOOKS_DOWNLOAD = 300


def parse_posts_links():

    chrome_options = Options()
    # specify headless mod for browser
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    # specify directory for download
    prefs = {'download.default_directory': DOWNLOAD_DIR}
    chrome_options.add_experimental_option('prefs', prefs)

    with webdriver.Chrome(executable_path=ABS_PATH_TO_CHROMEDRIVER, options=chrome_options) as browser:

        for no_book in range(170, HOW_MUCH_BOOKS_DOWNLOAD + 1):
            try:
                book_link = LINK + str(no_book) + '/'
                browser.get(book_link)
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
                        print(f'Error, there is no one element {element_1} and {element_2}')

            except Exception as e:
                print('There is no xpath to download book.zip', e)


parse_posts_links()

# Error, there is no one element //a[@href="40-0.zip"] and //a[@href="40.zip"]  - случай пдф
# Error, there is no one element //a[@href="89-0.zip"] and //a[@href="89.zip"]  - случай пдф
# Error, there is no one element //a[@href="181-0.zip"] and //a[@href="181.zip"]  - случай картинки
# ....
