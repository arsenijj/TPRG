from help import *


def main(f_name_out,m_d,c,args):
    f = open(f_name_out, 'w')
    f.close()
    del_m = False
    try:
        if m_d != "No":
            del_m = True
            m_d = int(m_d)
        x = int(args[0])
        n = 16637
        for i in range(c):
            rez = (x ** 2) % n
            x = rez
            if del_m:
                rez = d_m(rez, m_d)
            wri_fale(f_name_out, rez)
    except FileNotFoundError:
        print('Файл не найден\n')
        exit(0)
    except:
        print('Ошибка\n')
        exit(0)
