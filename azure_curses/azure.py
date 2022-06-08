import json
import re
import os
import subprocess

def clean_json(string):
    string = re.sub(",[ \t\r\n]+}", "}", string)
    string = re.sub(",[ \t\r\n]+\]", "]", string)

    return string


def get_azure_accounts():
    azure_accounts = str(subprocess.check_output("az account list", shell=True), "windows-1252")

    azure_accounts = clean_json(azure_accounts.strip().replace("\n\n", "\n"))

    azure_accounts = json.loads(azure_accounts)
    
    return azure_accounts


def set_azure_account(subscription_id: str):
    os.system(f"az account set -s \"{subscription_id}\"")