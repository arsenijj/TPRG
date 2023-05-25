from help import *


def main(f_name_out,m_d,n,args):
    f = open(f_name_out, 'w')
    f.close()
    del_m = False
    try:
        if m_d != "No":
            del_m = True
            m_d = int(m_d)
        c = int(args[0])
        m = int(args[1])
        a_s = []
        x_s = []
        del args[0]
        del args[0]
        if (len(args) % 2) != 0:
            print('Ошибка\n')
            exit(0)
        l = len(args)
        for i in range(0, int(l / 2)):
            a_s.append(int(args[i]))
        for i in range(int(l / 2), l):
            x_s.append(int(args[i]))
        if c < 0 or m < 0:
            print('Ошибка\n')
            exit(0)
        cout = 1
        n = int(n)
        for q in range(n):
            rez = 0
            for w in range(len(a_s)):
                rez += a_s[w] * x_s[q + w]
            rez = (rez + c) % m
            if del_m:
                rez = d_m(rez, m_d)
            wri_fale (f_name_out, rez)
            cout += 1
            x_s.append(rez)
    except FileNotFoundError:
        print('Файл не найден\n')
        exit(0)
    except:
        print('Ошибка\n')
        exit(0)
