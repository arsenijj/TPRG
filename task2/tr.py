import help


def tr(x1, x2, a, b, m):
    rez = a + b * ((x1 / m) + (x2 / m) - 1)
    return rez


def main (f_name_in, f_name_out, args):
    try:
        f_in = help.op_file(f_name_in)
        m, a, b = help.get_arg(args)
        f = open(f_name_out, 'w')
        i = 0
        while i < len(f_in) - 1:
            f.write(str(round(tr(f_in[i], f_in[i + 1], a, b, m), 3)) + " ")
            i = i + 2
        f.close()
    except FileNotFoundError:
        print('Файл не найден\n')
        exit(0)
    except:
        print('Ошибка\n')
        exit(0)
