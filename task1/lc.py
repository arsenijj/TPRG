from help import *


def main(f_name_out,m_d,n,args):
    f = open(f_name_out, 'w')
    f.close()
    del_m = False
    try:
        if m_d != "No":
            del_m = True
            m_d = int(m_d)
        a,c,m,x0 = list(map(int, args))
        if a < 0 or c < 0 or m < 0 or x0 < 0:
            print('Ошибка: входные числа не удовлетворяют условиям\n')
            exit(0)
        cout = 1
        xi = x0
        n = int(n)
        for i in range(n):
            xi = (a * xi + c) % m
            rez = xi
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

