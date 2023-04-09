from sys import stdout, stderr


def wri_fale (file_name,mass):
    fale = open (file_name,"a")
    fale.write(str(mass)+ "\n")
    fale.close()


def monitor (i,n1):
    stderr.write('Генерация ' + str(i) + '/' + str(n1) + '\n')


def d_m (i,m_d):
    tmp = i % m_d
    return  tmp


def zakalka(x, u, s, t, l,  b, c, w):
    y = (x ^ (x >> u) % (2 ** w))
    y ^= ((y << s) & b)
    y ^= ((y << t) & c)
    z = (y ^ (y >> l) % (2 ** w))
    return z


def stick(a, b, r, w):
    a_bin = bin(a)[2:]
    b_bin = bin(b)[2:]
    if len(a_bin) < w:
        a_bin = "0" * (w - len(a_bin)) + a_bin
    if len(b_bin) < w:
        b_bin = "0" * (w - len(b_bin)) + b_bin
    return int(a_bin[:-r] + b_bin[-r:], 2)


def main(f_name_out,m_d,n,args):
    f = open(f_name_out, 'w')
    f.close()
    del_m = False
    try:
        cout = 1
        if m_d != "No":
            del_m = True
            m_d = int(m_d)
        p, w, r, q, a, u, s, t, l, b, c = [int(args[i]) for i in range(11)]
        x = [int(args[i]) for i in range(11, len(args))]
        if q <= 0 or p < q or r < 0 or u < 0 or s < 0 or t < 0 or l < 0 or w < r or w < u or w < s or w < t or w < l:
            stdout.write('Ошибка\n')
            exit(0)
        for i in range(n):
            temp = stick(x[i], x[i + 1], r, w)
            x.append((x[i + q] ^ (temp >> 1) ^ (a * (temp % 2))) % (2 ** w))
            ans = zakalka(x[i + p], u, s, t, l, b, c, w)
            rez = ans
            if del_m:
                rez = d_m(rez, m_d)
            monitor(cout, n)
            wri_fale(f_name_out, rez)
            cout += 1
    except FileNotFoundError:
        stdout.write('Файл не найден\n')
        exit(0)
    except:
        stdout.write('Ошибка\n')
        exit(0)

    
