import keyboard
import mouse
import pyautogui
import ctypes
import time
import sys

banner = """
      ___          __                __             __
 ____/ (_)__ ___  / /___ _  ___  ___/ /   ___  ____/ / __ __
/ __/ / / -_) _ \\/ __/  ' \\/ _ \\/ _  /   / _ \\/ __/ _ \\ \\ /
\\__/_/_/\\__/_//_/\\__/_/_/_/\\___/\\_,_/___/ .__/_/ /_.__/_\\_\\
                                   /___/_/ assis
"""

is_on = False

rev_key = "e"
chat_key = "y"
jump_key = "space"
enter_key = "enter"
grenade_key = "4"
capslock_key = 0x14


medic_command = "!medic"

power_script = "delete"
medic_script = "pageup"
grenad_script = "alt"


# Disabling PyAutoGUI's failsafe feature which moves the mouse to the top left corner of the screen
# if the mouse pointer is at (0, 0) coordinates. Useful when working with full-screen applications
# or games where moving the mouse to (0, 0) unintentionally could cause disruptions.
pyautogui.FAILSAFE = False


