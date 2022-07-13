# master_checkout.py is designed to check out and pull from master all of your repositories.
# It works on the assumption that it lives alongside your git repos, something like this:
# workspace/
#   ├─ backend/
#   ├─ frontend/
#   ├─ tda/
#   ├─ tda_amadeus/
#   ├─ master_checkout.py

# if this applies, simply run the file and it will checkout all of your projects. If there
# are any problems, it will report back the projects that failed so you can check if you 
# had any leftover code sitting about. 
import os
import subprocess


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

def checkout_master():
    checkout_master_process =  subprocess.Popen(['git', 'checkout', 'master'], 
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


working_dir = os.getcwd()
all_current_directories = os.listdir(working_dir)

directories_with_failures=[]
for directory in all_current_directories:
    if os.path.isdir(directory) and not directory.startswith('.'):
        print(f"{bcolors.HEADER}{bcolors.BOLD}------------------------- {directory.upper()} ------------------------- {bcolors.ENDC}")
        
        os.chdir(directory)
        master_checkout_return_code = checkout_master()
        pull_from_origin_return_code = git_pull()    
        
        if master_checkout_return_code != 0 or pull_from_origin_return_code != 0:
            directories_with_failures.append(directory)

        os.chdir('..')

print("\n","\n")

if directories_with_failures:
    print(f"{bcolors.FAIL} There were failures checking out to the following directories: {str(directories_with_failures)}{bcolors.ENDC}")
else:
    print(f"{bcolors.OKGREEN}Successfully checked out and pulled from master in all directories{bcolors.ENDC}")
