import os
from ppadb.client import Client
from PIL import Image


os.system("adb start-server")
pwd = os.getcwd()
screenshots = pwd + "\screenshots"
screenshot_path = screenshots + "\screen.png"

client = Client(host="127.0.0.1", port=5037)
device = client.device("emulator-5554")

print("Arknights Auto Farmer!")
print(pwd)

# create the screenshots folder (if it doesnt exist already)
if not os.path.exists(screenshots):
    os.mkdir(screenshots)
    print("Created the screenshots folder")

# take a screenshot 
result = device.screencap()
with open(screenshot_path, "wb") as fp:
    fp.write(result)
    print("screenshot taken!")

# check if the start button is on screen
    # tap cords  (ON A 720P WINDOW)
        # Start: 1120 670
        # Team selection: 1100 500


image = Image.open(screenshot_path)
print(image.size)




# basically, 
    # take screenshot
    # search for start button
        # if found
            # click button
            # return
    # search for mission start button
        # if found
                # click button
                # return
    # search for exp button
        # if found
                # click button
                # return