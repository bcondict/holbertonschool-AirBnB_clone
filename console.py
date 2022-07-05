#!/usr/bin/python3
""" """


import cmd, sys


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit()
    def do_EOF(self, arg):
        sys.exit()
    def empyline(self, arg):
        print()
        pass
    def EOF(self, arg):
        pass
    def EOF(self, arg):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
