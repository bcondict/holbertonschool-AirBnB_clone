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
    def do_create(self, arg):
        pass
    def do_show(self, arg):
        pass
    def do_destroy(self, arg):
        pass
    def do_all(self, arg):
        pass
    def do_update(self, arg):
        pass
    def do_show(self, arg):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
