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


def main(f_name_out,m_d,n,args):
    f = open(f_name_out, 'w')
    f.close()
    del_m = False
    try:
        cout = 1
        if m_d != "No":
            del_m = True
            m_d = int(m_d)
        p, a, x, s = list(map(int, args))
        if a < 0 or x < 0 or p < 0 or s < 0:
            stdout.write('Ошибка\n')
            exit(0)
        a = bin(a)[:1:-1]
        j = []
        for i in range(len(a)):
            if a[i] == '1':
                j.append(i + 1)
        x = list(map(int, list(bin(x)[2:])))
        count = p - len(x)
        for _ in range(count):
            x.insert(0, 0)
        for i in range(p + (n + 1) * s + s):
            x_tmp = 0
            for k in range(len(j)):
                x_tmp += x[i + j[k] - 1]
            x.append(x_tmp % 2)
        for t in range(n):
            tmp = ""
            for s_i in range(s):
                tmp += str(x[p + t * s + s_i])
            rez = int(tmp, 2)
            if del_m:
                rez = d_m(rez, m_d)
            monitor(cout, n)
            wri_fale(f_name_out, rez)
            cout +=1
    except FileNotFoundError:
        stdout.write('Файл не найден\n')
        exit(0)
    except:
        stdout.write('Ошибка\n')
        exit(0)
