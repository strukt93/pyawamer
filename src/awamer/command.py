import os

class Command():
    def __init__(self, name, target=""):
        self.name = name
        self.args = {}
        self.target = target
        self.out = ""
    
    def add_arg(self, switch, value=""):
        self.args[switch] = value
    
    def run(self):
        cmd = self.name
        args = " ".join(" ".join([key, value]) for key, value in self.args.items())
        if self.target:
            cmd += " " + self.target
        if args:
            cmd += " " + args
        self.out = os.popen(cmd).read().strip()
        return self