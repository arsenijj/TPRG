import math, help, nr


def gamma(x, a, b, c, fl_c, m):
    if fl_c:
        umn = 1
        for key in x:
            umn = umn * (1 - (key / m))
        y = a - b * math.log(math.fabs(umn))
        return str(round(y, 3))
    else:
        k = int(c - 0.5)
        umn = 1
        z1, z2 = nr.nr(x[0], x[1], 0, 1, m)
        for key in range(2, k + 2):
            umn = umn * (1 - (x[key] / m))
        y1 = a + b * ( ((z1 ** 2) / 2)  - math.log(umn))
        umn = 1
        for key in range(k + 2, len(x)):
            umn = umn * (1 - (x[key] / m))
        y2 = a + b * (((z2 ** 2) / 2)  - math.log(umn))
        return str(round(y1, 3)) + " " + str(round(y2, 3))


def func_chunks_generators(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def main (f_name_in, f_name_out, args):
    try:
        f_in = help.op_file(f_name_in)
        m, a, b, c, fl_c = help.get_arg_gm(args)
        f = open(f_name_out, 'w')
        if fl_c:
            mass = list(func_chunks_generators(f_in, c))
            for i in range(0, len(mass)):
                f.write(gamma(mass[i], a, b, c, fl_c, m) + " ")
        else:
            k = int(c - 0.5)
            mass = list(func_chunks_generators(f_in, 2 * k + 2))
            for i in range(0, len(mass)):
                f.write(gamma(mass[i], a, b, c, fl_c, m) + " ")
        f.close()

    except FileNotFoundError:
        print('Файл не найден\n')
        exit(0)
    except:
        print('Ошибка\n')
        exit(0)
