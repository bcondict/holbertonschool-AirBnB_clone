#!/usr/bin/python3
""" """


import cmd, sys, shlex, models
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity

classes = {"BaseModel" : BaseModel, "User" : User, "State" : State, "City" : City,
            "Amenity" : Amenity, "Place" : Place, "Review" : Review}




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
        """  """
        line = arg.split()
        if len(line) == 0:
            print("** class name missing **")
        if line[0] != "BaseModel":
            print("** class doesn't exist **")
        instance = classes[line[0]]()
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """  """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """  """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        pass
    def do_update(self, arg):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
