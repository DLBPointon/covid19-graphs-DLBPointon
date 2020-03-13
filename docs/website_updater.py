#!/usr/bin/env python3

"""
A Suplementary script to aid in the updating of the status
website dlbpointon.github.io
"""

try:
    import os

    print('Import Success')
except ImportError:
    print('Import Failed')

try:
    import re

    print('Import Success')
except ImportError:
    print('Import Failed')


def folder_finder():
    """
    A function to find and move the folder prepared by
    the covid-19 script
    """
    if os.path.exists('/home/runner/work'):
        os.popen('git config --global user.email \'damonlbp@hotmail.co.uk\'')
        os.popen('git config --global user.name \'DLBPointon\'')

        os.chdir('/home/runner/work')
        if os.path.exists('graphics/'):
            os.popen('cp -rf graphics dlbpointon.github.io/')
            print('Copied to dlbpointon.github.io')
        else:
            print('No Graphics folder found')

        os.chdir('/home/runner/work/covid19-graphs-DLBPointon/covid19-graphs-DLBPointon/dlbpointon.github.io')

    else:
        print(os.getcwd())
        os.chdir('../')
        if os.path.exists('graphics/'):
            if os.path.exists('dlbpointon.github.io/graphics'):
                os.popen('rm -rf dlbpointon.github.io/graphics')

            os.popen('cp -rf graphics dlbpointon.github.io/')
            print('Copied to dlbpointon.github.io')

        else:
            print('No Graphics folder found')
        os.chdir('dlbpointon.github.io')
        os.popen('git add graphics*')

    os.popen('git commit -a -m \'Updates for Graphics folder\'')
    os.popen('git push origin master --force')


def main():
    """
    A function to control the logic of the script
    """
    folder_finder()


if __name__ == '__main__':
    main()
