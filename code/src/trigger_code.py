from class_file import file_handeling
from main import covet_log_to_dict_from_file
import time
import os

if __name__ == '__main__':
    path_to_watch = "log_files"
    before = dict ([(f, None) for f in os.listdir (path_to_watch)])
    while 1:
        print('waiting for 10 seconds')
        time.sleep(10)
        after = dict ([(f, None) for f in os.listdir (path_to_watch)])
        added = [f for f in after if not f in before]
        if added:
                [covet_log_to_dict_from_file(path_to_watch + "/" + f) for f in added]
                print(f'added {added}')
                added = False
                before = after
        else:
            print(f'nothing to add')
            before = after
