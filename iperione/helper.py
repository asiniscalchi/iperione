import os, subprocess, uuid

def execute(command, shell=False):
    subprocess.call(command, shell=shell)
    
def getUniqueFilename():
    return str(uuid.uuid4())
