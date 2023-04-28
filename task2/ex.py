import math, help


def ex(x, a, b, m):
    rez = a - b * math.log(x / m)
    return rez


def main (f_name_in, f_name_out, args):
    try:
        f_in = help.op_file(f_name_in)
        m, a, b = help.get_arg(args)
        f = open(f_name_out, 'w')
        for i in range(0, len(f_in)):
            f.write(str(round(ex(f_in[i], a, b, m), 3)) + " ")
        f.close()
    except FileNotFoundError:
        print('Файл не найден\n')
        exit(0)
    except :
        print('Ошибка\n')
        exit(0)
