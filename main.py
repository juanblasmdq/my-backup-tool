# Created by JBC
# July 13, 2021

import os
from datetime import datetime
from typing import TextIO
import zipfile
from pathlib import Path

class ZipUtilities:
    def __init__(self):
        self.originalpath ='' # Variable to be used by all class functions

    # Function to call from main. Runs only (1) time, i.i. toZip is 'non-recursive'. Other functions in class ZipUtilities are recursive
    def toZip(self, filetozip, zipfilename):
        zip_file = zipfile.ZipFile(zipfilename, 'w', zipfile.ZIP_DEFLATED)
        self.originalpath = filetozip
        if os.path.isfile(filetozip):
            print('Selected file zipped: ' + str(zipfilename))
            short_path= self.zipFileArcName(filetozip,str(Path(filetozip).parent))     
            zip_file.write(filetozip, arcname= short_path)
        else:
            print('Root directory:')
            self.addFolderToZip(zip_file, filetozip)
        zip_file.close()
    
    def addFolderToZip(self, zip_file, foldertozip): 
        for file in os.listdir(foldertozip):
            full_path = os.path.join(foldertozip, file)
            if os.path.isfile(full_path):
                 print('+File added: ' + str(full_path))
                 short_path= self.zipFileArcName(full_path,self.originalpath)
                 zip_file.write(full_path, arcname= short_path)
            elif os.path.isdir(full_path):
                print('--->Entering folder: ' + str(full_path))
                self.addFolderToZip(zip_file, full_path)

    # Function to avoid directory structure when zipping
    # See https://stackoverflow.com/questions/27991745/zip-file-and-avoid-directory-structure
    def zipFileArcName(self,full_name,parent_dir):
        return full_name.replace(parent_dir,'')

# Source: https://stackoverflow.com/questions/13852700/create-file-but-if-name-exists-add-number
def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 2
    while os.path.exists(path):
        path = filename + " (" + str(counter) + ")" + extension
        counter += 1
    return path

def main():
    DEFAULT_BACKUP_PATH = r'c:/_baks'
    DEFAULT_INPUT_PATH = r'c:/_filesToZip' # r'' (raw string) indicate that special characters as \U should not be evaluated

    BACKUP_PATH = input('Write destination path. If empty, default path "{}" will be considered: '.format(DEFAULT_BACKUP_PATH))
    INPUT_PATH = input('Write path to zip. If empty, default path "{}" will be considered: '.format(DEFAULT_INPUT_PATH)).strip('"')

    if not BACKUP_PATH:
        print('\n>> Using default destination path "{}"'.format(DEFAULT_BACKUP_PATH))
        input()
        BACKUP_PATH = DEFAULT_BACKUP_PATH

    if not INPUT_PATH:
        print('\n>> Using default path to zip "{}"'.format(DEFAULT_INPUT_PATH))
        input()
        INPUT_PATH = DEFAULT_INPUT_PATH

    Path(BACKUP_PATH).mkdir(parents=True, exist_ok=True) # Make dir if dir not exist
    folder_to_back = Path(INPUT_PATH).name
    date = datetime.now().strftime('%Y-%m-%d')
    back_name = '{}_BAK-{}'.format(folder_to_back,date)
    back_full_name = '{}.zip'.format(os.sep.join([BACKUP_PATH,back_name]))
    back_full_name = uniquify(back_full_name)

    utilities = ZipUtilities()
    utilities.toZip(INPUT_PATH, back_full_name)

    print('\n>> Zip file created at "{}"'.format(BACKUP_PATH))
    print('>> Zip full name == "{}"'.format(back_full_name))

main()