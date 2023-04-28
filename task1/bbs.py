from help import *


def main(f_name_out,m_d,c,args):
    f = open(f_name_out, 'w')
    f.close()
    del_m = False
    try:
        cout = 1
        if m_d != "No":
            del_m = True
            m_d = int(m_d)
        n, x, l = list(map(int, args))
        if n < 0 or l < 0 or x < 0 or x >= n:
            print('Ошибка\n')
            exit(0)
        for i in range(c):
            s = ""
            for j in range(l):
                x = pow(x, 2, n)
                x_bin = bin(x)
                s += x_bin[-1]
            rez = int(s,2)
            if del_m:
                rez = d_m(rez, m_d)
            wri_fale(f_name_out, rez)
            cout +=1
    except FileNotFoundError:
        print('Файл не найден\n')
        exit(0)
    except:
        print('Ошибка\n')
        exit(0)
