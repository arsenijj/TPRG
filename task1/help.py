def wri_fale (file_name,mass):
    fale = open (file_name,"a")
    fale.write (str(mass)+ " ")
    fale.close()

def d_m (i,m_d):
    tmp = i % m_d
    return  tmp

def set_bit(num, num_bit, bit):
    mask = 1 << num_bit
    num &= ~mask
    if bit:
        return num | mask
    else:
        return num

def shift(num, s):
    new_num = 0
    bit = 0
    for i in range(s):
        new_num = set_bit(new_num, i, bit)
        bit = (num & ( 1 << i )) >> i
    new_num = set_bit(new_num, 0, bit)
    return new_num