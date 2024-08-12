import time
import pyautogui
import keyboard

list_5 = [355., 356., 3., 5., 4.]  # -> 0.6


def solve(c_list):
    c_list = [element if element < 180 else element - 360 for element in list_5]

    return sum(c_list) / len(c_list)


average = solve(list_5)
print(average)
