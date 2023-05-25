from help import *


def lfsr(n, args, m_d):
    ans = []
    l = len(args[0])
    x = int(args[0], 2)
    a = int(args[1], 2)
    for _ in range(n):
        cur_bit = 0
        for i in range(l):
            cur_bit ^= ((x & (1 << i)) >> i) * ((a & (1 << i)) >> i)
        a = shift(a, l)
        rez = set_bit(a, 0, cur_bit)
        if m_d != "No":
            m_d = int(m_d)
            rez = d_m(rez, m_d)
        ans.append(rez)
    return ans


def main(f_name_out, m_d, n, args):
    f = open(f_name_out, 'w')
    f.close()
    try:
        ans = lfsr(n, args, m_d)
        for i in range(len(ans)):
            wri_fale(f_name_out, ans[i])
    except FileNotFoundError:
        print('Файл не найден\n')
        exit(0)
    except:
        print('Ошибка\n')
        exit(0)
