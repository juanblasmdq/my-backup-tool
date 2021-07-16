'''A python script to create a zip file containing all the files and folders of
a selected path (either via CLI or config.ini file),
in a user define backup folder

Full code: https://github.com/juanblasmdq/my-backup-tool/'''

import os
from datetime import datetime
import zipfile
from pathlib import Path
from configparser import ConfigParser
import TkGUI #project-specific-module TkGUI.py

__copyright__   = 'My-backup-tool'
__version__     = ''
__date__        = 'July 15, 2021'
__author__      = 'Juan Blas Carelli'
__credits__     = ['Dakosaurio']
__contact__     = 'https://github.com/juanblasmdq/my-backup-tool/'

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
            #print('Root directory:')
            self.addFolderToZip(zip_file, filetozip)

        #Log creation
        tmp_name = 'bk-tool-tmp'
        with open(tmp_name,'w') as f:
            f.write('This zip file was automatically created with {}'.format(__copyright__))
            f.write('\n\nPath to the original file(s): {}'.format(filetozip))
            f.write('\n\nCreation date: {}'.format(datetime.now().strftime('%Y-%m-%d')))
            f.write('\nCreation time: {}'.format(datetime.now().strftime('%H:%M:%S')))
            f.write('\n\nFull project code @ {}'.format(__contact__))
            f.close()
        zip_file.write(tmp_name, arcname= 'zip_creation.log')
        os.remove(tmp_name)

        #Zip file close
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
    def zipFileArcName(self,full_name,parent_dir):
        return full_name.replace(parent_dir,'')

def uniquify(path):

    filename, extension = os.path.splitext(path)
    counter = 2
    while os.path.exists(path):
        path = filename + " (" + str(counter) + ")" + extension
        counter += 1
    return path

def get_config(lookup):
    config = ConfigParser()
    config.read('config.ini')
    return config['paths to use']['{}'.format(lookup)]

def main():
    #DEFAULTS
    CLI = True #Defines whether or not the program runes using a Command-Line-Interface
    DEFAULT_BACKUP_PATH = r'c:/_baks'
    DEFAULT_INPUT_PATH = r'c:/_filesToZip' # r'' (raw string) indicate that special characters as \U should not be evaluated

    if CLI:
        use_config = input('Use information included in "config.ini"? [y=yes]: ').lower()
    else:
        #GIU magic here
        use_config = 'no'
        pass

    if use_config == 'y':
        BACKUP_PATH = get_config('BACKUP_PATH')
        INPUT_PATH = get_config('INPUT_PATH')
        if CLI: print('Using "config.ini". If any path is empty, default paths will be considered.')
    else:
        if CLI: BACKUP_PATH = input('Write destination path. If empty, default path "{}" will be considered: '.format(DEFAULT_BACKUP_PATH))
        if CLI: INPUT_PATH = input('Write path to zip. If empty, default path "{}" will be considered: '.format(DEFAULT_INPUT_PATH)).strip('"')
        if not CLI:
            #GIU magic here
            #GUI from bkTkGUI
            #label_list = ['Destination path (empty=Default)','Path to zip (empty=Default)']
            #logContent = ''
            #GUI_extraction = bkTkGUI.ShowForm('Backup creator',label_list,'')       
            #BACKUP_PATH = GUI_extraction[0]
            #INPUT_PATH = GUI_extraction[1]
            pass

        
    if not BACKUP_PATH:
        BACKUP_PATH = DEFAULT_BACKUP_PATH
        if CLI:
            print('\n>> Using default destination path "{}"'.format(DEFAULT_BACKUP_PATH))
            input()
        if not CLI:
            #logContent = logContent + '\n' + '>> Using default destination path "{}"'.format(DEFAULT_BACKUP_PATH)
            # GUI_log.setLogValue(logContent)
            # GUI_log.update_log()
            #log.WriteToLog(logContent)
            pass

    if not INPUT_PATH:
        INPUT_PATH = DEFAULT_INPUT_PATH
        if CLI:
            print('\n>> Using default path to zip "{}"'.format(DEFAULT_INPUT_PATH))
        if not CLI:
            #logContent = logContent + '\n' +'>> Using default path to zip "{}"'.format(DEFAULT_INPUT_PATH)
            #print('\n>> Using default path to zip "{}"'.format(DEFAULT_INPUT_PATH))
            #input()
            pass
    
    # *****************
    #     MAIN LOOP    
    # *****************
    INPUT_PATH=INPUT_PATH.split(',')
    for in_path in INPUT_PATH:
        in_path = r'{}'.format(in_path).strip()

        if CLI:
            print('\n>> !WORKING ON PATH {}'.format(in_path))
        else:
            #logContent = logContent + '\n' +'>> !WORKING ON PATH {}'.format(in_path)
            pass

        Path(BACKUP_PATH).mkdir(parents=True, exist_ok=True) # Make dir if dir not exist
        folder_to_back = Path(in_path).name
        date = datetime.now().strftime('%Y-%m-%d')
        back_name = '{}_BAK-{}'.format(folder_to_back,date)
        back_full_name = '{}.zip'.format(os.sep.join([BACKUP_PATH,back_name]))
        back_full_name = uniquify(back_full_name)

        #Call zip creation
        utilities = ZipUtilities()
        utilities.toZip(in_path, back_full_name)

        if CLI:
            print('\n>> Zip file created at "{}"'.format(BACKUP_PATH))
            print('>> Zip full name == "{}"'.format(back_full_name))
        else:
            #logContent = logContent + '\n' +'>> Zip file created at "{}"'.format(BACKUP_PATH)
            #logContent = logContent + '\n' +n'>> Zip full name == "{}"'.format(back_full_name)
            pass

    if CLI:
        print('\n>> END OF PROCESS. Press any key to exit')
        input()
    else:
        #logContent = str(logContent + '\n' +'>> END OF PROCESS. Close window to exit')
        # GUI_log = bkTkGUI.LogWindow()
        # GUI_log.setLogValue(logContent)
        # GUI_log.update_log
         #GUI_log = bkTkGUI.ShowLog(logContent)
        pass
    
if __name__ == '__main__':
    main()