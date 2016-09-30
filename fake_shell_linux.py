# -*- coding: utf-8 -*-
# A fake shell for project show, input anything to get prearranged inputs and outputs
# Prearranged inputs and outputs are written in an excel file (see "fake shell data.xlsx") in advance
# Inspired by NEO HACKER TYPER
# OS: Linux
# Reference: http://blog.csdn.net/querdaizhi/article/details/7436722
import tty
import termios
import sys
import xlrd


def shell_loop():
    # cmd
    table = xlrd.open_workbook('fake shell data.xlsx').sheet_by_name(u'Sheet1')
    input_set = table.col_values(0)
    output_set = table.col_values(1)
    cmd_len = len(input_set)
    # device setting
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    # shell
    for jj in range(0, cmd_len):
        sys.stdout.write("root>")
        sys.stdout.flush()
        input_cmd = input_set[jj]
        for ii in range(0, len(input_cmd)):
            try:
                tty.setraw(fd)
                sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            sys.stdout.write(input_cmd[ii])
            sys.stdout.flush()
        print '\n' + output_set[jj]
    # the last input hint, input e to exit.
    sys.stdout.write("root>")
    sys.stdout.flush()
    while True:
        try:
            tty.setraw(fd)
            new_char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        if new_char == 'e':
            print 'exit'
            break


def main():
    shell_loop()

if __name__ == "__main__":
    main()

