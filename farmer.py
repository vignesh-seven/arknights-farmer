import time
import os
import random
from ppadb.client import Client
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch

# max delay between on-screen event and a click
max_delay = 10

os.system("adb start-server")
pwd = os.getcwd()
screenshots = pwd + "\screenshots"
screenshot_path = screenshots + "\screen.png"

# reference image paths
path_start_button = pwd + "\\reference-images\start_btn.png"
start_button = Image.open(path_start_button)
# path_start_button_2 = pwd + "\\reference-images\start_btn_2.png"
# start_button_2 = Image.open(path_start_button_2)
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

# check for start button
def check_btn(image, ref, ref_coords):
    # mask for matching
    img_diff = Image.new("RGBA", ref.size)

    # start searching for buttons on screen
    ref_c = image.crop(ref_coords)

    # ref_c.show()

    match = pixelmatch(ref, ref_c, img_diff)

    if match < 2040:  # 2040 is to compensate for the sanity icon that appears on some stage's Start Button
        return True


def click_button(coords):
    # print("--- %s seconds ---" % (time.time() - start_time))

    # wait for random time
    delay = random.randint(1, max_delay)
    print("Clicking in", delay, "seconds...")
    time.sleep(delay)

    # width and height of the buttons space
    w = coords[2] - coords[0]   # x2 - x1
    h = coords[3] - coords[1]   # y2 - y1

    # adding some randomness to the click coords
    click_cords = (
        random.randint(0, w) + coords[0],  
        random.randint(0, h) + coords[1]
    )
    
    # CLICK!
    device.shell(f"input tap {click_cords[0]} {click_cords[1]}")

def the_loop():
    print("Checking...")

    # take a screenshot 
    result = device.screencap()
    with open(screenshot_path, "wb") as fp:
        fp.write(result)

    # load the screenshot image
    screenshot = Image.open(screenshot_path)

    if check_btn(screenshot, start_button, start_button_coords):
        print("Start Button found")
        click_button(start_button_coords)

    # elif check_btn(screenshot, start_button_2, start_button_coords):
    #     print("Start Button found")
    #     click_button(start_button_coords)

    elif check_btn(screenshot, start_mission_button, start_mission_button_coords):
        print("Start Mission Button found")
        click_button(start_mission_button_coords)

    elif check_btn(screenshot, three_stars, three_stars_coords):
        print("Three Stars found")
        click_button(three_stars_coords)
    else:
        print("Nothing found")

# the_loop()
while True:
    the_loop()
    time.sleep(5)