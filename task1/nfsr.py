from lfsr import lfsr
from help import *


def main1(f_name_out, m_d, c, args):
    f = open(f_name_out, 'w')
    f.close()
    del_m = False
    try:
        r1 = lfsr(c, [args[0], args[4]], m_d)
        r2 = lfsr(c, [args[1], args[5]], m_d)
        r3 = lfsr(c, [args[2], args[6]], m_d)
        w1 = 0
        for i in range(int(args[3])):
            w1 = set_bit(w1, i, 1)
        for i in range(c):
            a = r1[i]
            b = r2[i]
            c = r3[i]
            rez = (a ^ b + b ^ c + c) & w1
            if del_m:
                rez = d_m(rez, m_d)
            wri_fale(f_name_out, rez)
    except FileNotFoundError:
        print('Файл не найден\n')
        exit(0)
    except :
        print('Ошибка\n')
        exit(0)
