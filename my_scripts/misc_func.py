import random
import time
import pyautogui
import my_scripts.coords_and_img as ci


def rand_cords(cords):
    x, y, max_x = cords[0], cords[1], cords[2]
    try:
        max_y = cords[3]
    except IndexError:
        max_y = max_x
    point_x = random.randint(x, x + round(max_x / 2))
    point_y = random.randint(y + 4, y + round(max_y / 2))
    return point_x, point_y


def click_queue(queue_list, sleep=1):
    for cords in queue_list:
        x, y = rand_cords(cords)
        pyautogui.leftClick(x, y)
        time.sleep(sleep)


def warp_check():
    time.sleep(25)
    while True:
        click_queue([ci.WARP_CHECK_DRONE], 2)
        if pyautogui.locateOnScreen(ci.WARP_CHECK, region=ci.TWO_MINERS_SCREEN, confidence=0.7) is None:
            break
        time.sleep(random.randint(1, 2))
    click_queue([ci.DRONE_2])


def screen_shot():
    img = pyautogui.screenshot(region=ci.RIGHT_PART_SCREEN)
    img.save(r'img/target_img.png')
