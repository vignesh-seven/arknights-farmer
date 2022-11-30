import os
from ppadb.client import Client
from PIL import Image


os.system("adb start-server")
pwd = os.getcwd()
screenshots = pwd + "\screenshots"
screenshot_path = screenshots + "\screen.png"

# reference image paths
path_start_button = pwd + "\\reference-images\start_btn.png"
start_button = Image.open(path_start_button)
path_start_mission_button = pwd + "\\reference-images\start_mission_btn.png"
start_mission_button = Image.open(path_start_mission_button)
path_exp_button = pwd + "\\reference-images\exp_btn.png"
exp_button = Image.open(path_exp_button)



# connect with the adb client
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


# tap cords  (ON A 720P WINDOW)
    # Start: 1120 670
    # Team selection: 1100 500


image = Image.open(screenshot_path)

crop_start_btn()


crop_mission_start_btn()


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