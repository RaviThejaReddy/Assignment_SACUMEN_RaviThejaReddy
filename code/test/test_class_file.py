import sys
import pytest
import os
sys.path.append("./code/src/")


def test_covet_log_to_dict_from_file_get_data_from_list(mocker, import_fixture):
    # Setting up mock modules
    mocker.patch.dict('sys.modules', import_fixture)
    from class_file import convert_log_to_dict
    return_value = convert_log_to_dict.get_data_from_list(list_data1())
    assert return_value == valid_output1()


def test_covet_log_to_dict_from_file_get_key_value_pair_in_list(mocker, import_fixture):
    # Setting up mock modules
    mocker.patch.dict('sys.modules', import_fixture)
    from class_file import convert_log_to_dict
    return_value = convert_log_to_dict.get_key_value_pair_in_list(valid_output1()[0])
    assert return_value == valid_output2()


def test_covet_log_to_dict_from_file_convet_keyvaluelist_to_dict(mocker, import_fixture):
    # Setting up mock modules
    mocker.patch.dict('sys.modules', import_fixture)
    from class_file import convert_log_to_dict
    return_value = convert_log_to_dict.convet_keyvaluelist_to_dict(valid_output2())
    assert return_value == valid_output3()


def test_file_handeling_get_files_in_dir(mocker, import_fixture):
    # Setting up mock modules
    mocker.patch.dict('sys.modules', import_fixture)
    from class_file import file_handeling
    return_value = file_handeling.get_files_in_dir('code\src')
    assert return_value == os.listdir('code\src')


def test_file_handeling_get_data_from_file(mocker, import_fixture):
    # Setting up mock modules
    mocker.patch.dict('sys.modules', import_fixture)
    from class_file import file_handeling
    return_value = file_handeling.get_data_from_file('code\src\main.py')
    assert return_value == valid_output4('code\src\main.py')


def list_data1():
    return ['SAC:0|Sacumen|CAAS|2021.2.0|3|MALICIOUS|High|cat=C2 cs1Label=subcat cs1=DNS_TUNNELING cs2Label=vueUrls cs2=https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650 cs3Label=Tags cs3=USA,Finance cs4Label=Url cs4=https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323 cn1Label=severityScore cn1=900 msg=Malicious activity was reported in CAAS\\= A threat intelligence rule has been automatically created in DAAS. dhost=bad.com dst=1.1.1.1','SAC:0|Sacumen|CAAS|2021.2.0|3|MALICIOUS|High|cat=C2 cs1Label=subcat cs1=DNS_TUNNELING cs2Label=vueUrls cs2=https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650 cs3Label=Tags cs3=USA,Finance cs4Label=Url cs4=https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323 cn1Label=severityScore cn1=900 msg=Malicious activity was reported in CAAS\\= A threat intelligence rule has been automatically created in DAAS. dhost=bad.com dst=1.1.1.1']

def valid_output1():
    return ['cat=C2 cs1Label=subcat cs1=DNS_TUNNELING cs2Label=vueUrls cs2=https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650 cs3Label=Tags cs3=USA,Finance cs4Label=Url cs4=https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323 cn1Label=severityScore cn1=900 msg=Malicious activity was reported in CAAS\\= A threat intelligence rule has been automatically created in DAAS. dhost=bad.com dst=1.1.1.1','cat=C2 cs1Label=subcat cs1=DNS_TUNNELING cs2Label=vueUrls cs2=https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650 cs3Label=Tags cs3=USA,Finance cs4Label=Url cs4=https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323 cn1Label=severityScore cn1=900 msg=Malicious activity was reported in CAAS\\= A threat intelligence rule has been automatically created in DAAS. dhost=bad.com dst=1.1.1.1']

def valid_output2():
    return ['cat=C2', 'cs1Label=subcat', 'cs1=DNS_TUNNELING', 'cs2Label=vueUrls', 'cs2=https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650', 'cs3Label=Tags', 'cs3=USA,Finance', 'cs4Label=Url', 'cs4=https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323', 'cn1Label=severityScore', 'cn1=900', 'msg=Maliciousactivity was reported in CAAS\\= A threat intelligence rule has been automatically created in DAAS. ', 'dhost=bad.com', 'dst=1.1.1.1']

def valid_output3():
    return {'cat': 'C2', 'cs1Label': 'subcat', 'cs1': 'DNS_TUNNELING', 'cs2Label': 'vueUrls', 'cs2': 'https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650', 'cs3Label': 'Tags', 'cs3': 'USA,Finance', 'cs4Label': 'Url', 'cs4': 'https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323', 'cn1Label': 'severityScore', 'cn1': '900', 'msg': 'Maliciousactivity was reported in CAAS\\= A threat intelligence rule has been automatically created in DAAS. ', 'dhost': 'bad.com', 'dst': '1.1.1.1'}

def valid_output4(file_path):
    with open(file_path,'r') as file_data:
        return file_data.read().split('\n')