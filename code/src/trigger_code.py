"""
Properties of this file
- will be used to trigger the code.
- the code will be running in the background.
- it will call main code when a file is created in the directory["log_files"] every 10 seconds.
"""
from main import covet_log_to_dict_from_file
import time
import datetime
import os

if __name__ == '__main__':
    path_to_watch = "log_files"
    path_for_processed_files = "processed_log_files"
    before = dict ([(f, None) for f in os.listdir (path_to_watch)])
    [covet_log_to_dict_from_file(path_to_watch + "/" + f) for f in before.keys()]
    [os.replace(path_to_watch + "/" + f,path_for_processed_files + "/" + f+f".{datetime.datetime.now().strftime('%Y_%m_%dT%H_%M_%S_%fZ')}") for f in before.keys()]
    before = {}
    while 1:
        print('waiting for 10 seconds')
        time.sleep(10)
        after = dict ([(f, None) for f in os.listdir (path_to_watch)])
        added = [f for f in after if not f in before]
        if added:
                [covet_log_to_dict_from_file(path_to_watch + "/" + f) for f in added]
                print(f'added {added}')
                [os.replace(path_to_watch + "/" + f,path_for_processed_files + "/" + f+f".{datetime.datetime.now().strftime('%Y_%m_%dT%H_%M_%S_%fZ')}") for f in added]
                print(f'moved processed files to {path_for_processed_files}')
                added = False
                before = after = {}
        else:
            print(f'nothing to add')
            before = after = {}
