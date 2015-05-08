#! /usr/bin/env python
'''
Setup JMeter locally.
'''


def get_jmeter():
    '''
    Get JMeter from repository.
    '''
    pass


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
