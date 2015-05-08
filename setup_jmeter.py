#! /usr/bin/env python
'''
Setup JMeter locally.
'''
import config
import requests
from os.path import exists, join


def get_jmeter():
    '''
    Get JMeter from repository.
    '''
    # URL setup
    filename = 'apache-jmeter-' + config.VERSION + '.zip'
    url = config.SOURCE + filename

    # Get file
    print 'Downloading JMeter. Please wait...'
    response = requests.get(url)
    print 'Download complete.'

    # Check if request was successful
    if not response.ok:
        return False

    # Save file on disk
    print 'Saving JMeter. Please wait...'
    local_file_path = join(config.PATH_TO_INSTALL, filename)

    # Check if already exists. If not, write it to disk.
    if not exists(local_file_path):
        try:
            with open(local_file_path, 'w') as local_file:
                for block in response.iter_content(1024):
                    local_file.write(block)
            print 'Save complete.'
        except OSError:
            print 'Unable to open file'
            return False
    else:
        print 'Already exists.'

    return True


def extract_jmeter():
    '''
    Extract JMeter zip.
    '''
    pass


def install_jmeter():
    '''
    Install JMeter locally.

    Returns:
        bool: True was setup successfully, False otherwise.

    '''
    get_jmeter()
    extract_jmeter()


def setup_jmeter():
    '''
    Main function to coordinate installation of JMeter and it's plugins.

    Returns:
        bool: True was setup successfully, False otherwise.

    '''
    install_jmeter()

if __name__ == '__main__':
    setup_jmeter()
