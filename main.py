'''A python script to create a zip file containing all the files and folders of
a selected path (either via CLI or config.ini file),
in a user define backup folder

Full code: https://github.com/juanblasmdq/my-backup-tool/'''

import os
from datetime import datetime
import zipfile
from pathlib import Path
from configparser import ConfigParser

import mainGUI #project-specific-module TkGUI.py

__copyright__   = 'My-backup-tool'
__version__     = 'beta'
__date__        = 'July 16, 2021'
__author__      = 'Juan Blas Carelli'
__credits__     = 'Dakosaurio'
__contact__     = 'https://github.com/juanblasmdq/my-backup-tool/'

class ZipUtilities:
    def __init__(self):
        self.originalpath ='' # Variable to be used by all class functions

    # Function to call from main. Runs only (1) time, i.e. toZip is 'non-recursive'.
    #   Other functions in class ZipUtilities are (generally) recursive
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

def get_config(section, lookup):
    config = ConfigParser()
    config.read('config.ini')
    return config[section][lookup]

def main():
    # Variable early assignment to avoid errors until GUI release. HOLD. Shall be removed later
    INPUT_PATH = ''
    BACKUP_PATH = ''
    log = ''
    msg= ''
    # Get defaults from config.ini
    CLI_USSAGE = get_config('DEFAULT', 'USE_CLI')
    DEFAULT_BACKUP_PATH = get_config('DEFAULT', 'DEFAULT_BACKUP_PATH')
    DEFAULT_INPUT_PATH = get_config('DEFAULT', 'DEFAULT_INPUT_PATH')
    
    if CLI_USSAGE.upper() == "YES":
        CLI = True
    else:
        CLI = False

    # Use Command-Line-Interface for data entry
    if CLI: 
        use_config = input('\nUse information included in "config.ini"? [y=yes]: ').lower()
        if use_config == 'y' or use_config == 'yes':
            BACKUP_PATH = get_config('WORKING_PATHS','BACKUP_PATH')
            INPUT_PATH = get_config('WORKING_PATHS','INPUT_PATH')
            print('\n>> Using "config.ini". If any path is empty, default paths will be considered.')
        else:
            BACKUP_PATH = input('Write destination path. If empty, default path "{}" will be considered: '.format(DEFAULT_BACKUP_PATH))
            INPUT_PATH = input('Write path to zip. If empty, default path "{}" will be considered: '.format(DEFAULT_INPUT_PATH)).strip('"')
        # Verification if paths are null
        if not BACKUP_PATH:
            BACKUP_PATH = DEFAULT_BACKUP_PATH
            print('\n>> Backup path was empty. Using default destination path "{}"'.format(DEFAULT_BACKUP_PATH))

        if not INPUT_PATH:
            INPUT_PATH = DEFAULT_INPUT_PATH
            print('\n>> Path to zip was empty. Using default path to zip "{}"'.format(DEFAULT_INPUT_PATH))

    # Use Graphical user interface for data entry
    else: 
        use_config = 'no'
        # HOLD
        # Run GUI here
        # GUI shall catch all values and return them to continue the script
        pass 
    
    # ****************************
    #     MAIN LOOP EXECUTION     
    # ****************************
    INPUT_PATH=INPUT_PATH.split(',') # In case multiple inputs where entried
    for pth in INPUT_PATH:
        pth = r'{}'.format(pth).strip()
        msg = '\n>> !WORKING ON PATH {}'.format(pth)

        if CLI:
            print(msg)
        else:
            log = log + '\n' + msg
            #HOLD. Update log in the GUI
            pass
        
        # Make dir BACKUP_PATH if not exist
        Path(BACKUP_PATH).mkdir(parents=True, exist_ok=True)

        # Get name of path to backup
        pth_to_back = Path(pth).name
        currDate = datetime.now().strftime('%Y-%m-%d')
        back_name = '{}_BAK-{}'.format(pth_to_back,currDate)
        back_full_name = '{}.zip'.format(os.sep.join([BACKUP_PATH,back_name]))
        back_full_name = uniquify(back_full_name) # In case name exist
        
        #Call zip creation
        utilities = ZipUtilities()
        utilities.toZip(pth, back_full_name)

        msg = ('\n>> Zip file created at "{}"'.format(BACKUP_PATH) + 
                '\n>> Zip full name == "{}"'.format(back_full_name))
        
        if CLI:
            print(msg)
        else:
            log = log + '\n' + msg
            #HOLD. Update log in the GUI
            pass
    
    #End of main loop. Write end msg
    msg = '\n>> END OF PROCESS!. You can exit now'

    if CLI:
        print(msg)
    else:
        log = log + '\n' + msg
        #HOLD. Update log in the GUI
        pass
    
if __name__ == '__main__':
    main()