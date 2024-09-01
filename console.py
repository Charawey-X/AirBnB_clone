#!/usr/bin/python3
"""
Command Interpreter Module
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ AirBnB console interpreter """
    prompt = '(hbnb)'

    def do_quit(self, line):
        """Exits the program"""
        return True

    def do_EOF(self, line):
        """Forces exit from the program on SIGQUIT: CTRL + D"""
        return True

    def emptyline(self):
        """Returns prompt when no command is passed to prompt"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
