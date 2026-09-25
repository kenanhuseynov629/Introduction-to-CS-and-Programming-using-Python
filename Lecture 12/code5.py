# verilmiş siyahıdakı uzunluğu tam olaraq 3-ə bərabər olan 
# sətirlərin ortadakı hərfini çıxarıb yeni siyahı təşkil etsin

L=['xyz', 'abc', 7, '4.0']
Lnew = [[x[1]] for x in L if type(x) == str and len(x) == 3]
print(Lnew)