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


# Function to toggle the power switch when the 'p' key is pressed.
# This function changes the state of the 'is_on' variable between True and False
# and adds a delay of 5 seconds after each press to prevent rapid toggling.
def power_switch():
    global is_on
    if keyboard.is_pressed("delete"):
        if is_on:
            is_on = False
        else:
            is_on = True
        time.sleep(5)


# Function to check if the Caps Lock key is currently on.
# Using ctypes to access Windows API function GetKeyState to check the state of the Caps Lock key.
# The parameter 0x14 represents the Caps Lock key.
def is_capslock_on():
    return True if ctypes.WinDLL("User32.dll").GetKeyState(capslock_key) else False


# Function to simulate holding down the 'e' key if Caps Lock is on, otherwise releasing it.
# Pressing the 'e' key to perform an action (e.g., reviving teammates) in the game
# Releasing the 'e' key if Caps Lock is off to stop performing the action.
def hold_rev():
    if is_capslock_on():
        pyautogui.keyDown(rev_key)
    else:
        pyautogui.keyUp(rev_key)


# Function to perform actions when the 'n' key is pressed.
# Pressing 'y' to open the in-game chat and typing "!medic" command to Refill health for yourself.
def fast_medic():
    if keyboard.is_pressed(medic_script):
        pyautogui.press(chat_key)
        pyautogui.typewrite(medic_command)
        pyautogui.press(enter_key)


