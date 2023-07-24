
# Ana Liste
H = []

# Hasta Ekleme
def ekle():#numara, hasta_adı, cinsiyet, yaş, hasta_durumu, WBC, RBC, HGB, HCT
    # Maksimum değer kontrolü
    if len(H) !=25:
        # Hasta Numarası Döngüsü
        while True:
            try:
                # Hasta Numarası Girişi
                numara = int(input("Hasta No: "))
                ## Hasta Numarası Kontrolü
                # if 4000 <= numara <= 10000:
                #     # Hata Açıklaması
                #     print("Sadece 1-25 arasında değer girebilirsiniz.")  
                #     continue
                break
            # Değer Hatası
            except ValueError:
                # Hata Açıklaması
                print("Sadece 1-25 arasında sayısal değer girebilirsiniz.")  
                continue
        # Hasta Adı Girişi
        hasta_adı = str(input("Adı Soyadı: "))
        # Hasta Cinsiyeti Döngüsü
        while True:
            # Hasta Cinsiyeti Girişi
            cinsiyet = input("Cinsiyeti (E/K): ")
            # Giriş Değer Kontrolü
            if cinsiyet.lower() == "e" or cinsiyet.lower() == "k":
                # Girişi Binarye Çevirme
                if cinsiyet.lower() == "e":
                    cinsiyet = True
                else:
                    cinsiyet = False
                break
            else:
                # Giriş Değer Hatası
                print("Sadece E ve K değerlerini girebilirsiniz (E = Erkek, K = Kadın)")  
                continue
        # Hasta Yaşı Döngüsü
        while True:
            try:
                # Hasta Yaşı Girişi
                yaş = int(input("Yaşı: "))
                ## Hasta Yaşı Kontrolü
                # if 0 <= yaş <= 100:
                #     # Hata Açıklaması
                #     print("Sadece 0-100 arasında değer girebilirsiniz.")  
                #     continue
                break
            # Değer Hatası
            except ValueError:
                # Hata Açıklaması
                print("Sadece sayısal değer girebilirsiniz.")  
                continue
        # Hasta Durumu Döngüsü
        while True:
            try:
                # Hasta Durumu Girişi
                hasta_durumu = int(input("Hasta durumu(1-10 arası): "))
                # Hasta Durumu Kontrolü
                if hasta_durumu > 10 or hasta_durumu < 1:
                    # Hata Açıklaması
                    print("Sadece 1-10 arasında değer girebilirsiniz.")  
                    continue
                break
            # Değer Hatası
            except ValueError:
                # Hata Açıklaması
                print("Sadece 1-10 arasında sayısal değer girebilirsiniz.")  
                continue
        # WBC Döngüsü
        while True:
            try:
                # WBC Girişi
                WBC = int(input("WBC: "))
                ## WBC Kontrolü
                # if kucuk <= WBC <= buyuk:
                #     print("Sadece kucuk-buyuk arasında değer girebilirsiniz.")  
                #     continue
                break
            # Değer Hatası
            except ValueError:
                # Hata Açıklaması
                print("Sadece sayısal değer girebilirsiniz.")  
                continue
        # RBC Döngüsü
        while True:
            try:
                # RBC Girişi
                RBC = float(input("RBC: "))
                ## RBC Kontrolü
                # if kucuk <= RBC <= buyuk:
                #     print("Sadece kucuk-buyuk arasında değer girebilirsiniz.")  
                #     continue
                break
            # Değer Hatası
            except ValueError:
                # Hata Açıklaması
                print("Sadece sayısal değer girebilirsiniz.")  
                continue
        # HGB Döngüsü
        while True:
            try:
                # HGB Girişi
                HGB = float(input("HGB: "))
                ## HGB Kontrolü
                # if kucuk <= HGB <= buyuk:
                #     print("Sadece kucuk-buyuk arasında değer girebilirsiniz.")  
                #     continue
                break
            # Değer Hatası
            except ValueError:
                # Hata Açıklaması
                print("Sadece sayısal değer girebilirsiniz.")  
                continue
        # HCT Döngüsü
        while True:
            try:
                # HCT Girişi
                HCT = float(input("HCT: "))
                ## HCT Kontrolü
                # if kucuk <= HCT <= buyuk:
                #     print("Sadece kucuk-buyuk arasında değer girebilirsiniz.")  
                #     continue
                break
            # Değer Hatası
            except ValueError:
                # Hata Açıklaması
                print("Sadece sayısal değer girebilirsiniz.")  
                continue
        # Listeye Değer Girişi
        H.append([numara, hasta_adı, cinsiyet, yaş, hasta_durumu, WBC, RBC, HGB, HCT])
        # Hasta Önizlemesi
        print("--- YENİ HASTA EKLENDİ ---")
        print("Hasta No: " + str(numara))
        print("Adı Soyadı: " +  hasta_adı)
        # Cinsiyet Datasını Stringe Dönüştürme
        if cinsiyet == True:
            cinsiyetRAW = "Erkek"
        else:
            cinsiyetRAW = "Kadın"
        print("Cinsiyeti: " + cinsiyetRAW)
        print("Yaşı: " +  str(yaş))
        print("Hasta Durumu (1-10): " + str(hasta_durumu))
        print("WBC: " + str(WBC))
        print("RBC: " + str(RBC))
        print("HGB: " + str(HGB))
        print("HCT: " + str(HCT))
        print("")
        print("- Yatak Kapasitesi: (" + str(len(H)) +"/25)")
        print("--------------------------")
    else:
        print('''
        
        ---- HATA -----
        Yatak kapasitesi maksimuma ulaştı! (25/25)
        ---------------

        ''')
    input("Ana ekrana dönmek için Enter tuşuna basın...")
    anaekran()

# Hasta Tarama
def tara():
    # While değeri
    i = len(H)
    # Kayıt kontrolü
    if len(H) == 0:
        print('''
        
        ---- HATA -----
        Herhangi bir kayıt bulunamadı.
        ---------------

        ''')
        return
    # Kayıt Çıktı Döngüsü
    while i > 0:
        i -= 1
        WBC = ""
        RBC = ""
        HGB = ""
        HCT = ""
        # WBC Değer Kontrolü
        if H[i][5] <= 4000:
            WBC = " - Değer normalin altında! (4000-10000)"
        elif H[i][6] >= 10000:
            WBC = " - Değer normalin üstünde! (4000-10000)"
        # Cinsiyete Bağlı Diğer Değerlerin Kontrolü
        if H[i][2]:
            # RBC Değer Kontrolü
            if H[i][6] <= 4.2:
                RBC = " - Değer normalin altında! (4.2/5.4)"
            elif H[i][6] >= 5.4 :
                RBC = " - Değer normalin üstünde! (4.2/5.4)"
            # HGB Değer Kontrolü
            if H[i][7] <= 13.5:
                HGB = " - Değer normalin altında! (13.5/17.5)"
            elif H[i][7] >= 17.5:
                HGB = " - Değer normalin üstünde! (13.5/17.5)"
            # HCT Değer Kontrolü
            if H[i][8] <= 35:
                HCT = " - Değer normalin altında! (35/45)"
            elif H[i][8] >= 45:
                HCT = " - Değer normalin üstünde! (35/45)"
        else:
            # RBC Değer Kontrolü
            if H[i][6] <= 4.7:
                RBC = " - Değer normalin altında! (4.7/6.1)"
            elif H[i][6] >= 6.1:
                RBC = " - Değer normalin üstünde! (4.7/6.1)"
            # HGB Değer Kontrolü
            if H[i][7] <= 12.5:
                HGB = " - Değer normalin altında! (12.5/15.5)"
            elif H[i][7] >= 15.5:
                HGB = " - Değer normalin üstünde! (12.5/15.5)"
            # HCT Değer Kontrolü
            if H[i][8] <= 39:
                HCT = " - Değer normalin altında! (39/50)"
            elif H[i][8] >= 50:
                HCT = " - Değer normalin üstünde! (39/50)"
            #
            # if kucuk <= H[i][x] <= buyuk:
            #     XYZ = " - Değer normal değil!"
            # else:
            #     XYZ = " - Değer normal. ("+str(H[i][x])+"/kucuk-buyuk)"
        # Tarama Çıktısı
        print("---")
        print("Hasta No: " + str(H[i][0]))
        print("Adı Soyadı: " +  str(H[i][1]))
        # Cinsiyet Datasını Stringe Dönüştürme
        if H[i][2] == True:
            cinsiyetRAW = "Erkek"
        else:
            cinsiyetRAW = "Kadın"
        print("Cinsiyeti: " + cinsiyetRAW)
        print("Yaşı: " +  str(H[i][3]))
        print("Hasta Durumu (1-10): " + str(H[i][4]))
        print("WBC: " + str(H[i][5]) + "" + WBC)
        print("RBC: " + str(H[i][6]) + " milyon mcL" + RBC)
        print("HGB: " + str(H[i][7]) + " gr/dl" + HGB)
        print("HCT: " + str(H[i][8]) + " ml/100ml" + HCT)
    print("---")
    print("- Yatak Kapasitesi: (" + str(len(H)) +"/25)")
    print("---")
    input("Ana ekrana dönmek için Enter tuşuna basın...")
    anaekran()

# Ana Ekran
def anaekran():
    print('''
--- Hasta Terminali ---
- Hangi işlemi yapmak istiyorsunuz''')
    # İşlem Döngüsü
    while True:
        # İşlem Girişi
        islem = input('''- (Ekle/Tara): ''')
        # Giriş Değer Kontrolü
        if islem.lower() == "ekle" or islem.lower() == "tara":
            break
        else:
            # Giriş Değer Hatası
            print(islem.lower())
            print("--- ")
            print("- !! Sadece Ekle ve Tara değerlerini girebilirsiniz.")  
            continue
    # Giriş yönlendirme
    if islem.lower() == "ekle":
        ekle()
    else:
        tara()

anaekran()