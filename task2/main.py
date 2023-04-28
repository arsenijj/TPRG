import re
from sys import stdout, argv
import st, tr, ex, nr, ln, ls, bi, gm
mass_code = ["st", "tr", "ex", "nr", "ln", "ls","bi","gm"]


def helps():
    print("""
    1.	st – стандартное равномерное с заданным интервалом;
    2.	tr – треугольное распределение;
    3.	ex – общее экспоненциальное распределение;
    4.	nr – нормальное распределение;
    5.	gm – гамма распределение;
    6.	ln – логнормальное распределение;
    7.	ls – логистическое распределение;
    8.	bi – биномиальное распределение.
    
    /m:<число> – модуль; 
    /p:<параметр1> – 1-й параметр, необходимый для генерации ПСЧ заданного распределения;
    /q:<параметр2> – 2-й параметр, необходимый для генерации ПСЧ заданного распределения;
    /w:<параметр3> – 3-й параметр, необходимый для генерации ПСЧ заданного распределения (для гамма распределения);
    """)


def prov_code(mass):
    mass_code = ["st", "tr", "ex", "nr","gm", "ln", "ls",'bi']
    code = mass[0]
    code = code[3:]
    try:
        if mass_code.index(code) != -1:
            return code
    except ValueError:
        print("Ошибка, введите нужный код распределения")


def file_name(strok):
    file = strok
    file= file[3:]
    return  file


def file_resurs(mass):
    file_in = ""
    file_out = ""
    rez = []
    if mass[0].find("/f:") != -1:
        file_in = file_name(mass[0])
    else:
        if mass[0].find("/o:") != -1:
            file_out = file_name(mass[0])
    if mass[1].find("/o:") != -1:
        file_out = file_name(mass[1])
    rez.append(file_in)
    rez.append(file_out)
    if (file_in != "" ) and (file_out != "" ):
        rez.append(2)
    else:
        if ((file_in == "" ) and (file_out != "" )) or ((file_in != "") and (file_out == "")):
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
    if b[i].startswith('/d:') == 1:
        a.append(b[i])
        cnt += 1
for i in range(0, len(b), 1):
    if b[i].startswith('/f:') == 1:
        a.append(b[i])
        cnt += 1
for i in range(0, len(b), 1):
    if b[i].startswith('/o:') == 1:
        a.append(b[i])
        cnt += 1
for i in range(0, len(b), 1):
    if b[i].startswith('/m:') == 1:
        a.append(b[i])
        cnt += 1
for i in range(0, len(b), 1):
    if b[i].startswith('/p:') == 1:
        a.append(b[i])
        cnt += 1
for i in range(0, len(b), 1):
    if b[i].startswith('/q:') == 1:
        a.append(b[i])
        cnt += 1
for i in range(0, len(b), 1):
    if b[i].startswith('/w:') == 1:
        a.append(b[i])
        cnt += 1

try:
    args = []
    consol_in = False
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
    file_in, file_out, count_udal = f_res
    for i in range (int(count_udal)):
        del a[0]
    for i in a:
        args_t = "".join(re.findall(r'[-]?\d+[.]?[\d+]*',i))
        args.append(args_t)
    if file_in == "":
        print("Не указан входной файл")
        exit(0)
    if file_out == "":
        file_out = "rnd.dat"
    if code == "st":
        if len(args) != 3:
            stdout.write('Ошибка2\n')
            exit(0)  
        st.main(file_in,file_out,args)
    if code == "tr":
        if len(args) != 3:
            stdout.write('Ошибка3\n')
            exit(0)  
        tr.main(file_in,file_out,args)
    if code == "ex":
        if len(args) != 3:
            stdout.write('Ошибка4\n')
            exit(0)  
        ex.main(file_in,file_out,args)
    if code == "nr":
        if len(args) != 3:
            stdout.write('Ошибка5\n')
            exit(0)  
        nr.main(file_in,file_out,args)
    if code == "ln":
        if len(args) != 3:
            stdout.write('Ошибка6\n')
            exit(0)  
        ln.main(file_in,file_out,args)
    if code == "ls":
        if len(args) != 3:
            stdout.write('Ошибка7\n')
            exit(0)  
        ls.main(file_in,file_out,args)
    if code == "bi":
        if len(args) != 3:
            stdout.write('Ошибка8\n')
            exit(0)  
        bi.main(file_in,file_out,args)
    if code == "gm":
        if len(args) != 4:
            stdout.write('Ошибка9\n')
            exit(0)
        gm.main(file_in,file_out,args)
except FileNotFoundError:
    stdout.write('Файл не найден\n')
    exit(0)

