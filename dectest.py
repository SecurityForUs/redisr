class Dec(object):
    def __init__(self, re):
        self.f = re
    
    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            print "instance.v =",instance.v
            return self.f(instance, *args, **kwargs)
        return wrapper

class T(object):
    v = ""
    
    def __init__(self):
        self.v = "inside __init__"
    
    @Dec
    def t(self):
        self.v = "inside t"
    
    @Dec
    def u(self):
        print "u"

t = T()
t.t()
t.u()