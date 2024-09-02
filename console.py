#!/usr/bin/python3
"""
Command Interpreter Module
"""

import cmd
import models
import shlex
import sys

class HBNBCommand(cmd.Cmd):
    """ AirBnB console interpreter """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Exits the program"""
        return True

    def do_EOF(self, line):
        """Forces exit from the program on SIGQUIT: CTRL + D"""
        return True

    def emptyline(self):
        """Returns prompt when no command is passed to prompt"""
        pass

    def do_create(self, line):
        """Creates a new instance of a model and prints its id:
            <create> <model name>"""
        if line == "":
            print("** class name missing **")
        elif line not in models.classes.keys():
            print("** class doesn't exist **")
        else:
            cls = models.classes[line]
            a_model = cls()
            a_model.save()
            print(a_model.id)

    def do_show(self, line):
        """Prints string representation of instance specified:
            <show> <model name> <id>"""
        if line == "":
            print("** class name missing **")
        else:
            attributes = line.split()
            if attributes[0] not in models.classes.keys():
                print("** class doesn't exist **")
            elif len(attributes) < 2:
                print("** instance id missing **")
            else:
                models.storage.reload()
                key = f"{attributes[0]}.{attributes[1]}"
                objects = models.storage.all()
                if key in objects.keys():
                    print(objects[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """Deletes the instance specified:
            <destroy> <model name> <id>"""
        if line == "":
            print("** class name missing **")
        else:
            attributes = line.split()
            if attributes[0] not in models.classes.keys():
                print("** class doesn't exist **")
            elif len(attributes) < 2:
                print("** instance id missing **")
            else:
                models.storage.reload()
                key = f"{attributes[0]}.{attributes[1]}"
                objects = models.storage.all()
                if key in objects.keys():
                    del(objects[key])
                    models.FileStorage._FileStorage__objects = objects
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based on class name or all if (.) is used in place of class name:
        <all> <model name> or
        <all> ."""
        if line == "":
            print("** class name missing **")
        else:
            attributes = line.split()
            if attributes[0] not in models.classes.keys() and attributes[0] != ".":
                print("** class doesn't exist **")
            else:
                models.storage.reload()
                objects = models.storage.all()
                v_list = []
                if attributes[0] == '.':
                    for v in objects.values():
                        v_list.append(v.__str__())
                    print(v_list)
                else:
                    for k in objects.keys():
                        if attributes[0] in k:
                            v_list.append(objects[k].__str__())
                    print(v_list)

    def do_update(self, line):
        """Prints string representation of instance specified:
        <update> <model name> <id> <attribute> <value>"""
        if line == "":
            print("** class name missing **")
        else:
            attributes = shlex.split(line)
            if attributes[0] not in models.classes.keys():
                print("** class doesn't exist **")
            elif len(attributes) < 2:
                print("** instance id missing **")
            else:
                models.storage.reload()
                key = f"{attributes[0]}.{attributes[1]}"
                objects = models.storage.all()
                if key not in objects.keys():
                    print("** no instance found **")
                elif len(attributes) < 3:
                    print("** attribute name missing **")
                elif len(attributes) < 4:
                    print("** value missing **")
                else:
                    objects[key].__dict__[attributes[2]] = attributes[3]
                    models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
