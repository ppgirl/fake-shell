# A keyboard event monitor on Linux, on Windows we can use pyHook

import os
from evdev import InputDevice
from select import select
msg = ""


def k_event_loop():
    global msg
    # find keyboard id
    keyboard_id = ''
    dev_file_path = '/sys/class/input'
    os.chdir(dev_file_path)
    for ii in os.listdir(os.getcwd()):
        try:
            dev_name = file(dev_file_path + '/' + ii + '/device/name').read().strip()
        except IOError:
            continue
        if dev_name == "AT Translated Set 2 keyboard":
            keyboard_id = ii
            print "Keyboard id: " + keyboard_id
    if keyboard_id == '':
        print "Keyboard Not Found!"
        return

    # keyboard event monitor
    dev = InputDevice('/dev/input/' + keyboard_id)
    ii = 0
    while ii < 20:
        select([dev], [], [])
        for event in dev.read():
            if event.value == 1 and event.code != 0:
                # code is the key id on keyboard, see /linux/input.h
                msg += str(event.code) + '\n'
                ii += 1


def main():
    k_event_loop()
    print '\n' + msg

if __name__ == "__main__":
    main()
