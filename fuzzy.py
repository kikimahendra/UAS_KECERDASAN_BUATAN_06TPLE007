print ('UAS Kecerdasan Buatan - 06TPLE007')
print ('KIKI MAHENDRA - 191011400091')
print ('')

x_temp = input ('Masukkan nilai Temperatur (F) = ')
y_cuaca = input ('Masukkan nilai Cuaca (%) = ')
print ('')

temp = int(x_temp)
cuaca = int(y_cuaca)

#Proses Fuzifikasi Temperatur
if temp <= 35 :
    value_sgtdingin = 1
    value_dingin = 0
    value_hangat = 0
    value_panas = 0

if temp > 35 and temp < 55 :
    value_sgtdingin = (55 - temp)/(55 - 35)
    value_dingin = (temp - 35)/(55 - 35)
    value_hangat = 0
    value_panas = 0

if temp == 55 :
    value_sgtdingin = 0
    value_dingin = 1
    value_hangat = 0
    value_panas = 0

if temp > 55 and temp < 75 :
    value_sgtdingin = 0
    value_dingin = (75 - temp)/(75 - 55)
    value_hangat = (temp - 55)/(75 - 55)
    value_panas = 0

if temp == 75 :
    value_sgtdingin = 0
    value_dingin = 0
    value_hangat = 1
    value_panas = 0

if temp > 75 and temp < 95 :
    value_sgtdingin = 0
    value_dingin = 0
    value_hangat = (95 - temp)/(95 - 75)
    value_panas = (temp - 75)/(95 - 75)

if temp == 95 :
    value_sgtdingin = 0
    value_dingin = 0
    value_hangat = 0
    value_panas = 1

print ('Maka Temperatur dalam variabel linguistik, derajat keanggotaan adalah :')
print ('Sangat Dingin =', value_sgtdingin)
print ('Dingin =', value_dingin)
print ('Hangat =', value_hangat)
print ('Panas =', value_panas)
print ('')

#Proses Fuzifikasi Cuaca
if cuaca <= 30 :
    value_cerah = 1
    value_berawan = 0
    value_mendung = 0

if cuaca > 30 and cuaca < 50 :
    value_cerah = (50 - cuaca)/(50 - 30)
    value_mendung = 0

if cuaca > 30 and cuaca < 60 :
    value_berawan = (cuaca - 30)/(60 - 30)

if cuaca == 60 :
    value_cerah = 0
    value_berawan = 1
    value_mendung = 0

if cuaca > 60 and cuaca < 90 :
    value_cerah = 0
    value_berawan = (90 - cuaca)/(90 - 60)

if cuaca > 70 and cuaca < 90 :
    value_cerah = 0
    value_mendung = (cuaca - 70)/(90 - 70)

if cuaca >= 90 :
    value_cerah = 0
    value_berawan = 0
    value_mendung = 1

print ('Maka Cuaca dalam variabel linguistik, derajat keanggotaan adalah :')
print ('Cerah =', value_cerah)
print ('Berawan =', value_berawan)
print ('Mendung =', value_mendung)
print ('')

#Proses Inferensi
kecepatan = []
def pelan (variable_temp, variable_cuaca) :
    if variable_temp != 0 :
        if variable_cuaca != 0 :
            output = min(variable_temp, variable_cuaca)
            kecepatan.append([output, 35])

def cepat (variable_temp, variable_cuaca) :
    if variable_temp != 0 :
        if variable_cuaca != 0 :
            output = min(variable_temp, variable_cuaca)
            kecepatan.append([output, 85])

pelan(value_sgtdingin, value_cerah)
pelan(value_sgtdingin, value_berawan)
pelan(value_sgtdingin, value_mendung)
pelan(value_dingin, value_cerah)
pelan(value_dingin, value_berawan)
pelan(value_dingin, value_mendung)
cepat(value_hangat, value_cerah)
cepat(value_hangat, value_berawan)
cepat(value_hangat, value_mendung)
cepat(value_panas, value_cerah)
cepat(value_panas, value_berawan)
cepat(value_panas, value_mendung)

print ('Maka kecepatannya adalah', kecepatan)
print ('')

#Proses Defuzifikasi
perkalian_n = 0
pembagian_n = 0

for j in range (0, len(kecepatan)) :
    perkalian = kecepatan[j][0] * kecepatan[j][1]
    pembagian = kecepatan[j][0]
    perkalian_n = perkalian_n + perkalian
    pembagian_n = pembagian_n + pembagian
z = perkalian_n / pembagian_n

print ('Kecepatan kendaaran tersebut adalah', z , 'km/jam')
print ('')