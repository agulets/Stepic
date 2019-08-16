import os
import urllib.request
from zipfile import ZipFile

START_DIR = 'main/'


def get_file_from_web(link):
    file_on_web = urllib.request.urlopen(link).read()
    file_name = link.split("/")[-1].split("?")[0]
    with open(file_name, 'wb') as downloaded_file:
        downloaded_file.write(file_on_web)
    return file_name


def unzip_file(file_name):
    zf = ZipFile(file_name, 'r')
    zf.extractall()
    zf.close()


def check_for_py(files):
    for element in files:
        if element.endswith('.py'):
            return True
    return False


def walker(start_dir):
    tree = os.walk('main')
    result_dir_list = []
    for d, dirs, files in tree:
        if check_for_py(files):
            result_dir_list.append(d)
    result_dir_list.sort()
    return result_dir_list


if __name__ == '__main__':
    url = 'https://stepik.org/media/attachments/lesson/24465/main.zip'
    file_from_web = get_file_from_web(url)
    unzip_file(file_from_web)
    for element in (walker(START_DIR)):
        print(element)
