import time
print("Version is 0.8.3")
print("Proje ödevi uygulayıcısına hoş geldiniz.")
print("Uygulama sizden bir şey göndermesini istediğinde Enter tuşunu kullanın.")
print("")
ogrenci_sayisi = int(input("Sınıfta proje ödevi almış kaç öğrenci var? "))
mat = []
edebiyat = []
yd = []
cografya = []
tarih = []
din = []
fizik = []
beden = []
iyd = []
uyd = []
kimya = []
felsefe = []
Ek_1 = []
Ek_2 = []
Ek_3 = []
Ek_4 = []
idk = []

notlar = []
sinir = []
i = ogrenci_sayisi
print("Ders Numaraları:")
print("1 - Matematik")
print("2 - Türkçe")
print("3 - Yabancı Dil(İNG)")
print("4 - Fen Bilimleri")
print("5 - Sosyal Bilgiler")
print("6 - Bilişim veya Teknoloji Tasarım")
print("7 - Din Kültürü")
print("8 - Beden")
print("9 - 2. Yabancı Dil")
print("10 - 3. Yabancı Dil")
print("11 - Ek-1")
print("12 - Ek-2")
print("13 - Ek-3")
print("14 - Ek-4")
print("15 - Ek-5")
print("16 - Ek-6")
g = i+1
while i != 0:
    f = g - i
    a = int(input("{}. öğrencinin istediği ders numarası ".format(f)))
    if a == 1:
        mat.append(input("Öğrencinin ismi  "))
    if a == 2:
        edebiyat.append(input("Öğrencinin ismi  "))
    if a == 3:
        yd.append(input("Öğrencinin ismi  "))
    if a == 4:
        fizik.append(input("Öğrencinin ismi  "))
    if a == 5:
        cografya.append(input("Öğrencinin ismi  "))
    if a == 6:
        tarih.append(input("Öğrencinin ismi  "))
    if a == 7:
        din.append(input("Öğrencinin ismi  "))
    if a == 8:
        beden.append(input("Öğrencinin ismi  "))
    if a == 9:
        iyd.append(input("Öğrencinin ismi  "))
    if a == 10:
        uyd.append(input("Öğrencinin ismi  "))
    if a == 11:
        kimya.append(input("Öğrencinin ismi  "))
    if a == 12:
        felsefe.append(input("Öğrencinin ismi  "))
    if a == 13:
        Ek_1.append(input("Öğrencinin ismi  "))
    if a == 14:
        Ek_2.append(input("Öğrencinin ismi  "))
    if a == 15:
        Ek_3.append(input("Öğrencinin ismi  "))
    if a == 16:
        Ek_4.append(input("Öğrencinin ismi  "))
    print("")
    i = i-1

print("Yukarı aşağı için farenin topunu kullanabilirsiniz.")

print("")
print("")
print("")

print("Dersler için maksimum öğrenci sınırını girin (Eğer sınır yoksa 1000 gibi yüksek bir sayı girebilirsiniz)")

sinir.append(int(input("Matematik dersi için ")))
sinir.append(int(input("Türkçe dersi için ")))
sinir.append(int(input("Yabancı dil dersi için ")))
sinir.append(int(input("Fen Bilimleri dersi için ")))
sinir.append(int(input("Sosyal Bilgiler dersi için ")))
sinir.append(int(input("Bilişim veya Teknoloji Tasarım dersi için ")))
sinir.append(int(input("Din dersi için ")))
sinir.append(int(input("Beden dersi için ")))
sinir.append(int(input("2. Yabancı dil dersi için ")))
sinir.append(int(input("3. Yabancı dil dersi için ")))
sinir.append(int(input("Ek-1 ders için ")))
sinir.append(int(input("Ek-2 ders için ")))
sinir.append(int(input("Ek-3 ders için ")))
sinir.append(int(input("Ek-4 ders için ")))
sinir.append(int(input("Ek-5 ders için ")))
sinir.append(int(input("Ek-6 ders için ")))

dolu_dersler = []
bosaltilmasi_lazim = []

if len(mat) == sinir[0]:
    dolu_dersler.append("mat")
if len(mat) > sinir[0]:
    bosaltilmasi_lazim.append("mat")
if len(edebiyat) == sinir[1]:
    dolu_dersler.append("edebiyat")
if len(edebiyat) > sinir[1]:
    bosaltilmasi_lazim.append("edebiyat")
if len(yd) == sinir[2]:
    dolu_dersler.append("yd")
if len(yd) > sinir[2]:
    bosaltilmasi_lazim.append("yd")
if len(fizik) == sinir[3]:
    dolu_dersler.append("fizik")
if len(fizik) > sinir[3]:
    bosaltilmasi_lazim.append("fizik")
if len(cografya) == sinir[4]:
    dolu_dersler.append("cografya")
if len(cografya) > sinir[4]:
    bosaltilmasi_lazim.append("cografya")
if len(tarih) == sinir[5]:
    dolu_dersler.append("tarih")
if len(tarih) > sinir[5]:
    bosaltilmasi_lazim.append("tarih")
if len(din) == sinir[6]:
    dolu_dersler.append("din")
if len(din) > sinir[6]:
    bosaltilmasi_lazim.append("din")
if len(beden) == sinir[7]:
    dolu_dersler.append("beden")
if len(beden) > sinir[7]:
    bosaltilmasi_lazim.append("beden")
if len(iyd) == sinir[8]:
    dolu_dersler.append("iyd")
if len(iyd) > sinir[8]:
    bosaltilmasi_lazim.append("iyd")
if len(uyd) == sinir[9]:
    dolu_dersler.append("uyd")
if len(uyd) > sinir[9]:
    bosaltilmasi_lazim.append("uyd")
if len(kimya) == sinir[10]:
    dolu_dersler.append("kimya")
if len(kimya) > sinir[10]:
    bosaltilmasi_lazim.append("kimya")
if len(felsefe) == sinir[11]:
    dolu_dersler.append("felsefe")
if len(felsefe) > sinir[11]:
    bosaltilmasi_lazim.append("felsefe")
if len(Ek_1) == sinir[12]:
    dolu_dersler.append("Ek_1")
if len(Ek_1) > sinir[12]:
    bosaltilmasi_lazim.append("Ek_1")
if len(Ek_2) == sinir[13]:
    dolu_dersler.append("Ek_2")
if len(Ek_2) > sinir[13]:
    bosaltilmasi_lazim.append("Ek_2")
if len(Ek_3) == sinir[14]:
    dolu_dersler.append("Ek_3")
if len(Ek_3) > sinir[14]:
    bosaltilmasi_lazim.append("Ek_3")
if len(Ek_4) == sinir[15]:
    dolu_dersler.append("Ek_4")
if len(Ek_4) > sinir[15]:
    bosaltilmasi_lazim.append("Ek_4")

notlar.clear()

b = 0
x = 0
y = 0
z = 0

while len(bosaltilmasi_lazim) != 0:
    elema = bosaltilmasi_lazim[0]
    b = 0
    x = 0
    y = 0
    z = 0
    if elema == "mat":
        x = 0
        x = len(mat)
        while y != x:
            notlar.append(int(input("{} adlı öğrencinin matematik notu ".format(mat[y]))))
            y = y+1
        puan = 100
        b = 0
        c = 0
        z = sinir[0]
        print(notlar)
        while z != len(mat):
            c = 0
            while c != len(notlar):
                if notlar[c] >= puan:
                    idk.append(mat[c])
                    mat.pop(c)
                c = c+1
            puan = puan-1
        dolu_dersler.append("mat")
        bosaltilmasi_lazim.remove("mat")
    notlar.clear()
    if elema == "edebiyat":
        x = 0
        x = len(edebiyat)
        while y != x:
            notlar.append(int(input("{} adlı öğrencinin türkçe notu ".format(edebiyat[y]))))
            y = y+1
        puan = 100
        b = 0
        c = 0
        z = sinir[1]
        print(notlar)
        while z != len(edebiyat):
            c = 0
            while c != len(notlar):
                if notlar[c] >= puan:
                    idk.append(edebiyat[c])
                    edebiyat.pop(c)
                c = c+1
            puan = puan-1
        dolu_dersler.append("edebiyat")
        bosaltilmasi_lazim.remove("edebiyat")
    notlar.clear()
    if elema == "yd":
        x = 0
        x = len(yd)
        while y != x:
            notlar.append(int(input("{} adlı öğrencinin yabancı dil notu ".format(yd[y]))))
            y = y+1
        puan = 100
        b = 0
        c = 0
        z = sinir[2]
        print(notlar)
        while z != len(yd):
            c = 0
            while c != len(notlar):
                if notlar[c] >= puan:
                    idk.append(yd[c])
                    yd.pop(c)
                c = c+1
            puan = puan-1
        dolu_dersler.append("yd")
        bosaltilmasi_lazim.remove("yd")
    notlar.clear()
    if elema == "fizik":
        x = 0
        x = len(fizik)
        while y != x:
            notlar.append(int(input("{} adlı öğrencinin fen bilimleri notu ".format(fizik[y]))))
            y = y+1
        puan = 100
        b = 0
        c = 0
        z = sinir[3]
        print(notlar)
        while z != len(fizik):
            c = 0
            while c != len(notlar):
                if notlar[c] >= puan:
                    idk.append(fizik[c])
                    fizik.pop(c)
                c = c+1
            puan = puan-1
        dolu_dersler.append("fizik")
        bosaltilmasi_lazim.remove("fizik")
    notlar.clear()
    if elema == "cografya":
        x = 0
        x = len(cografya)
        while y != x:
            notlar.append(int(input("{} adlı öğrencinin sosyal bilgiler notu ".format(cografya[y]))))
            y = y+1
        puan = 100
        b = 0
        c = 0
        z = sinir[4]
        print(notlar)
        while z != len(cografya):
            c = 0
            while c != len(notlar):
                if notlar[c] >= puan:
                    idk.append(cografya[c])
                    cografya.pop(c)
                c = c+1
            puan = puan-1
        dolu_dersler.append("cografya")
        bosaltilmasi_lazim.remove("cografya")
    notlar.clear()
    if elema == "tarih":
        x = 0
        x = len(tarih)
        while y != x:
            notlar.append(int(input("{} adlı öğrencinin bilişim tenolojileri veya teknoloji tasarım(hangisine giriyorsa) notu ".format(tarih[y]))))
            y = y+1
        puan = 100
        b = 0
        c = 0
        z = sinir[5]
        print(notlar)
        while z != len(tarih):
            c = 0
            while c != len(notlar):
                if notlar[c] >= puan:
                    idk.append(tarih[c])
                    tarih.pop(c)
                c = c+1
            puan = puan-1
        dolu_dersler.append("tarih")
        bosaltilmasi_lazim.remove("tarih")
    notlar.clear()
    if elema == "din":
        x = 0
        x = len(din)
        while y != x:
            notlar.append(int(input("{} adlı öğrencinin din notu ".format(din[y]))))
            y = y+1
        puan = 100
        b = 0
        c = 0
        z = sinir[6]
        print(notlar)
        while z != len(din):
            c = 0
            while c != len(notlar):
                if notlar[c] >= puan:
                    idk.append(din[c])
                    din.pop(c)
                c = c+1
            puan = puan-1
        dolu_dersler.append("din")
        bosaltilmasi_lazim.remove("din")
    notlar.clear()
    if elema == "beden":
        x = 0
        x = len(beden)
        while y != x:
            notlar.append(int(input("{} adlı öğrencinin beden notu ".format(beden[y]))))
            y = y+1
        puan = 100
        b = 0
        c = 0
        z = sinir[7]
        print(notlar)
        while z != len(beden):
            c = 0
            while c != len(notlar):
                if notlar[c] >= puan:
                    idk.append(beden[c])
                    beden.pop(c)
                c = c+1
            puan = puan-1
        dolu_dersler.append("beden")
        bosaltilmasi_lazim.remove("beden")
    notlar.clear()
    if elema == "iyd":
        x = 0
        x = len(iyd)
        while y != x:
            notlar.append(int(input("{} adlı öğrencinin 2. Yabancı Dil notu ".format(iyd[y]))))
            y = y+1
        puan = 100
        b = 0
        c = 0
        z = sinir[8]
        print(notlar)
        while z != len(iyd):
            c = 0
            while c != len(notlar):
                if notlar[c] >= puan:
                    idk.append(iyd[c])
                    mat.pop(c)
                c = c+1
            puan = puan-1
        dolu_dersler.append("iyd")
        bosaltilmasi_lazim.remove("iyd")
    notlar.clear()
    if elema == "uyd":
        x = 0
        x = len(uyd)
        while y != x:
            notlar.append(int(input("{} adlı öğrencinin 3. Yabancı Dil notu ".format(uyd[y]))))
            y = y+1
        puan = 100
        b = 0
        c = 0
        z = sinir[9]
        print(notlar)
        while z != len(uyd):
            c = 0
            while c != len(notlar):
                if notlar[c] >= puan:
                    idk.append(uyd[c])
                    uyd.pop(c)
                c = c+1
            puan = puan-1
        dolu_dersler.append("uyd")
        bosaltilmasi_lazim.remove("uyd")
    notlar.clear()
    if elema == "kimya":
        x = 0
        x = len(kimya)
        while y != x:
            notlar.append(int(input("{} adlı öğrencinin Ek-1 notu ".format(kimya[y]))))
            y = y+1
        puan = 100
        b = 0
        c = 0
        z = sinir[10]
        print(notlar)
        while z != len(kimya):
            c = 0
            while c != len(notlar):
                if notlar[c] >= puan:
                    idk.append(kimya[c])
                    kimya.pop(c)
                c = c+1
            puan = puan-1
        dolu_dersler.append("kimya")
        bosaltilmasi_lazim.remove("kimya")
    notlar.clear()
    if elema == "felsefe":
        x = 0
        x = len(felsefe)
        while y != x:
            notlar.append(int(input("{} adlı öğrencinin Ek-2 notu ".format(felsefe[y]))))
            y = y+1
        puan = 100
        b = 0
        c = 0
        z = sinir[11]
        print(notlar)
        while z != len(felsefe):
            c = 0
            while c != len(notlar):
                if notlar[c] >= puan:
                    idk.append(felsefe[c])
                    felsefe.pop(c)
                c = c+1
            puan = puan-1
        dolu_dersler.append("felsefe")
        bosaltilmasi_lazim.remove("felsefe")
    notlar.clear()
    if elema == "Ek_1":
        x = 0
        x = len(Ek_1)
        while y != x:
            notlar.append(int(input("{} adlı öğrencinin Ek-3 notu ".format(Ek_1[y]))))
            y = y+1
        puan = 100
        b = 0
        c = 0
        z = sinir[12]
        print(notlar)
        while z != len(Ek_1):
            c = 0
            while c != len(notlar):
                if notlar[c] >= puan:
                    idk.append(Ek_1[c])
                    Ek_1.pop(c)
                c = c+1
            puan = puan-1
        dolu_dersler.append("Ek_1")
        bosaltilmasi_lazim.remove("Ek_1")
    notlar.clear()
    if elema == "Ek_2":
        x = 0
        x = len(Ek_2)
        while y != x:
            notlar.append(int(input("{} adlı öğrencinin Ek-4 notu ".format(Ek_2[y]))))
            y = y+1
        puan = 100
        b = 0
        c = 0
        z = sinir[13]
        print(notlar)
        while z != len(Ek_2):
            c = 0
            while c != len(notlar):
                if notlar[c] >= puan:
                    idk.append(Ek_2[c])
                    mat.pop(c)
                c = c+1
            puan = puan-1
        dolu_dersler.append("Ek_2")
        bosaltilmasi_lazim.remove("Ek_2")
    notlar.clear()
    if elema == "Ek_3":
        x = 0
        x = len(Ek_3)
        while y != x:
            notlar.append(int(input("{} adlı öğrencinin Ek-5 notu ".format(Ek_3[y]))))
            y = y + 1
        puan = 100
        b = 0
        c = 0
        z = sinir[14]
        print(notlar)
        while z != len(Ek_3):
            c = 0
            while c != len(notlar):
                if notlar[c] >= puan:
                    idk.append(Ek_3[c])
                    Ek_3.pop(c)
                c = c + 1
            puan = puan - 1
        dolu_dersler.append("Ek_3")
        bosaltilmasi_lazim.remove("Ek_3")
    notlar.clear()
    if elema == "Ek_4":
        x = 0
        x = len(Ek_4)
        while y != x:
            notlar.append(int(input("{} adlı öğrencinin Ek-6 notu ".format(Ek_4[y]))))
            y = y + 1
        puan = 100
        b = 0
        c = 0
        z = sinir[15]
        print(notlar)
        while z != len(Ek_4):
            c = 0
            while c != len(notlar):
                if notlar[c] >= puan:
                    idk.append(Ek_4[c])
                    Ek_4.pop(c)
                c = c + 1
            puan = puan - 1
        dolu_dersler.append("Ek_4")
        bosaltilmasi_lazim.remove("Ek_4")
    notlar.clear()

print("")
print("Yukarı aşağı için farenin topunu kullanabilirsiniz.")
print("")
print("Başarıyla ilk tercihler yerleştirildi.")
print("")
print("Yerleştirilemeyenler:")
print(idk)
print("")
mod = 0

if len(idk) > 0:
    print("Sistem iki çeşit yerleştirici moda sahiptir.")
    print("")
    print("1 - İlk modda sistem ilk tercihlerden yerleştirilmişlere ellemez.")
    print("Ve yerleştirilemeyenlerin diğer tercihlerini alırken dolu derslere yerleştirmez.")
    print("2- İlk modun aksine öğrencinin ikinci(veya daha sonraki) tercihi aldıktan sonra onu")
    print("ilk tercih yapmış insanların arasına alır ve tekrar not değerlendirmesi yapar.")
    print("En yüksek notu olan atılır(Eğer sınırdan fazla öğrenci varsa.   Ve evet yeniden soracak :)  )")
    mod = int(input("Hangi mod? "))
    if mod != 1 and mod != 2:
        print("Yerleştiriliemeyen öğrenci var. Lütfen olan bir mod girin!")
        print("")
        print("Sistem iki çeşit yerleştirici moda sahiptir.")
        print("1 - İlk modda sistem ilk tercihlerden yerleştirilmişlere ellemez.")
        print("Ve yerleştirilemeyenlerin diğer tercihlerini alırken dolu derslere yerleştirmez.")
        print("2- İlk modun aksine öğrencinin ikinci(veya daha sonraki) tercihi aldıktan sonra onu")
        print("ilk tercih yapmış insanların arasına alır ve tekrar not değerlendirmesi yapar.")
        print("En yüksek notu olan atılır(Eğer sınırdan fazla öğrenci varsa.)")
        mod = int(input("Hangi mod? "))
if mod == 1:
    print("")
    print("Ders Numaraları:")
    print("1 - Matematik")
    print("2 - Türkçe")
    print("3 - Yabancı Dil(İNG)")
    print("4 - Fen Bilimleri")
    print("5 - Sosyal Bilgiler")
    print("6 - Bilişim veya Teknoloji Tasarım")
    print("7 - Din Kültürü")
    print("8 - Beden")
    print("9 - 2. Yabancı Dil")
    print("10 - 3. Yabancı Dil")
    print("11 - Ek-1")
    print("12 - Ek-2")
    print("13 - Ek-3")
    print("14 - Ek-4")
    print("15 - Ek-5")
    print("16 - Ek-6")
    while len(idk) > 0:
        while True:
            if len(mat) == sinir[0]:
                dolu_dersler.append("mat")
            if len(mat) > sinir[0]:
                bosaltilmasi_lazim.append("mat")
            if len(edebiyat) == sinir[1]:
                dolu_dersler.append("edebiyat")
            if len(edebiyat) > sinir[1]:
                bosaltilmasi_lazim.append("edebiyat")
            if len(yd) == sinir[2]:
                dolu_dersler.append("yd")
            if len(yd) > sinir[2]:
                bosaltilmasi_lazim.append("yd")
            if len(fizik) == sinir[3]:
                dolu_dersler.append("fizik")
            if len(fizik) > sinir[3]:
                bosaltilmasi_lazim.append("fizik")
            if len(cografya) == sinir[4]:
                dolu_dersler.append("cografya")
            if len(cografya) > sinir[4]:
                bosaltilmasi_lazim.append("cografya")
            if len(tarih) == sinir[5]:
                dolu_dersler.append("tarih")
            if len(tarih) > sinir[5]:
                bosaltilmasi_lazim.append("tarih")
            if len(din) == sinir[6]:
                dolu_dersler.append("din")
            if len(din) > sinir[6]:
                bosaltilmasi_lazim.append("din")
            if len(beden) == sinir[7]:
                dolu_dersler.append("beden")
            if len(beden) > sinir[7]:
                bosaltilmasi_lazim.append("beden")
            if len(iyd) == sinir[8]:
                dolu_dersler.append("iyd")
            if len(iyd) > sinir[8]:
                bosaltilmasi_lazim.append("iyd")
            if len(uyd) == sinir[9]:
                dolu_dersler.append("uyd")
            if len(uyd) > sinir[9]:
                bosaltilmasi_lazim.append("uyd")
            if len(kimya) == sinir[10]:
                dolu_dersler.append("kimya")
            if len(kimya) > sinir[10]:
                bosaltilmasi_lazim.append("kimya")
            if len(felsefe) == sinir[11]:
                dolu_dersler.append("felsefe")
            if len(felsefe) > sinir[11]:
                bosaltilmasi_lazim.append("felsefe")
            if len(Ek_1) == sinir[12]:
                dolu_dersler.append("Ek_1")
            if len(Ek_1) > sinir[12]:
                bosaltilmasi_lazim.append("Ek_1")
            if len(Ek_2) == sinir[13]:
                dolu_dersler.append("Ek_2")
            if len(Ek_2) > sinir[13]:
                bosaltilmasi_lazim.append("Ek_2")
            if len(Ek_3) == sinir[14]:
                dolu_dersler.append("Ek_3")
            if len(Ek_3) > sinir[14]:
                bosaltilmasi_lazim.append("Ek_3")
            if len(Ek_4) == sinir[15]:
                dolu_dersler.append("Ek_4")
            if len(Ek_4) > sinir[15]:
                bosaltilmasi_lazim.append("Ek_4")
            d = int(input("{} adlı öğrencinin diğer tercihi ".format(idk[0])))
            if d == 1:
                if "mat" in dolu_dersler:
                    print("Matematik doludur.")
                    print("")
                    break
                else:
                    mat.append(idk[0])
                    idk.pop(0)
                    print("")
                    break
            if d == 2:
                if "edebiyat" in dolu_dersler:
                    print("Türkçe doludur.")
                    print("")
                    break
                else:
                    edebiyat.append(idk[0])
                    idk.pop(0)
                    print("")
                    break
            if d == 3:
                if "yd" in dolu_dersler:
                    print("Yabancı Dil doludur.")
                    print("")
                    break
                else:
                    yd.append(idk[0])
                    idk.pop(0)
                    print("")
                    break
            if d == 4:
                if "fizik" in dolu_dersler:
                    print("Fen Bilimleri doludur.")
                    print("")
                    break
                else:
                    fizik.append(idk[0])
                    idk.pop(0)
                    print("")
                    break
            if d == 5:
                if "cografya" in dolu_dersler:
                    print("Sosyal Bilgiler doludur.")
                    print("")
                    break
                else:
                    cografya.append(idk[0])
                    idk.pop(0)
                    print("")
                    break
            if d == 6:
                if "tarih" in dolu_dersler:
                    print("Bilişim Teknolojileri veya Teknoloji tasarım dersi doludur.")
                    print("")
                    break
                else:
                    tarih.append(idk[0])
                    idk.pop(0)
                    print("")
                    break
            if d == 7:
                if "din" in dolu_dersler:
                    print("Din doludur.")
                    print("")
                    break
                else:
                    din.append(idk[0])
                    idk.pop(0)
                    print("")
                    break
            if d == 8:
                if "beden" in dolu_dersler:
                    print("Beden doludur. (Burası nasıl bir okul?)")
                    print("")
                    break
                else:
                    beden.append(idk[0])
                    idk.pop(0)
                    print("")
                    break
            if d == 9:
                if "iyd" in dolu_dersler:
                    print("2. Yabancı dil doludur.")
                    print("")
                    break
                else:
                    iyd.append(idk[0])
                    idk.pop(0)
                    print("")
                    break
            if d == 10:
                if "uyd" in dolu_dersler:
                    print("3. Yabancı Dil doludur.")
                    print("")
                    break
                else:
                    uyd.append(idk[0])
                    idk.pop(0)
                    print("")
                    break
            if d == 11:
                if "kimya" in dolu_dersler:
                    print("Ek-1 doludur.")
                    print("")
                    break
                else:
                    kimya.append(idk[0])
                    idk.pop(0)
                    print("")
                    break
            if d == 12:
                if "felsefe" in dolu_dersler:
                    print("Ek-2 doludur.")
                    print("")
                    break
                else:
                    felsefe.append(idk[0])
                    idk.pop(0)
                    print("")
                    break
            if d == 13:
                if "Ek_1" in dolu_dersler:
                    print("Ek-3 doludur.")
                    print("")
                    break
                else:
                    Ek_1.append(idk[0])
                    idk.pop(0)
                    print("")
                    break
            if d == 14:
                if "Ek_2" in dolu_dersler:
                    print("Ek-4 doludur.")
                    print("")
                    break
                else:
                    Ek_2.append(idk[0])
                    idk.pop(0)
                    print("")
                    break
            if d == 15:
                if "Ek_3" in dolu_dersler:
                    print("Ek-5 doludur.")
                    print("")
                    break
                else:
                    Ek_3.append(idk[0])
                    idk.pop(0)
                    print("")
                    break
            if d == 16:
                if "Ek_4" in dolu_dersler:
                    print("Ek-6 doludur.")
                    print("")
                    break
                else:
                    Ek_4.append(idk[0])
                    idk.pop(0)
                    print("")
                    break
    print("Yazılım yerleştirme işlemini bitirdi!")
    print("")
    print("Matematik dersinden proje alanlar:")
    print(mat)
    print("")
    print("Türkçe dersinden proje alanlar:")
    print(edebiyat)
    print("")
    print("Yabancı Dil dersinden proje alanlar:")
    print(yd)
    print("")
    print("Fen Bilimleri dersinden proje alanlar:")
    print(fizik)
    print("")
    print("Sosyal Bilgiler dersinden proje alanlar:")
    print(cografya)
    print("")
    print("Bilişim dersinden proje alanlar:")
    print(tarih)
    print("")
    print("Din dersinden proje alanlar:")
    print(din)
    print("")
    print("Beden dersinden proje alanlar:")
    print(beden)
    print("")
    print("2. Yabancı Dil dersinden proje alanlar:")
    print(iyd)
    print("")
    print("3. Yabancı Dil dersinden proje alanlar:")
    print(uyd)
    print("")
    print("Ek-1 dersinden proje alanlar:")
    print(kimya)
    print("")
    print("Ek-2 dersinden proje alanlar:")
    print(felsefe)
    print("")
    print("Ek-3 dersinden proje alanlar:")
    print(Ek_1)
    print("")
    print("Ek-4 dersinden proje alanlar:")
    print(Ek_2)
    print("")
    print("Ek-5 dersinden proje alanlar:")
    print(Ek_3)
    print("")
    print("Ek-6 dersinden proje alanlar:")
    print(Ek_4)
    print("")
    print("Sonuçlar yukarıdadır.Yukarı aşağı için farenin topunu kullanabilirsiniz")

if mod == 2:
    while True:
        print("Ders Numaraları:")
        print("1 - Matematik")
        print("2 - Türkçe")
        print("3 - Yabancı Dil(İNG)")
        print("4 - Fen Bilimleri")
        print("5 - Sosyal Bilgiler")
        print("6 - Bilişim veya Teknoloji Tasarım")
        print("7 - Din Kültürü")
        print("8 - Beden")
        print("9 - 2. Yabancı Dil")
        print("10 - 3. Yabancı Dil")
        print("11 - Ek-1")
        print("12 - Ek-2")
        print("13 - Ek-3")
        print("14 - Ek-4")
        print("15 - Ek-5")
        print("16 - Ek-6")
        a = int(input("{} adlı öğrencinin istediği diğer dersin numarası ".format(idk[0])))
        if a == 1:
            mat.append(idk[0])
        if a == 2:
            edebiyat.append(idk[0])
        if a == 3:
            yd.append(idk[0])
        if a == 4:
            fizik.append(idk[0])
        if a == 5:
            cografya.append(idk[0])
        if a == 6:
            tarih.append(idk[0])
        if a == 7:
            din.append(idk[0])
        if a == 8:
            beden.append(idk[0])
        if a == 9:
            iyd.append(idk[0])
        if a == 10:
            uyd.append(idk[0])
        if a == 11:
            kimya.append(idk[0])
        if a == 12:
            felsefe.append(idk[0])
        if a == 13:
            Ek_1.append(idk[0])
        if a == 14:
            Ek_2.append(idk[0])
        if a == 15:
            Ek_3.append(idk[0])
        if a == 16:
            Ek_4.append(idk[0])
        print("")
        if len(mat) == sinir[0]:
            dolu_dersler.append("mat")
        if len(mat) > sinir[0]:
            bosaltilmasi_lazim.append("mat")
        if len(edebiyat) == sinir[1]:
            dolu_dersler.append("edebiyat")
        if len(edebiyat) > sinir[1]:
            bosaltilmasi_lazim.append("edebiyat")
        if len(yd) == sinir[2]:
            dolu_dersler.append("yd")
        if len(yd) > sinir[2]:
            bosaltilmasi_lazim.append("yd")
        if len(fizik) == sinir[3]:
            dolu_dersler.append("fizik")
        if len(fizik) > sinir[3]:
            bosaltilmasi_lazim.append("fizik")
        if len(cografya) == sinir[4]:
            dolu_dersler.append("cografya")
        if len(cografya) > sinir[4]:
            bosaltilmasi_lazim.append("cografya")
        if len(tarih) == sinir[5]:
            dolu_dersler.append("tarih")
        if len(tarih) > sinir[5]:
            bosaltilmasi_lazim.append("tarih")
        if len(din) == sinir[6]:
            dolu_dersler.append("din")
        if len(din) > sinir[6]:
            bosaltilmasi_lazim.append("din")
        if len(beden) == sinir[7]:
            dolu_dersler.append("beden")
        if len(beden) > sinir[7]:
            bosaltilmasi_lazim.append("beden")
        if len(iyd) == sinir[8]:
            dolu_dersler.append("iyd")
        if len(iyd) > sinir[8]:
            bosaltilmasi_lazim.append("iyd")
        if len(uyd) == sinir[9]:
            dolu_dersler.append("uyd")
        if len(uyd) > sinir[9]:
            bosaltilmasi_lazim.append("uyd")
        if len(kimya) == sinir[10]:
            dolu_dersler.append("kimya")
        if len(kimya) > sinir[10]:
            bosaltilmasi_lazim.append("kimya")
        if len(felsefe) == sinir[11]:
            dolu_dersler.append("felsefe")
        if len(felsefe) > sinir[11]:
            bosaltilmasi_lazim.append("felsefe")
        if len(Ek_1) == sinir[12]:
            dolu_dersler.append("Ek_1")
        if len(Ek_1) > sinir[12]:
            bosaltilmasi_lazim.append("Ek_1")
        if len(Ek_2) == sinir[13]:
            dolu_dersler.append("Ek_2")
        if len(Ek_2) > sinir[13]:
            bosaltilmasi_lazim.append("Ek_2")
        if len(Ek_3) == sinir[14]:
            dolu_dersler.append("Ek_3")
        if len(Ek_3) > sinir[14]:
            bosaltilmasi_lazim.append("Ek_3")
        if len(Ek_4) == sinir[15]:
            dolu_dersler.append("Ek_4")
        if len(Ek_4) > sinir[15]:
            bosaltilmasi_lazim.append("Ek_4")
        idk.pop(0)
        while len(bosaltilmasi_lazim) != 0:
            elema = bosaltilmasi_lazim[0]
            b = 0
            x = 0
            y = 0
            z = 0
            if elema == "mat":
                x = 0
                x = len(mat)
                while y != x:
                    notlar.append(int(input("{} adlı öğrencinin matematik notu ".format(mat[y]))))
                    y = y + 1
                puan = 100
                b = 0
                c = 0
                z = sinir[0]
                print(notlar)
                while z != len(mat):
                    c = 0
                    while c != len(notlar):
                        if notlar[c] >= puan:
                            idk.append(mat[c])
                            mat.pop(c)
                        c = c + 1
                    puan = puan - 1
                dolu_dersler.append("mat")
                bosaltilmasi_lazim.remove("mat")
            notlar.clear()
            if elema == "edebiyat":
                x = 0
                x = len(edebiyat)
                while y != x:
                    notlar.append(int(input("{} adlı öğrencinin türkçe notu ".format(edebiyat[y]))))
                    y = y + 1
                puan = 100
                b = 0
                c = 0
                z = sinir[1]
                print(notlar)
                while z != len(edebiyat):
                    c = 0
                    while c != len(notlar):
                        if notlar[c] >= puan:
                            idk.append(edebiyat[c])
                            edebiyat.pop(c)
                        c = c + 1
                    puan = puan - 1
                dolu_dersler.append("edebiyat")
                bosaltilmasi_lazim.remove("edebiyat")
            notlar.clear()
            if elema == "yd":
                x = 0
                x = len(yd)
                while y != x:
                    notlar.append(int(input("{} adlı öğrencinin yabancı dil notu ".format(yd[y]))))
                    y = y + 1
                puan = 100
                b = 0
                c = 0
                z = sinir[2]
                print(notlar)
                while z != len(yd):
                    c = 0
                    while c != len(notlar):
                        if notlar[c] >= puan:
                            idk.append(yd[c])
                            yd.pop(c)
                        c = c + 1
                    puan = puan - 1
                dolu_dersler.append("yd")
                bosaltilmasi_lazim.remove("yd")
            notlar.clear()
            if elema == "fizik":
                x = 0
                x = len(fizik)
                while y != x:
                    notlar.append(int(input("{} adlı öğrencinin fen bilimleri notu ".format(fizik[y]))))
                    y = y + 1
                puan = 100
                b = 0
                c = 0
                z = sinir[3]
                print(notlar)
                while z != len(fizik):
                    c = 0
                    while c != len(notlar):
                        if notlar[c] >= puan:
                            idk.append(fizik[c])
                            fizik.pop(c)
                        c = c + 1
                    puan = puan - 1
                dolu_dersler.append("fizik")
                bosaltilmasi_lazim.remove("fizik")
            notlar.clear()
            if elema == "cografya":
                x = 0
                x = len(cografya)
                while y != x:
                    notlar.append(int(input("{} adlı öğrencinin sosyal bilgiler notu ".format(cografya[y]))))
                    y = y + 1
                puan = 100
                b = 0
                c = 0
                z = sinir[4]
                print(notlar)
                while z != len(cografya):
                    c = 0
                    while c != len(notlar):
                        if notlar[c] >= puan:
                            idk.append(cografya[c])
                            cografya.pop(c)
                        c = c + 1
                    puan = puan - 1
                dolu_dersler.append("cografya")
                bosaltilmasi_lazim.remove("cografya")
            notlar.clear()
            if elema == "tarih":
                x = 0
                x = len(tarih)
                while y != x:
                    notlar.append(int(input("{} adlı öğrencinin bilişim tenolojileri veya teknoloji tasarım(hangisine giriyorsa) notu ".format(tarih[y]))))
                    y = y + 1
                puan = 100
                b = 0
                c = 0
                z = sinir[5]
                print(notlar)
                while z != len(tarih):
                    c = 0
                    while c != len(notlar):
                        if notlar[c] >= puan:
                            idk.append(tarih[c])
                            tarih.pop(c)
                        c = c + 1
                    puan = puan - 1
                dolu_dersler.append("tarih")
                bosaltilmasi_lazim.remove("tarih")
            notlar.clear()
            if elema == "din":
                x = 0
                x = len(din)
                while y != x:
                    notlar.append(int(input("{} adlı öğrencinin din notu ".format(din[y]))))
                    y = y + 1
                puan = 100
                b = 0
                c = 0
                z = sinir[6]
                print(notlar)
                while z != len(din):
                    c = 0
                    while c != len(notlar):
                        if notlar[c] >= puan:
                            idk.append(din[c])
                            din.pop(c)
                        c = c + 1
                    puan = puan - 1
                dolu_dersler.append("din")
                bosaltilmasi_lazim.remove("din")
            notlar.clear()
            if elema == "beden":
                x = 0
                x = len(beden)
                while y != x:
                    notlar.append(int(input("{} adlı öğrencinin beden notu ".format(beden[y]))))
                    y = y + 1
                puan = 100
                b = 0
                c = 0
                z = sinir[7]
                print(notlar)
                while z != len(beden):
                    c = 0
                    while c != len(notlar):
                        if notlar[c] >= puan:
                            idk.append(beden[c])
                            beden.pop(c)
                        c = c + 1
                    puan = puan - 1
                dolu_dersler.append("beden")
                bosaltilmasi_lazim.remove("beden")
            notlar.clear()
            if elema == "iyd":
                x = 0
                x = len(iyd)
                while y != x:
                    notlar.append(int(input("{} adlı öğrencinin 2. Yabancı Dil notu ".format(iyd[y]))))
                    y = y + 1
                puan = 100
                b = 0
                c = 0
                z = sinir[8]
                print(notlar)
                while z != len(iyd):
                    c = 0
                    while c != len(notlar):
                        if notlar[c] >= puan:
                            idk.append(iyd[c])
                            mat.pop(c)
                        c = c + 1
                    puan = puan - 1
                dolu_dersler.append("iyd")
                bosaltilmasi_lazim.remove("iyd")
            notlar.clear()
            if elema == "uyd":
                x = 0
                x = len(uyd)
                while y != x:
                    notlar.append(int(input("{} adlı öğrencinin 3. Yabancı Dil notu ".format(uyd[y]))))
                    y = y + 1
                puan = 100
                b = 0
                c = 0
                z = sinir[9]
                print(notlar)
                while z != len(uyd):
                    c = 0
                    while c != len(notlar):
                        if notlar[c] >= puan:
                            idk.append(uyd[c])
                            uyd.pop(c)
                        c = c + 1
                    puan = puan - 1
                dolu_dersler.append("uyd")
                bosaltilmasi_lazim.remove("uyd")
            notlar.clear()
            if elema == "kimya":
                x = 0
                x = len(kimya)
                while y != x:
                    notlar.append(int(input("{} adlı öğrencinin Ek-1 notu ".format(kimya[y]))))
                    y = y + 1
                puan = 100
                b = 0
                c = 0
                z = sinir[10]
                print(notlar)
                while z != len(kimya):
                    c = 0
                    while c != len(notlar):
                        if notlar[c] >= puan:
                            idk.append(kimya[c])
                            kimya.pop(c)
                        c = c + 1
                    puan = puan - 1
                dolu_dersler.append("kimya")
                bosaltilmasi_lazim.remove("kimya")
            notlar.clear()
            if elema == "felsefe":
                x = 0
                x = len(felsefe)
                while y != x:
                    notlar.append(int(input("{} adlı öğrencinin Ek-2 notu ".format(felsefe[y]))))
                    y = y + 1
                puan = 100
                b = 0
                c = 0
                z = sinir[11]
                print(notlar)
                while z != len(felsefe):
                    c = 0
                    while c != len(notlar):
                        if notlar[c] >= puan:
                            idk.append(felsefe[c])
                            felsefe.pop(c)
                        c = c + 1
                    puan = puan - 1
                dolu_dersler.append("felsefe")
                bosaltilmasi_lazim.remove("felsefe")
            notlar.clear()
            if elema == "Ek_1":
                x = 0
                x = len(Ek_1)
                while y != x:
                    notlar.append(int(input("{} adlı öğrencinin Ek-3 notu ".format(Ek_1[y]))))
                    y = y + 1
                puan = 100
                b = 0
                c = 0
                z = sinir[12]
                print(notlar)
                while z != len(Ek_1):
                    c = 0
                    while c != len(notlar):
                        if notlar[c] >= puan:
                            idk.append(Ek_1[c])
                            Ek_1.pop(c)
                        c = c + 1
                    puan = puan - 1
                dolu_dersler.append("Ek_1")
                bosaltilmasi_lazim.remove("Ek_1")
            notlar.clear()
            if elema == "Ek_2":
                x = 0
                x = len(Ek_2)
                while y != x:
                    notlar.append(int(input("{} adlı öğrencinin Ek-4 notu ".format(Ek_2[y]))))
                    y = y + 1
                puan = 100
                b = 0
                c = 0
                z = sinir[13]
                print(notlar)
                while z != len(Ek_2):
                    c = 0
                    while c != len(notlar):
                        if notlar[c] >= puan:
                            idk.append(Ek_2[c])
                            mat.pop(c)
                        c = c + 1
                    puan = puan - 1
                dolu_dersler.append("Ek_2")
                bosaltilmasi_lazim.remove("Ek_2")
            notlar.clear()
            if elema == "Ek_3":
                x = 0
                x = len(Ek_3)
                while y != x:
                    notlar.append(int(input("{} adlı öğrencinin Ek-5 notu ".format(Ek_3[y]))))
                    y = y + 1
                puan = 100
                b = 0
                c = 0
                z = sinir[14]
                print(notlar)
                while z != len(Ek_3):
                    c = 0
                    while c != len(notlar):
                        if notlar[c] >= puan:
                            idk.append(Ek_3[c])
                            Ek_3.pop(c)
                        c = c + 1
                    puan = puan - 1
                dolu_dersler.append("Ek_3")
                bosaltilmasi_lazim.remove("Ek_3")
            notlar.clear()
            if elema == "Ek_4":
                x = 0
                x = len(Ek_4)
                while y != x:
                    notlar.append(int(input("{} adlı öğrencinin Ek-6 notu ".format(Ek_4[y]))))
                    y = y + 1
                puan = 100
                b = 0
                c = 0
                z = sinir[15]
                print(notlar)
                while z != len(Ek_4):
                    c = 0
                    while c != len(notlar):
                        if notlar[c] >= puan:
                            idk.append(Ek_4[c])
                            Ek_4.pop(c)
                        c = c + 1
                    puan = puan - 1
                dolu_dersler.append("Ek_4")
                bosaltilmasi_lazim.remove("Ek_4")
            notlar.clear()
        if len(idk) == 0:
            break
    print("Yazılım yerleştirme işlemini bitirdi!")
    print("")
    print("Matematik dersinden proje alanlar:")
    print(mat)
    print("")
    print("Türkçe dersinden proje alanlar:")
    print(edebiyat)
    print("")
    print("Yabancı Dil dersinden proje alanlar:")
    print(yd)
    print("")
    print("Fen Bilimleri dersinden proje alanlar:")
    print(fizik)
    print("")
    print("Sosyal Bilgiler dersinden proje alanlar:")
    print(cografya)
    print("")
    print("Bilişim dersinden proje alanlar:")
    print(tarih)
    print("")
    print("Din dersinden proje alanlar:")
    print(din)
    print("")
    print("Beden dersinden proje alanlar:")
    print(beden)
    print("")
    print("2. Yabancı Dil dersinden proje alanlar:")
    print(iyd)
    print("")
    print("3. Yabancı Dil dersinden proje alanlar:")
    print(uyd)
    print("")
    print("Ek-1 dersinden proje alanlar:")
    print(kimya)
    print("")
    print("Ek-2 dersinden proje alanlar:")
    print(felsefe)
    print("")
    print("Ek-3 dersinden proje alanlar:")
    print(Ek_1)
    print("")
    print("Ek-4 dersinden proje alanlar:")
    print(Ek_2)
    print("")
    print("Ek-5 dersinden proje alanlar:")
    print(Ek_3)
    print("")
    print("Ek-6 dersinden proje alanlar:")
    print(Ek_4)
    print("")
    print("Sonuçlar yukarıdadır.Yukarı aşağı için farenin topunu kullanabilirsiniz")

time.sleep(10000)
a = input("Sistem bir tuşa basınca kapanacak!")
