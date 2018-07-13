#This script downloads the playbook folder from GitHhub

#Note: This requires subversion installed in the machine

#!/usr/bin/env python3
import sys
import subprocess
from send_get_req import *


URL=str(case_precons())
p = subprocess.Popen('svn checkout '+URL, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
print("Folder Downloaded Successfully!")




