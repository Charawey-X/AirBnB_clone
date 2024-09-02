#!/usr/bin/python3
"""
Command Interpreter Module
"""

from io import StringIO
import cmd
import models
import re
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
        """Creates a new instance of a model and prints its id.
        Usage:
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
        """Prints string representation of instance specified.
        Usage:
            show <model name> <id>
            <model name>.show(<id>)"""
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
        """Deletes the instance specified.
        Usage:
            destroy <model name> <id>
            <model name>.destroy(<id>)"""
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
                    del objects[key]
                    models.FileStorage._FileStorage__objects = objects
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances as specified.
        Usage:
            all <model name>
            all
            <model name>.all()"""
        models.storage.reload()
        objects = models.storage.all()
        v_list = []
        if line == "":
            for v in objects.values():
                v_list.append(v.__str__())
            print(v_list)
        else:
            attributes = line.split()
            if attributes[0] not in models.classes.keys():
                print("** class doesn't exist **")
            else:
                for k in objects.keys():
                    if attributes[0] in k:
                        v_list.append(objects[k].__str__())
                print(v_list)

    def do_update(self, line):
        """Updates instance specified with respective attribute and value.
        Usage:
            update <model name> <id> <attribute> <value>
            <model name>.update(<id>, <attribute>, <value>)"""
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

    def do_count(self, line):
        """Retrieve the number of instances of a class
        Usage:
            <model name>.count()"""
        old_stdout = sys.stdout
        sys.stdout = my_stdout = StringIO()
        self.do_all(line.split()[0])
        count = len(eval(my_stdout.getvalue()))
        sys.stdout = old_stdout
        print(count)

    def default(self, line):
        args = line.split('.')
        func = args[1].split('(')
        classes = models.classes.keys()
        methods = {"show": self.do_show, "destroy": self.do_destroy,
          "all": self.do_all, "update": self.do_update, "count": self.do_count}
        if args[0] not in classes:
            print("** class doesn't exist **")
        elif func[0] not in methods.keys():
            print("**command doesn't exist**")
        else:
            if "{" in args[1] and func[0] == "update":
                attributes = re.findall(r'\((.*?)\)', args[1])[0]
                model_id = attributes.split(',')[0]
                a_dict = eval(re.findall(r'\{.*?\}', attributes)[0])
                key = str(args[0] + "." + model_id).replace('"', '')
                if key not in models.storage.all().keys():
                    print("** no instance found **")
                else:
                    for k, v in a_dict.items():
                        new_line = f"{args[0]} {model_id} {k} {v}"
                        self.do_update(new_line)
            else:
                new_line = (args[0] + " " +
                        re.findall(r'\((.*?)\)', args[1])[0].replace(',', ''))
                method = methods[func[0]]
                method(new_line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
