import os
from ppadb.client import Client

os.system("adb start-server")
pwd = os.getcwd()

client = Client(host="127.0.0.1", port=5037)
device = client.device("emulator-5554")

print("hello")
print(pwd)

# create the screenshots folder (if it doesnt exist already)
if (os.path.exists(pwd + "\screenshots")):
    os.mkdir(pwd + "\screenshots")
    print("Created the screenshots folder")