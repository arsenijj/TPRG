def wri_fale (file_name,mass):
    fale = open (file_name,"a")
    fale.write (str(mass)+ " ")
    fale.close()


def d_m (i,m_d):
    tmp = i % m_d
    return  tmp