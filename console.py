#!/usr/bin/python3
""" """


import cmd, sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit()
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        sys.exit()
    def empyline(self, arg):
        """Emptyline print a new line"""
        print()
        pass
    def do_create(self, arg):
        line = arg.split()
        if len(line == 0)
            print("** class name missing **")
        if line[0] not "BaseModel":
            print("** class doesn't exist **")
        


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
