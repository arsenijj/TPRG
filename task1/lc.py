from sys import stdout, stderr


def wri_fale (file_name,mass):
    fale = open(file_name, "a")
    fale.write(str(mass) + "\n")
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
        if m_d != "No":
            del_m = True
            m_d = int(m_d)
        a,c,m,x0 = list(map(int, args))
        if a < 0 or c < 0 or m < 0 or x0 < 0:
            stdout.write('Ошибка: входные числа не удовлетворяют условиям\n')
            exit(0)
        cout = 1
        xi = x0
        n = int(n)
        for i in range(n):
            xi = (a * xi + c) % m
            rez = xi
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

