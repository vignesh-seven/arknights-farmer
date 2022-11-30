import os
from ppadb.client import Client
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch

os.system("adb start-server")
pwd = os.getcwd()
screenshots = pwd + "\screenshots"
screenshot_path = screenshots + "\screen.png"

# reference image paths
path_start_button = pwd + "\\reference-images\start_btn.png"
start_button = Image.open(path_start_button)
path_start_mission_button = pwd + "\\reference-images\start_mission_btn.png"
start_mission_button = Image.open(path_start_mission_button)
path_three_stars = pwd + "\\reference-images\\3-stars.png"
three_stars = Image.open(path_three_stars)

# ref cords
start_button_coords = (1040, 640, 1240, 700)  # x1, y1, x2, y2
start_mission_button_coords = (1040, 370, 1170, 645)  # x1, y1, x2, y2
three_stars_coords = (60, 290, 280, 360)  # x1, y1, x2, y2

# connect with the adb client
client = Client(host="127.0.0.1", port=5037)
device = client.device("emulator-5554")

print("Arknights Auto Farmer!")

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

# load the screenshot image
screenshot = Image.open(screenshot_path)

# check for start button
def check_start_btn():
    # mask for matching
    img_diff = Image.new("RGBA", start_button.size)

    # start searching for buttons on screen
    start_button_c = screenshot.crop(start_button_coords)

    match = pixelmatch(start_button, start_button_c, img_diff)

    if match == 0:
        return True

def check_start_mission_btn():
    # mask for matching
    img_diff = Image.new("RGBA", start_mission_button.size)

    # start searching for buttons on screen
    start_mission_button_c = screenshot.crop(start_mission_button_coords)

    match = pixelmatch(start_mission_button, start_mission_button_c, img_diff)

    if match == 0:
        return True

def check_three_stars():
    # mask for matching
    img_diff = Image.new("RGBA", three_stars.size)

    # start searching for buttons on screen
    three_stars_c = screenshot.crop(three_stars_coords)

    match = pixelmatch(three_stars, three_stars_c, img_diff)

    if match == 0:
        return True

if check_start_btn():
    print("click start button")
    # click_start_button()
if check_start_mission_btn():
    print("click start mission button")
    # click_start_mission_button()
if check_three_stars():
    print("three stars are visible")





