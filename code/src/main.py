"""
Main class/the actual logic of the program
"""
from class_file import file_handeling, convert_log_to_dict


def covet_log_to_dict_from_file(path):
    """
    This function will take the path of the file and apply some logic and convert it to a dictionary
    input:  path of the file
    output: dictionary of the file contents after applying some logic
    """
    file_data = file_handeling.get_data_from_file(path)
    for x in convert_log_to_dict.get_data_from_list(file_data):
        if x[0]:
            print(convert_log_to_dict.convet_keyvaluelist_to_dict(
                convert_log_to_dict.get_key_value_pair_in_list(x[1])))
        else:
            print('******************************************************************')
            print(f'write it to a new file {x[1]}')
            print('******************************************************************')
