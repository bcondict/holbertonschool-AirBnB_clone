#!/usr/bin/python3
""" contains the entry point of the command interpreter. """


from ast import Store
import cmd
import sys
import shlex
import models
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity

classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """
        Class that defines HBNBCommand, defines the prompt and the methods
        to create, update, show and delete instances.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        sys.exit()

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        sys.exit()

    def empyline(self, arg):
        """Emptyline print a new line
        """
        print()
        pass

    def do_create(self, arg):
        """If arguments are valid create a new instance according to given values.
        """
        line = arg.split()
        if len(line) == 0:
            print("** class name missing **")
        else:
            if line[0] not in classes:
                print("** class doesn't exist **")
            else:
                instance = classes[line[0]]()
                instance.save()
                print(instance.id)

    def do_show(self, arg):
        """Prints a representation of an instance.
        """
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
        """Deletes an instance.
        """
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
        """Return a dictionary from objects
        """
        args = shlex.split(arg)
        my_dict = models.storage.all()
        my_list = []
        if arg:
            if args[0] not in classes:
                print("** class doesn't exist **")
                return False

            for key, value in my_dict.items():
                if args[0] in key:
                    my_list.append(str(value))
            print(my_list)

        else:
            for value in my_dict.values():
                my_list.append(str(value))
            print(my_list)

    def do_update(self, arg):
        """  Updates an instance based on the class name and id 
            by adding or updating attribute
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        else:
            my_dict = models.storage.all()
            if args[0] in classes:
                key = args[0] + "." + args[1]
                if len(args) < 2:
                    print("** instance id missing **")
                    return False
                if len(args) < 3:
                    print("** attribute name missing **")
                    return False
                if len(args) < 4:
                    print("** value missing **")
                    return False
                if key in my_dict.keys():
                    my_obj = my_dict[key]
                    setattr(my_obj, args[2], args[3])
                    models.storage.save()
            else:
                print("** class doesn't exist **")
                return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
