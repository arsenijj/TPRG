from sys import stdout, stderr


def wri_fale (file_name,mass):
    fale = open (file_name,"a")
    fale.write (str(mass)+ "\n")
    fale.close()


def monitor (i,n):
    stderr.write('Генерация ' + str(i) + '/' + str(n) + '\n')


def d_m (i,m_d):
    tmp = i % m_d
    return  tmp


def main(f_name_out,m_d,c,args):
    f = open(f_name_out, 'w')
    f.close()
    init = args
    del_m = False
    try:
        cout = 1
        if m_d != "No":
            del_m = True
            m_d = int(m_d)
        k = int(init[0])
        w = int(init[1])
        if k < 0:
            stdout.write('Ошибка\n')
            exit(0)
        p = []
        x = []
        m = []
        j = []
        j2 = []
        f = 2
        for i in range(k):
            p.append(int(init[f]))
            t = bin(init[f + 1])[:1:-1]
            j.append([z+1 for z in range(len(t)) if t[z] == '1'])
            x.append(int(init[f + 2]))
            m.append(len(j[i]))
            f += 3
        q = 0
        for i in range(3 * k + 2, len(init)):
            q += 1
            t = bin(init[i])[2:]
            t = "0" * (k - len(t)) + t
            t = t[::-1]
            j2.append(t)
        rslos_arr = []
        for i in range(k):
            x_bin = bin(x[i])[2:]
            x_bin = '0' * (p[i] - len(x_bin) + 1) + x_bin
            x_res = x_bin
            for r in range(int(c * w / p[i] + 1)):
                for s in range(p[i]):
                    x_new = 0
                    for t in range(m[i]):
                        temp = r * p[i] + s + j[i][t]
                        x_new += int(x_res[temp])
                        x_new %= 2
                    x_res += str(x_new)
            rslos_arr.append(x_res[len(x_bin):])
        for o in range(c):
            res = ''
            for s in range(w):
                x_new = 0
                bits = list(map(lambda b: b[w * o + s], rslos_arr))
                for r in range(q):
                    bit_tmp = []
                    for t in range(len(bits)):
                        if j2[r][t] == '0':
                            bit_tmp.append('1')
                        else:
                            bit_tmp.append(bits[t])
                    q_tmp = int(bit_tmp[0])
                    for u in range(1, len(bit_tmp)):
                        q_tmp &= int(bit_tmp[u])
                    x_new ^= q_tmp
                res += str(x_new)
            rez1 = int(res, 2)
            if del_m:
                rez = d_m(rez1, m_d)
            monitor(cout, c)
            wri_fale(f_name_out, rez1)
            cout += 1
    except FileNotFoundError:
        stdout.write('Файл не найден\n')
        exit(0)
    except :
        stdout.write('Ошибка\n')
        exit(0)

