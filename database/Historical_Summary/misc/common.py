#       Sgourakis Lab
#   Author: Sagar Gupta
#   Date: May 24, 2022
#   Email: sagar@sas.upenn.edu

# import required libraries
import subprocess

'''

Common methods used throughout the application

'''

def run_command(command, ignore=False):

    cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = cmd.communicate()

    if cmd.returncode != 0:
        if ignore:
            return False
        print("--- FAIL ---\n")
        print(command)
        if output[0] != None:
            print(str(output[0], 'utf-8'))
        if output[1] != None:
            print(str(output[1], 'utf-8'))
        print("\n--- FAIL ---")
        return False
    else:
        if output[0] != None:
            output = output[0].decode('utf-8')
        return output
        # return True
