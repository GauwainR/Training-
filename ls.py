#!/usr/bin/env python3

import os
from sys import argv
from pwd import getpwuid

def ls():

    dir_name = argv

    if os.path.exists("%s" % dir_name[1]):

        list_of_files = os.listdir("%s" % dir_name[1])

        for file_name in list_of_files:

            file_size = os.path.getsize("%s%s" % (dir_name[1], file_name))
            file_author_id = os.stat("%s%s" % (dir_name[1], file_name)).st_uid
            file_author = getpwuid(file_author_id).pw_name

            print("%s || Size: %s || Author: %s " % (file_name, file_size, file_author), sep='\n')

    else:
        print("Directory not found")


ls()