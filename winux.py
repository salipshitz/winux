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
                continue
            elif sep == None:
                sep = '\''
                continue
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
        if ch == ' ':
            if sep == None:
                i, j, tmp, cmd, opt_args, args = done_split(i, j, tmp, cmd, opt_args, args, optnl)
                optnl = False
                continue
        tmp += ch
        j += 1
    i, j, tmp, cmd, opt_args, args = done_split(i, j, tmp, cmd, opt_args, args, optnl)
    return (cmd, args, opt_args)

class function:
    def __init__(self, alwd_args, alwd_optl_args, args, optl_args):
        if len(args) != alwd_args and alwd_args != -1:
            raise ValueError(f"{self.__class__.__name__} only accepts {alwd_args} arguments")

class echo(function):
    def __init__(self, args, optl_args):
        super(echo, self).__init__(-1, [], args, optl_args)
        print(" ".join(args))

cmds = {"echo": echo}

while True:
    cmd, args, optl_args = split_args(input("$ "))
    cmds[cmd](args, optl_args)
