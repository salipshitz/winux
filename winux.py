import os

def split_args(ui):
    i = 0
    j = 0
    sep = None
    optnl = False
    cmd = ""
    args = []
    opt_args = []
    tmp
    def done_split:
        j = 0
        if i == 0:
            cmd = tmp
        elif optnl:
            opt_args += tmp
        else:
            args.append(tmp)
        i += 1
        tmp = ""
    for ch in ui:
        if ch == '\'':
            if sep == '\'':
                sep = None
                done_split()
                continue
            elif sep == None:
                sep = '\''
                continue
        if ch == '"':
            if sep == '"':
                sep = None
                done_split()
                continue
            elif sep == None:
                sep = '"'
                continue
        if ch == '-' and j == 0:
            optnl = True
            continue
        if ch == ' ':
            if sep == None:
                done_split()
                continue
        tmp += sep

while True:
    cmd, args, optl_args = split_args(input("$ "))
