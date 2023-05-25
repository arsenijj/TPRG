from help import *


def zakalka(y, u, s, t, l, b, c):
    y ^= (y >> u)
    y ^= (y << s) & b
    y ^= (y << t) & c
    y ^= (y >> l)
    return y


def main(f_name_out, m_d, count, args):
    f = open(f_name_out, 'w')
    f.close()
    del_m = False
    try:
        if m_d != "No":
            del_m = True
            m_d = int(m_d)
        p, w, r, q, a, u, s, t, l, b, c = 624, 32, 31, 397, 2567483615, 11, 7, 15, 18, 2636928640, 4022730752
        n = int(args[0])
        x0 = [int(args[1])]
        lower_mask = (1 << r) - 1
        w1 = 0
        for i in range(w):
            w1 = set_bit(w1, i, 1)
        upper_mask = (~lower_mask * -1) & w1
        for i in range(1, p):
            x0.append((x0[i - 1] ^ (x0[i - 1] >> 30)) + i)
        check = p
        for i in range(count):
            if check >= p:
                for i in range(p):
                    x = (x0[i] & upper_mask) + (x0[(i + 1) % p] & lower_mask)
                    xA = x >> 1
                    if x & 1:
                        xA ^= a
                    x0[i] = x0[(i + q) % p] ^ xA
                check = 0
            y = x0[check]
            check += 1
            y = zakalka(y, u, s, t, l, b, c)
            rez = y % n
            if del_m:
                rez = d_m(rez, m_d)
            wri_fale(f_name_out, rez)
    except FileNotFoundError:
        print('Файл не найден\n')
        exit(0)
    except:
        print('Ошибка\n')
        exit(0)
