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
        n, e, x, w, l = list(map(int, args))
        if n < 0 or e < 0 or w < 0 or l < 0 or x < 0 or x >= n:
            print('Ошибка\n')
            exit(0)
        s = ""
        count = 0
        while count != c:
            x = pow(x, e, n)
            a = bin(x)[2:]
            if len(a) < w:
                a = "0" * (w - len(a)) + a
            s += a[-w:]
            while len(s) >= l:
                 rez = int(str(s[:l]),2)
                 if del_m:
                     rez = d_m(rez, m_d)
                 wri_fale(f_name_out, rez)
                 s = s[l:]
                 count +=1
                 cout +=1
    except FileNotFoundError:
        print('Файл не найден\n')
        exit(0)
    except:
        print('Ошибка\n')
        exit(0)
