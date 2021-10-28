import sys
import pytest
sys.path.append("./code/src/")


def test_covet_log_to_dict_from_file(mocker, import_fixture):
    # Setting up mock modules
    mocker.patch.dict('sys.modules', import_fixture)
    from main import covet_log_to_dict_from_file
    return_value = covet_log_to_dict_from_file('log_files\logfile_data.log')
    assert return_value == valid_output()


def valid_output():
    return {'cat': 'C2', 'cs1Label': 'subcat', 'cs1': 'DNS_TUNNELING', 'cs2Label': 'vueUrls', 'cs2': 'https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650', 'cs3Label': 'Tags', 'cs3': 'USA,Finance', 'cs4Label': 'Url', 'cs4': 'https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323', 'cn1Label': 'severityScore', 'cn1': '900', 'msg': 'Maliciousactivity was reported in CAAS\\= A threat intelligence rule has been automatically created in DAAS. ', 'dhost': 'bad.com', 'dst': '1.1.1.1'}