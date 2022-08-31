import zipfile
from os import listdir
from os.path import isfile, join

# local pc dirs
# DIRECTORY_TO_EXTRACT_FROM = '/home/nick/PycharmProjects/gutenberg_ebooks/data/output/zip'
# DIRECTORY_TO_EXTRACT_TO = '/home/nick/PycharmProjects/gutenberg_ebooks/data/output/txt'

# dirs for server
DIRECTORY_TO_EXTRACT_FROM = '/home/ubuntu/gutenberg_ebooks/data/output/zip'
DIRECTORY_TO_EXTRACT_TO = '/home/ubuntu/gutenberg_ebooks/data/output/txt'

files = [f for f in listdir(DIRECTORY_TO_EXTRACT_FROM) if isfile(join(DIRECTORY_TO_EXTRACT_FROM, f))]

for file in files:
    dir_file_extract_from = '/'.join((DIRECTORY_TO_EXTRACT_FROM, file))
    with zipfile.ZipFile(dir_file_extract_from, 'r') as zip_ref:
        zip_ref.extractall(DIRECTORY_TO_EXTRACT_TO)
