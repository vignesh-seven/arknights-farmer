import os
from ppadb.client import Client

os.system("adb start-server")
pwd = os.getcwd()
screenshots = pwd + "\screenshots"

client = Client(host="127.0.0.1", port=5037)
device = client.device("emulator-5554")

print("Arknights Auto Farmer!")
print(pwd)

# create the screenshots folder (if it doesnt exist already)
if not os.path.exists(screenshots):
    os.mkdir(screenshots)
    print("Created the screenshots folder")

