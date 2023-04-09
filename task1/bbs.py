from sys import stdout, stderr


def wri_fale (file_name,mass):
    fale = open (file_name,"a")
    fale.write (str(mass)+ "\n")
    fale.close()


def monitor (i,n1):
    stderr.write('Генерация ' + str(i) + '/' + str(n1) + '\n')


def d_m (i,m_d):
    tmp = i % m_d
    return  tmp


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
            stdout.write('Ошибка\n')
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
            monitor(cout, c)
            wri_fale(f_name_out, rez)
            cout +=1
    except FileNotFoundError:
        stdout.write('Файл не найден\n')
        exit(0)
    except:
        stdout.write('Ошибка\n')
        exit(0)
