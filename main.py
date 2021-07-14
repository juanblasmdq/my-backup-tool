# Created by JBC
# July 13, 2021

import os
from datetime import datetime
from typing import TextIO
import zipfile
from pathlib import Path

class ZipUtilities:
    def toZip(self, filetozip, zipfilename):
        zip_file = zipfile.ZipFile(zipfilename, 'w')
        if os.path.isfile(filetozip):
            print('Selected file zipped: ' + str(zipfilename))
            zip_file.write(filetozip)
        else:
            print('Root directory:')
            self.addFolderToZip(zip_file, filetozip)
        zip_file.close()
    
    def addFolderToZip(self, zip_file, foldertozip): 
        for file in os.listdir(foldertozip):
            full_path = os.path.join(foldertozip, file)
            if os.path.isfile(full_path):
                 print('+File added: ' + str(full_path))
                 zip_file.write(full_path)
            elif os.path.isdir(full_path):
                print('--->Entering folder: ' + str(full_path))
                self.addFolderToZip(zip_file, full_path)

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
    DEFAULT_INPUT_PATH = r'C:/_filesToZip' #r'' (raw string) indicate that special characters should not be evaluated

    BACKUP_PATH = input('Write destination path. If empty, default path "{}" will be considered: '.format(DEFAULT_BACKUP_PATH))
    INPUT_PATH = input('Write path to zip. If empty, default path "{}" will be considered: '.format(DEFAULT_INPUT_PATH))

    if not BACKUP_PATH:
        print('\n>> Using default destination path "{}"'.format(DEFAULT_BACKUP_PATH))
        input()
        BACKUP_PATH = DEFAULT_BACKUP_PATH

    if not INPUT_PATH:
        print('\n>> Using default path to zip "{}"'.format(DEFAULT_INPUT_PATH))
        input()
        INPUT_PATH = DEFAULT_INPUT_PATH

    Path(BACKUP_PATH).mkdir(parents=True, exist_ok=True) #Make dir if not exist
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