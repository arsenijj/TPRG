from sys import stdout, argv
import lc,add,lfsr,fp,rsa,bbs,rc4,nfsr,mt
mass_code = ["lc","add", "lfsr", "5p", "rsa","bbs", "rc4", "nfsr","mt"]


def helps():
    print("""
    1.	lc – линейный конгруэнтный метод (/i: a c m x[0] – целые неотрицательные числа; m > 0)
    2.	add – аддитивный метод (/i: c m a[1] a[2] ... a[s] x[1] ... x[s] – целые неотрицательные числа, меньше m; m > 0);
    3.	5p – пятипараметрический метод (/i: p q1 q2 q3 w x0 – целые неотрицательные числа; w – разрядность выходного числа; 
            p > q1, q2, q3 > 0; q1, q2, q3 – попарно различны;  x0 – p-битное число);
    4.	lfsr – регистр сдвига с обратной связью (РСЛОС) (/i: p a x[0] l; a, x0 – p-битные неотрицательные числа, 
            a и x0 интерпретируются как двоичный вектор);
    5.	nfsr – нелинейная комбинация РСЛОС (/i: n l p[1] a[1] x0[1] p[2] a[2] x0[2] ... p[n] a[n] x0[n] c[1] ... c[m]; 
            n – количество генераторов, n > 0; l – количество бит в сгенерированном значении; 
            p[i], a[i], x0[i] – параметры соответствующего РСЛОС; c[i] – n-битные числа);
    6.	mt – вихрь Мерсенна (/i: p w r q a u s t l b c. w – размерность слова; r – позиция разделения, r <= w; 
            p, q – два положительных числа, 0 < q <= p; a, b, c – w-разрядные неотрицательные числа, 0 <= a, b, c < 2w; 
            u, s, t, l – коэффициенты, 0 <= u, s, t, l <= w);
    7.	rc4 – RC4 (/i: w K0 … K255, где w – длина в битах, на которую разбиваются блоки; 
            K0 … K255 – некоторая перестановка чисел от 0 до 255);
    8.	rsa – ГПСЧ на основе RSA (/i: n e x0 w l - положительные целые числа; w > 0, x0 < n; 
            w – количество генерируемых бит за шаг, l – разрядность выходного числа);
    9.	bbs – алгоритм Блюма-Блюма-Шуба (/i: n x0 l – положительные целые числа; x0 < n; l – разрядность выходного числа);
""")


def prov_code(mass):
    mass_code = ["lc","add", "lfsr", "5p", "rsa","bbs", "rc4", "nfsr","mt"]
    code = mass[0]
    code = code[3:]
    try:
        if mass_code.index(code) != -1:
            return code
    except ValueError:
        print("Ошибка, введите нужный код генератора")


def file_name(strok):
    file = strok
    file= file[3:]
    return  file


def pare_args(mass):
    try:
        rez = []
        for key in mass:
            tmp = str(key)
            rez.append(tmp)
        return rez
    except:
        stdout.write('Ошибка со входными параметрами\n')
        exit(0)


def file_resurs(mass):
    m = ""
    file_out = ""
    rez = []
    if mass[0].find("/m:") != -1:
        m = file_name(mass[0])
    else:
        if mass[0].find("/f:") != -1:
            file_out = file_name(mass[0])
    if mass[1].find("/f:") != -1:
        file_out = file_name(mass[1])
    rez.append(m)
    rez.append(file_out)
    if (m != "" ) and (file_out != "" ):
        rez.append(2)
    else:
        if ((m == "" ) and (file_out != "" )) or ((m != "") and (file_out == "")):
            rez.append(1)
        else:
            rez.append(0)
    return rez


b = argv
a = []
a.append(b[0])
cnt = 0
for i in range(0, len(b), 1):
    if b[i].startswith('/h') == 1:
        a.append(b[i])
for i in range(0, len(b), 1):
    if b[i].startswith('/g:') == 1:
        a.append(b[i])
        cnt += 1
for i in range(0, len(b), 1):
    if b[i].startswith('/m:') == 1:
        a.append(b[i])
        cnt += 1
for i in range(0, len(b), 1):
    if b[i].startswith('/f:') == 1:
        a.append(b[i])
        cnt += 1
for i in range(0, len(b), 1):
    if b[i].startswith('/n:') == 1:
        a.append(b[i])
        cnt += 1
for i in range(0, len(b), 1):
    if b[i].startswith('/i:') == 1:
        a.append(b[i])
        cnt += 1
        for j in range (1, len(b) - cnt, 1):
            a.append(b[i + j])
try:
    args = []
    consol_out = False
    file_name_in = ""
    del a[0]
    if a[0] == '/h':
        helps()
        exit(0)
    code = prov_code(a)
    if code != "":
        del a[0]
    if len(a) >= 2:
        f_res = file_resurs(a)
    else:
        f_res = ["","",0]
    m, file_out, count_udal = f_res
    for i in range (int(count_udal)):
        del a[0]
    if a[0].find("/n:") != -1:
        n = int(file_name(a[0]))
        del a[0]
    else:
        n = str(10000)
    if a[0] != "/i:":
        stdout.write('Ошибка\n')
        exit(0)
    del a[0]
    new_a = pare_args(a)
    if m == "":
        m = "No"
    if file_out == "":
        file_out = "rnd.dat"
    if code == "lc":
        lc.main(file_out,m,n,new_a)
    if code == "add":
        add.main(file_out,m,n,new_a)
    if code == "lfsr":
        lfsr.main(file_out,m,n,new_a)
    if code == "5p":
        fp.main(file_out,m,n,new_a)
    if code == "rsa":
        rsa.main(file_out,m,n,new_a)
    if code == "bbs":
        bbs.main(file_out,m,n,new_a)
    if code == "rc4":
        rc4.main(file_out,m,n,new_a)
    if code == "nfsr":
        nfsr.main1(file_out,m,n,new_a)
    if code == "mt":
        mt.main(file_out,m,n,new_a)
except FileNotFoundError:
    stdout.write('Файл не найден\n')
    exit(0)
