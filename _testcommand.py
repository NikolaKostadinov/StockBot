import os

fileForTransfer = "_testcommand.py"
toInstance = "instance-stockbot-0"
command = f"gcloud compute scp {fileForTransfer} --zone=europe-west6-a {toInstance}:~"

os.system(command)