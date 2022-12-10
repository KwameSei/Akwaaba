#!/usr/bin/env python3

import cmd


class AkwaabaCommand(cmd.Cmd):

    prompt = "Akwaaba> "

    classes = []

    def do_EOF(self, line):
        """Command to exit from the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Parses the previous command entered"""
        pass

if __name__ == "__main__":
    AkwaabaCommand().cmdloop()