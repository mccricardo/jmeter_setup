#! /usr/bin/env python
'''
Setup JMeter locally.
'''
import config
import requests
from os.path import exists, join
from zipfile import ZipFile


FILENAME = 'apache-jmeter-' + config.VERSION + '.zip'
FOLDERNAME = 'apache-jmeter-' + config.VERSION
URL = config.SOURCE + FILENAME
LOCAL_FILE_PATH = join(config.PATH_TO_INSTALL, FILENAME)
LOCAL_FOLDER_PATH = join(config.PATH_TO_INSTALL, FOLDERNAME)


def get_file(filename, filepath, url):
    '''
    Get file from url.

    Returns:
        bool: True file was downloaded successfully, False otherwise.
    '''
    # Check if already exists. If not, download and write it to disk.
    if not exists(filepath):
        # Get file
        print 'Downloading {0}. Please wait...'.format(filename)
        response = requests.get(url)
        print 'Download complete.'

        # Check if request was successful
        if not response.ok:
            return False

        try:
            # Save file to disk
            print 'Saving {0}. Please wait...'.format(filename)
            with open(filepath, 'w') as local_file:
                for block in response.iter_content(1024):
                    local_file.write(block)
            print 'Save complete.'
        except OSError:
            print 'Unable to open file'
            return False
    else:
        print '{0} already exists.'.format(filename)

    return True


def extract_file(filename, filepath, folderpath, path_to_extract):
    '''
    Extract file zip.

    Returns:
        bool: True file was extracted successfully, False otherwise.

    '''
    # Check if already exists. If not, extract it.
    if not exists(folderpath):
        try:
            print 'Extracting {0}. Please wait...'.format(filename)
            jmeter_zip = ZipFile(filepath)
            ZipFile.extractall(jmeter_zip, path=path_to_extract)
            print '{0} extracted.'.format(filename)
        except RuntimeError:
            print '{0} failed to extract.'.format(filename)
            return False
    else:
        print '{0} already extracted.'.format(filename)

    return True


def install_jmeter():
    '''
    Install JMeter locally.

    Returns:
        bool: True if it was setup successfully, False otherwise.

    '''
    if get_file('apache-jmeter', LOCAL_FILE_PATH, URL) == True:
        return extract_file(FILENAME, LOCAL_FILE_PATH,
                            LOCAL_FOLDER_PATH, config.PATH_TO_INSTALL)

    return False


def setup_jmeter():
    '''
    Main function to coordinate installation of JMeter and it's plugins.

    Returns:
        bool: True was setup successfully, False otherwise.

    '''
    if install_jmeter():
        print 'JMeter successfully  installed.'
    else:
        print 'JMeter installation failed.'


if __name__ == '__main__':
    setup_jmeter()
