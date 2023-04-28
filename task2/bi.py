import math, help


def binominal(x,a,b,m):
    u = x / m
    s = 0
    y = 0
    for k in range(b):
        c_b = math.factorial(b)/(math.factorial(k) * math.factorial(b - k))
        s += c_b * (a ** k) * ((1 - a ) ** (b - k))
        if s > u:
            y = k
            break
        y = b
        k += 1
    return y


def main (f_name_in, f_name_out, args):
    try:
        f_in = help.op_file(f_name_in)
        m, a, b = help.get_arg(args)
        f = open(f_name_out, 'w')
        for i in range(0, len(f_in)):
            f.write(str(binominal(f_in[i], a, b, m)) + " ")
        f.close()
    except FileNotFoundError:
        print('Файл не найден\n')
        exit(0)
    except :
        print('Ошибка\n')
        exit(0)
