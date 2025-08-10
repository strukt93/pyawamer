from . import command

class Uname(command.Command):
    def __init__(self):
        super().__init__("uname")
    
    def m(self):
        self.add_arg('-m')
        return self
    
    def a(self):
        self.add_arg('-a')
        return self
    
    def v(self):
        self.add_arg('-v')
        return self
    
    def r(self):
        self.add_arg('-r')
        return self
    
    def s(self):
        self.add_arg('-s')
        return self
    
    def n(self):
        self.add_arg('-n')
        return self
    
    def p(self):
        self.add_arg('-p')
        return self
