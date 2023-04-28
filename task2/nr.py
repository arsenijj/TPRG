import math, help


def nr(x1, x2, a, b, m):
    rez = []
    y1 = a + b * math.sqrt(math.fabs(-2 * math.log(1 - (x1 / m)))) * math.cos(2*math.pi*(x2 / m))
    y2 = a + b * math.sqrt(math.fabs(-2 * math.log(1 - (x1 / m)))) * math.sin(2*math.pi*(x2 / m))
    rez.append(y1)
    rez.append(y2)
    return rez


def main (f_name_in, f_name_out, args):
    try:
        f_in = help.op_file(f_name_in)
        m, a, b = help.get_arg(args)
        f = open(f_name_out, 'w')
        i = 0
        while i < len(f_in) - 1:
            rez = nr(f_in[i], f_in[i + 1], a, b, m)
            f.write(str(round(rez[0], 3)) + " " + str(round(rez[1], 3)) + " ")
            i = i + 2
        f.close()
    except FileNotFoundError:
        print('Файл не найден\n')
        exit(0)
    except:
        print('Ошибка\n')
        exit(0)
