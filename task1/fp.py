from help import *


def main(f_name_out,m_d,n,args):
    f = open(f_name_out, 'w')
    f.close()
    del_m = False
    try:
        cout = 1
        if m_d != "No":
            del_m = True
            m_d = int(m_d)
        p, q1, q2, q3, w, y = list(map(int, args))
        if q1 < 0 or q2 < 0 or q3 < 0 or p < q1 or p < q2 or p < q3 or q1 == q2 or q2 == q3 or q1 == q3:
            print('Ошибка\n')
            exit(0)
        x = list(map(int, list(bin(y)[2:])))
        count = p - len(x)
        for j in range(count):
            x.insert(0, 0)
        for i in range(p + (n + 1) * w + w):
            x_tmp = x[i + q1] + x[i + q2] + x[i + q3] + x[i]
            x.append(x_tmp % 2)
        for t in range(n):
            tmp = ""
            for w_i in range(w):
                tmp += str(x[p + t * w + w_i])
            rez = int(tmp, 2)
            if del_m:
                rez = d_m(rez, m_d)
            wri_fale(f_name_out, rez)
            cout +=1
    except FileNotFoundError:
        print('Файл не найден\n')
        exit(0)
    except:
        print('Ошибка\n')
        exit(0)
