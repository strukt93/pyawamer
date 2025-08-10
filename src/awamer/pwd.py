from . import command

class Pwd(command.Command):
    def __init__(self):
        super().__init__("pwd")