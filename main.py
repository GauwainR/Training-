import os
import sys
from pwd import getpwuid

class Ls():

    def __init__(self, dir_name):
        self.dir_name = dir_name
        try:
            self.ld = os.listdir("%s" % dir_name)
        except:
            print("Directory not found")
            sys.exit()

        self.size_list = [os.path.getsize("%s%s" % (dir_name, i)) for i in self.ld]

        self.author_list = [getpwuid(os.stat("%s%s" % (dir_name, i)).st_uid).pw_name for i in self.ld]

    def getLs(self):
        return self.ld

    def getSize(self):
        return self.size_list

    def getAuthor(self):
        return  self.author_list


def startProgram():
    dir_name = input("Folder path: ")
    folder_data = Ls(dir_name)
    for file_count in range(len(folder_data.getLs())):
        print("%s || Size: %s || Author: %s " % (folder_data.getLs()[file_count],
                                                 folder_data.getSize()[file_count],
                                                 folder_data.getAuthor()[file_count]), sep='\n')

startProgram()
