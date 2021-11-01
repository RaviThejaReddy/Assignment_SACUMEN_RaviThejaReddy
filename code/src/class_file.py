"""
Class for some of the file operations and core logic.
"""
import os


class convert_log_to_dict():
    """
    core logic for converting log file to dictionary
    """
    def get_data_from_list(list_data):
        return [(True, x.split('|')[-1]) if all([cond in x for cond in ['cat=', 'cs1Label=', 'cs1=', 'msg=']]) else (False, x) for x in list_data]

    def get_key_value_pair_in_list(data):
        non_char = "[@_!#$%^&*()<>?/\|}{~:]"
        new_list = []
        for x in data.split():
            if '=' not in x and '=' in new_list[-1]:
                new_list[-1] += x
                new_list[-1] += ' '
            else:
                if x[x.find('=')-1] in non_char or x[x.find('=')+1] in non_char:
                    new_list[-1] += x
                    new_list[-1] += ' '
                else:
                    new_list.append(x)
        return new_list

    def convet_keyvaluelist_to_dict(keyvaluelist):
        return dict([(x[:x.index('=')], x[x.index('=')+1:]) for x in keyvaluelist])


class file_handeling():
    """
    class for file operations
    """
    def get_files_in_dir(dir_path):
        return os.listdir(dir_path)

    def get_data_from_file(file_path):
        with open(file_path, 'r') as file_data:
            return file_handeling.convert_to_list(file_data.read())

    def convert_to_list(file_data):
        return file_data.split('\n')
