from class_file import file_handeling, convert_log_to_dict

def covet_log_to_dict_from_file(path):
    file_data = file_handeling.get_data_from_file(path)
    for x in  convert_log_to_dict.get_data_from_list(file_data):
        return convert_log_to_dict.convet_keyvaluelist_to_dict(convert_log_to_dict.get_key_value_pair_in_list(x))
