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
        w = args[0]
        del args[0]
        k = [int(args[i]) for i in range(len(args))]
        s = list(range(256))
        j = 0
        for i in range(256):
            j = (j + s[i] + k[i]) % 256
            s[i], s[j] = s[j], s[i]
        j = 0
        i = 0
        y = ""
        n = c
        while n > 0:
            i = (i + 1) % 256
            j = (j + s[i]) % 256
            s[i], s[j] = s[j], s[i]
            x = s[(s[i] + s[j]) % 256]
            x_bin = bin(x)[2:]
            if len(x_bin) < 8:
                 x_bin = "0" * (8 - len(x_bin)) + x_bin
            y += x_bin[-8:]
            while len(y) >= w and n > 0:
                rez = int(y[:w], 2)
                if del_m:
                    rez = d_m(rez, m_d)
                wri_fale(f_name_out, rez)
                y = y[w:]
                n -= 1
                cout += 1
    except FileNotFoundError:
        print('Файл не найден\n')
        exit(0)
    except:
        print('Ошибка\n')
        exit(0)
        
