from help import *


def main(f_name_out,m_d,c,args):
    f = open(f_name_out, 'w')
    f.close()
    del_m = False
    try:
        if m_d != "No":
            del_m = True
            m_d = int(m_d)
        n, e, x, w = list(map(int, args))
        if n < 0 or e < 0 or w < 0 or x < 0 or x >= n:
            print('Ошибка\n')
            exit(0)
        for i in range(c):
            z = 0
            for i in range(w):
                x = x ** e % n
                z = set_bit(z, w - i - 1, x & 1)
            if del_m:
                rez = d_m(z, m_d)
            wri_fale(f_name_out, rez)
    except FileNotFoundError:
        print('Файл не найден\n')
        exit(0)
    except:
        print('Ошибка\n')
        exit(0)
