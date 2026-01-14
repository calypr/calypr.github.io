#!/usr/bin/env python

import subprocess

def sync_funnel_docs():
    subprocess.check_call(["rsync", "-av", "products/funnel/website/content/", "./docs/tools/funnel"]) 

def sync_grip_docs():
    subprocess.check_call(["rsync", "-av", "products/grip/website/content/docs/", "./docs/tools/grip"])

def sync_git_drs_docs():
    subprocess.check_call(["rsync", "-av", "products/git-drs/docs/", "./docs/tools/git-drs"])

if __name__ == "__main__":
    sync_funnel_docs()
    sync_grip_docs()
    sync_git_drs_docs()
