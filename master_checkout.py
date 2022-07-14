# master_checkout.py is designed to check out and pull from master (or main, see later) all of your repositories.
# It works on the assumption that it lives alongside your git repos, something like this:
# workspace/
#   ├─ backend/
#   ├─ frontend/
#   ├─ tda/
#   ├─ tda_amadeus/
#   ├─ master_checkout.py

# However it can also be called from anywhere if the first parameter you pass it is the directory
# where you projects live. 
# Simply run the file and it will checkout all of your projects. If there
# are any problems, it will report back the projects that failed so you can check if you 
# had any leftover code or commits leftover. 
# If you have any projects that have a primary branch as `main` instead of `master` , add them as strings
# to the following constant:
PROJECTS_WITH_MAIN_BRANCH = ['tools', 'tda']

# USAGE (in top level directory)
# python master_checkout.py
# OR (from anywhere)
# python master_checkout.py ~/workspace/
import os
import subprocess
from pathlib import Path
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def checkout_primary(project_name):
    primary_branch = 'master' if project_name not in PROJECTS_WITH_MAIN_BRANCH else 'main'
    checkout_master_process =  subprocess.Popen(['git', 'checkout', primary_branch], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)
    checkout_master_process.communicate()
    return checkout_master_process.returncode
    

def git_pull():
    pull_process = subprocess.Popen(['git', 'pull'], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)
    pull_process.communicate()
    return pull_process.returncode


if (len(sys.argv) > 1):
    first_arg = sys.argv[1]
    path_to_repos = Path(first_arg)
    if os.path.isdir(path_to_repos):
        working_dir = path_to_repos
    else:
        print(f"{bcolors.FAIL} It looks like the supplied path '{path_to_repos}' is not a proper directory{bcolors.ENDC}")
        sys.exit()
else:
    working_dir = os.getcwd()

os.chdir(working_dir)

all_current_directories = os.listdir(working_dir)
directories_with_failures=[]

for directory in all_current_directories:
    if os.path.isdir(directory) and not directory.startswith('.'):
        print(f"{bcolors.HEADER}{bcolors.BOLD}------------------------- {directory.upper()} ------------------------- {bcolors.ENDC}")
        
        os.chdir(directory)
        master_checkout_return_code = checkout_primary(directory)
        pull_from_origin_return_code = git_pull()    
        
        if master_checkout_return_code != 0 or pull_from_origin_return_code != 0:
            directories_with_failures.append(directory)

        os.chdir('..')

print("\n")

if directories_with_failures:
    print(f"{bcolors.FAIL} There were failures checking out to the following directories: {str(directories_with_failures)}{bcolors.ENDC}")
else:
    print(f"{bcolors.OKGREEN}Successfully checked out and pulled from master in all directories{bcolors.ENDC}")
