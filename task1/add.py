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
            stdout.write('Ошибка\n')
            exit(0)
        l = len(args)
        for i in range(0, int(l / 2)):
            a_s.append(args[i])
        for i in range(int(l / 2), l):
            x_s.append(args[i])
        if c < 0 or m < 0:
            stdout.write('Ошибка\n')
            exit(0)
        cout = 1
        n = int(n)
        for q in range(n):
            rez = 0
            for w in range(len(a_s)):
                rez += a_s[w]  * x_s[q + w]
            rez = (rez + c) % m
            if del_m:
                rez = d_m(rez, m_d)
            monitor (cout, n)
            wri_fale (f_name_out, rez)
            cout += 1
            x_s.append(rez)
    except FileNotFoundError:
        stdout.write('Файл не найден\n')
        exit(0)
    except:
        stdout.write('Ошибка\n')
        exit(0)
