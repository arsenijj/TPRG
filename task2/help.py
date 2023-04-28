def op_file(file_name):
    fale = open(file_name,"r")
    rez = fale.read().split()
    for x in rez:
        if x.find(".") != -1:
            print("Не верные входные значения")
            exit(0)
    fale.close()
    return[int(elem) for elem in rez]


def get_arg(args):
    m = int(args[0])
    if args[1].find(".") != -1:
        a = float(args[1])
    else:
        a = int(args[1])
    if args[2].find(".") != -1:
        b = float(args[2])
    else:
        b = int(args[2])
    return m, a, b


def get_arg_gm(args):
    fl_c = False
    m = int(args[0])
    if args[1].find(".") != -1:
        a = float(args[1])
    else:
        a = int(args[1])
    if args[2].find(".") != -1:
        b = float(args[2])
    else:
        b = int(args[2])
    if args[3].find(".") != -1:
        if args[3][-1] != '5':
            print("Ошибка в параметре w")
            exit(0)
        c = float(args[3])
        if c < 0:
            print("Ошибка в параметре w")
            exit(0)
    else:
        c = int(args[3])
        if c <= 0:
            print("Ошибка в параметре w")
            exit(0)
        fl_c = True
    return m, a, b, c, fl_c
