# Assignment_SACUMEN_RaviThejaReddy

# [Link to this repo](https://github.com/RaviThejaReddy/Assignment_SACUMEN_RaviThejaReddy)

# PROBLEM STATEMENT

* Antivirus is generating system logs with the following format.
    * file content

        SAC:0|Sacumen|CAAS|2021.2.0|3|MALICIOUS|High|cat=C2 cs1Label=subcat cs1=DNS_TUNNELING cs2Label=vueUrls cs2=https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650 cs3Label=Tags cs3=USA,Finance cs4Label=Url cs4=https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323 cn1Label=severityScore cn1=900 msg=Malicious activity was reported in CAAS\= A threat intelligence rule has been automatically created in DAAS. dhost=bad.com dst=1.1.1.1
* Write a program to take the above string as an input and provide the following output as a dictionary
    * ```
        {   
            cat: C2,
            cs1Labelsubcat,
            cs1: DNS_TUNNELING,
            cs2Label: vueUrls,
            cs2: https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650,
            cs3Label: Tags,
            cs3: USA,Finance,
            cs4Label: Url,
            cs4: https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323,
            cn1Label: severityScore,
            cn1: 900,
            msg: Malicious activity was reported in CAAS\=  A threat intelligence rule has been automatically created in DAAS.,
            dhost: bad.com,
            dst: 1.1.1.1
        }

# about this program


#  to install Required packages  run below command
* pip install pytest mock pytest-cov pytest-coverage coverage mocker


# To run Code
from root folder 
* python .\code\src\trigger_code.py

# To run Pytest
## * to generate html report 
    * python -m pytest --cov-report html


