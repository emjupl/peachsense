from pyautogui import pixel as pyautogui_pixel
from pyautogui import pixelMatchesColor as pyautogui_pixelMatchesColor
from keyboard import is_pressed as keyboard_is_pressed
from keyboard import press_and_release as keyboard_press_and_release
from keyboard import write as keyboard_write
import win32api, win32con
from win32api import GetSystemMetrics
from time import sleep as time_sleep
from os import system as os_system
from os import kill as os_kill
import random
import winsound
import PIL
from cmdcolors import *

import pyautogui
import keyboard
import os

from config import *

AllCharacters = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'o',
    'p',
    'r',
    's',
    't',
    'u',
    'w',
    'y',
    'z',
    'x',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'R',
    'S',
    'T',
    'U',
    'W',
    'Y',
    'Z',
    'X',
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
]

def pickRandomListSubject(list):
    return list[random.randrange(0, len(list))]

def generateRandomKeychain(keychainlenght, list):
    keychain = ''
    while True:
        character = pickRandomListSubject(list)
        keychain += str(character)
        if len(keychain) == keychainlenght:
            return keychain


title = generateRandomKeychain(42, AllCharacters)
os.system('title ' + str(title))

def main():
    try:
        #############
        # Functions #
        #############

        snipermodeStatus = '\u001b[95mWaiting for key..'
        autoacceptStatus = False
        weaponepilepsyStatus = False


        def textOnChat(random):
            if not keyboard_is_pressed('control'):
                keyboard_press_and_release('y')
                time_sleep(0.05)
                text = messages[random] + ' | Peachsense.                                           '
                keyboard_write(text)
                keyboard_press_and_release('enter')

        def click(x):
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            time_sleep(x)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        def sound(sound):
            if sound == 'toggleStartBeep':
                winsound.Beep(2000, 100)
            elif sound == 'toggleStopBeep':
                winsound.Beep(1500, 100)
            elif sound == 'successBeep':
                winsound.Beep(2000, 100)
                winsound.Beep(1500, 100)
            elif sound == 'errorBeep':
                winsound.Beep(1500, 100)
                winsound.Beep(1000, 100)

        sound('successBeep')


        def printBanner(nd):

            if nd == 1:
                print()
                print(Colors.LightRed, '█ ▄▄  ▄███▄   ██   ▄█▄     ▄  █    ▄▄▄▄▄   ▄███▄      ▄      ▄▄▄▄▄   ▄███▄   ')
                print(Colors.Red, '█   █ █▀   ▀  █ █  █▀ ▀▄  █   █   █     ▀▄ █▀   ▀      █    █     ▀▄ █▀   ▀  ')
                print(Colors.Yellow, '█▀▀▀  ██▄▄    █▄▄█ █   ▀  ██▀▀█ ▄  ▀▀▀▀▄   ██▄▄    ██   █ ▄  ▀▀▀▀▄   ██▄▄    ')
                print(Colors.Green, '█     █▄   ▄▀ █  █ █▄  ▄▀ █   █  ▀▄▄▄▄▀    █▄   ▄▀ █ █  █  ▀▄▄▄▄▀    █▄   ▄▀ ')
                print(Colors.LightGreen, ' █    ▀███▀      █ ▀███▀     █             ▀███▀   █  █ █            ▀███▀   ')
                print(Colors.Blue, '  ▀             █           ▀                      █   ██                    ')
                print(Colors.LightBlue, '               ▀                                                             ')
            if nd == 2:
                print()
                print(Colors.LightPink,
                      '  ██▓███  ▓█████ ▄▄▄       ▄████▄   ██░ ██   ██████ ▓█████  ███▄    █   ██████ ▓█████ ')
                print('  ▓██░  ██▒▓█   ▀▒████▄    ▒██▀ ▀█  ▓██░ ██▒▒██    ▒ ▓█   ▀  ██ ▀█   █ ▒██    ▒ ▓█   ▀ ')
                print('  ▓██░ ██▓▒▒███  ▒██  ▀█▄  ▒▓█    ▄ ▒██▀▀██░░ ▓██▄   ▒███   ▓██  ▀█ ██▒░ ▓██▄   ▒███   ')
                print(Colors.Pink,'  ▒██▄█▓▒ ▒▒▓█  ▄░██▄▄▄▄██ ▒▓▓▄ ▄██▒░▓█ ░██   ▒   ██▒▒▓█  ▄ ▓██▒  ▐▌██▒  ▒   ██▒▒▓█  ▄ ')
                print('  ▒██▒ ░  ░░▒████▒▓█   ▓██▒▒ ▓███▀ ░░▓█▒░██▓▒██████▒▒░▒████▒▒██░   ▓██░▒██████▒▒░▒████▒')
                print('  ▒▓▒░ ░  ░░░ ▒░ ░▒▒   ▓▒█░░ ░▒ ▒  ░ ▒ ░░▒░▒▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░')
                print('  ░▒ ░      ░ ░  ░ ▒   ▒▒ ░  ░  ▒    ▒ ░▒░ ░░ ░▒  ░ ░ ░ ░  ░░ ░░   ░ ▒░░ ░▒  ░ ░ ░ ░  ░')
                print('  ░░          ░    ░   ▒   ░         ░  ░░ ░░  ░  ░     ░      ░   ░ ░ ░  ░  ░     ░')
                print('              ░  ░     ░  ░░ ░       ░  ░  ░      ░     ░  ░         ░       ░     ░  ░')
                print()

        def modulesStatus(bunnyhop, snipermode, autoaccept, weaponepilepsy):
            os_system('cls')
            printBanner(2)
            print(Colors.White, ' ')

            if bunnyhop:
                print(Colors.White, 'Bunnyhop:                     ', Colors.LightPink, bunnyhop)
            else:
                print(Colors.White, 'Bunnyhop:                     ', Colors.Red, bunnyhop)

            if snipermode:
                print(Colors.White, 'Snipermode:                   ', Colors.LightPink, snipermode, Colors.White, 'Status:',
                      snipermodeStatus, Colors.White, 'Delay:', Colors.LightPink,
                      '~' + str((snipermodeDelay + 0.05) * 1000) + 'ms')
            else:
                print(Colors.White, 'Snipermode:                   ', Colors.Red, snipermode)

            if autoaccept:
                print(Colors.White, 'Auto Match Accept:            ', Colors.LightPink, autoaccept)
            else:
                print(Colors.White, 'Auto Match Accept:            ', Colors.Red, autoaccept)

            if isKillMessageEnabled:
                print(Colors.White, 'Kill Messages:                ', Colors.LightPink, isKillMessageEnabled, Colors.White,'(' + str(len(messages)) + ')')

            print('')
            print(Colors.White, '-- Misc: ----------------')
            print('')

            if weaponepilepsy:
                print(Colors.White, 'Weapon Epilepsy:              ', Colors.LightPink, weaponepilepsy)
            else:
                print(Colors.White, 'Weapon Epilepsy:              ', Colors.Red, weaponepilepsy)

            print('')

            print(Colors.Gray, '----------', Colors.Bold, Colors.Pink, 'KEYBINDS', Colors.Gray, '----------')
            print(Colors.White, 'Snipermode ON/OFF Button:', Colors.LightPink, snipermodeToggleKey)
            print(Colors.White, 'Snipermode Start Button:', Colors.LightPink, snipermodeKey)
            print(Colors.White, 'Bunnyhop ON/OFF Button:', Colors.LightPink, bunnyhopToggleKey)
            print(Colors.White, 'Weapon Epilepsy ON/OFF Button:', Colors.LightPink, weaponepilepsyKey)
        ####################
        # Autostart Checks #
        ####################

        if snipermodeAutoStart:
            isSnipermodeEnabled = True
        else:
            isSnipermodeEnabled = False

        if bunnyhopAutoStart:
            isBunnyhopEnabled = True
        else:
            isBunnyhopEnabled = False

        # ERRORS

        if snipermodeToggleKey == bunnyhopToggleKey:
            print('ERROR!')
            print('SniperMode Toggle Key and Bunnyhop Toggle Key can\'t be the same!')
            sound('errorBeep')
            input()
            os_kill()

        modulesStatus(isBunnyhopEnabled, isSnipermodeEnabled, autoacceptStatus, weaponepilepsyStatus)

        # MAIN

        while True:

            ##################
            # Toggle buttons #
            ##################

            # Weapon Epilepsy toggle button
            if keyboard_is_pressed(weaponepilepsyKey):
                if not weaponepilepsyStatus:
                    weaponepilepsyStatus = True
                    modulesStatus(isBunnyhopEnabled, isSnipermodeEnabled, autoacceptStatus, weaponepilepsyStatus)
                    sound('toggleStartBeep')
                    time_sleep(0.5)
                else:
                    weaponepilepsyStatus = False
                    modulesStatus(isBunnyhopEnabled, isSnipermodeEnabled, autoacceptStatus, weaponepilepsyStatus)
                    sound('toggleStopBeep')
                    time_sleep(0.5)

            # Autoaccept toggle button
            if keyboard_is_pressed(autoacceptKey):
                if not autoacceptStatus:
                    autoacceptStatus = True
                    modulesStatus(isBunnyhopEnabled, isSnipermodeEnabled, autoacceptStatus, weaponepilepsyStatus)
                    sound('toggleStartBeep')
                    time_sleep(0.5)
                else:
                    autoacceptStatus = False
                    modulesStatus(isBunnyhopEnabled, isSnipermodeEnabled, autoacceptStatus, weaponepilepsyStatus)
                    sound('toggleStopBeep')
                    time_sleep(0.5)

            # Bunnyhop toggle button
            if keyboard_is_pressed(bunnyhopToggleKey):
                if not isBunnyhopEnabled:
                    isBunnyhopEnabled = True
                    modulesStatus(isBunnyhopEnabled, isSnipermodeEnabled, autoacceptStatus, weaponepilepsyStatus)
                    sound('toggleStartBeep')
                    time_sleep(0.5)
                else:
                    isBunnyhopEnabled = False
                    modulesStatus(isBunnyhopEnabled, isSnipermodeEnabled, autoacceptStatus, weaponepilepsyStatus)
                    sound('toggleStopBeep')
                    time_sleep(0.5)

            # Snipermode toggle button
            if keyboard_is_pressed(snipermodeToggleKey):
                if not isSnipermodeEnabled:
                    isSnipermodeEnabled = True
                    modulesStatus(isBunnyhopEnabled, isSnipermodeEnabled, autoacceptStatus, weaponepilepsyStatus)
                    sound('toggleStartBeep')
                    time_sleep(0.5)
                else:
                    isSnipermodeEnabled = False
                    modulesStatus(isBunnyhopEnabled, isSnipermodeEnabled, autoacceptStatus, weaponepilepsyStatus)
                    sound('toggleStopBeep')
                    time_sleep(0.5)

            # Autoaccept

            if weaponepilepsyStatus:
                keyboard_press_and_release('1')
                time_sleep(0.0001)
                keyboard_press_and_release('2')
                time_sleep(0.0001)
                keyboard_press_and_release('3')

            if autoacceptStatus:
                monitorHeight = GetSystemMetrics(1)
                monitorWidth = GetSystemMetrics(0)
                pixelY = monitorHeight // 2 + 1
                pixelX = monitorWidth // 2 + 1
                winsound.Beep(3000, 100)
                win32api.SetCursorPos((pixelX+random.randrange(500), pixelY+random.randrange(500)))
                win32api.SetCursorPos((pixelX+random.randrange(500), pixelY+random.randrange(500)))
                if pyautogui.locateCenterOnScreen('akceptuj.png', grayscale=True, confidence=0.5):
                    pyautogui.moveTo(pyautogui.locateCenterOnScreen('akceptuj.png', grayscale=True, confidence=0.5))
                    click(0.1)

            # Snipermode
            if isSnipermodeEnabled:  # Checks if snipermode is enabled
                if keyboard_is_pressed(snipermodeKey):
                    sound('toggleStartBeep')
                    monitorHeight = GetSystemMetrics(1)
                    monitorWidth = GetSystemMetrics(0)
                    pixelY = monitorHeight // 2 + 1
                    pixelX = monitorWidth // 2 + 1
                    r, g, b = pyautogui_pixel(pixelX, pixelY)
                    while True:
                        if pyautogui_pixelMatchesColor(pixelX, pixelY, (r, g, b), tolerance=10):
                            snipermodeStatus = '\u001b[95mWaiting for opponent..'
                            modulesStatus(isBunnyhopEnabled, isSnipermodeEnabled, autoacceptStatus, weaponepilepsyStatus)
                        else:
                            time_sleep(snipermodeDelay)
                            click(0.1)
                            snipermodeStatus = '\u001b[95mWaiting for key..'
                            modulesStatus(isBunnyhopEnabled, isSnipermodeEnabled, autoacceptStatus, weaponepilepsyStatus)
                            if isKillMessageEnabled:
                                textOnChat(random.randrange(0, len(messages)))
                            sound('successBeep')
                            break

            # Bunnyhop
            if isBunnyhopEnabled:  # Checks if bunnyhop is enabled
                if keyboard_is_pressed('spacebar'):
                    keyboard_press_and_release('spacebar')
                    time_sleep(0.01)
                    modulesStatus(isBunnyhopEnabled, isSnipermodeEnabled, autoacceptStatus, weaponepilepsyStatus)


    except:
        sound('errorBeep')
        main()

main()