import os

def split_args(ui):
    i = 0
    j = 0
    sep = None
    optnl = False
    cmd = ""
    args = []
    opt_args = []
    tmp = ""
    def done_split(i, j, tmp, cmd, opt_args, args, optnl):
        j = 0
        if i == 0:
            cmd = tmp
        elif optnl:
            opt_args += tmp
        else:
            args.append(tmp)
        i += 1
        tmp = ""
        return (i, j, tmp, cmd, opt_args, args)
    for ch in ui:
        if ch == '\'':
            if sep == '\'':
                sep = None
                i, j, tmp, cmd, opt_args, args = done_split(i, j, tmp, cmd, opt_args, args, optnl)
                optnl = False
            elif sep == None:
                sep = '\''
        if ch == '"':
            if sep == '"':
                sep = None
                i, j, tmp, cmd, opt_args, args = done_split(i, j, tmp, cmd, opt_args, args, optnl)
                optnl = False
                continue
            elif sep == None:
                sep = '"'
                continue
        if ch == '-' and j == 0:
            optnl = True
            continue
        if ch == '~' and j == 0:
            tmp += "C:"
            continue
        if ch == ' ':
            if sep == None:
                i, j, tmp, cmd, opt_args, args = done_split(i, j, tmp, cmd, opt_args, args, optnl)
                optnl = False
                continue
        tmp += ch
        j += 1
    i, j, tmp, cmd, opt_args, args = done_split(i, j, tmp, cmd, opt_args, args, optnl)
    return (cmd, args, opt_args)
    
class command:
    def require_args(self, alwd_args, args):
        if (len(args) != alwd_args):
            raise ValueError(f" {self.__class__.__name__} only accepts {alwd_args} arguments")
    def require_args_range(self, min_args, max_args, args):
      if (not min_args < len(args) < max_args):
            raise ValueError(f" {self.__class__.__name__} only accepts {alwd_args} arguments")


class echo(command):
    def __init__(self, args, optl_args):
        print(" ".join(args))

class cd(command):
    def __init__(self, args, optl_args):
        self.require_args(1, args)
        os.chdir(args[0])

class ls(command):
    def __init__(self, args, optl_args):
        self.require_range(0, 1, args)
        os.system("dir"+"".join([" /a"]*int("a" in optl_args)))

class clear(command):
    def __init__(self, args, optl_args):
        self.require_args(0, args)
        os.system("cls")

class touch(command):
    def __init__(self, args, optl_args):
        self.require_args_range(1, 100, args)
        for arg in args:
            os.system(f"type nul > {arg}")

class mkdir(command):
    def __init__(self, args, optl_args):
        self.require_args(1, args)
        os.system("md "+args[0])
        
class pwd(command):
    def __init__(self, args, optl_args):
        self.require_args(0, args)
        print(os.getcwd())

class cp(command):
    def __init__(self, args, optl_args):
        self.require_args(2, args)
        os.system("copy "+" ".join(args))

class mv(command):
    def __init__(self, args, optl_args):
        self.require_args(2, args)
        os.system("move "+" ".join(args))

class rm(command):
    def __init__(self, args, optl_args):
        self.require_args(1, args)
        os.system("del "+args[0])

class rmdir(command):
    def __init__(self, args, optl_args):
        self.require_args(1, args)
        os.system("rmdir "+args[0])

cmds = {"echo": echo, "cd": cd, "ls": ls, "clear": clear, "pwd": pwd, "cp": cp, "mv": mv, "rm": rm, "rmdir": rmdir}

while True:
    cmd, args, optl_args = split_args(input("$ "))
    cmds[cmd](args, optl_args)
