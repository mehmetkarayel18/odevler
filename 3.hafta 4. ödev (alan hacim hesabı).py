

while True:
    print("**Lütfen aşağıdaki işlemlerden seçmek istediğiniz işlemin numarasını tıklayınız**")
    print("""
1-Kare Alan Hesaplama
2-Dikdörtgen Alan Hesaplama
3-Üçgen Alan Hesaplama
4-Küre hacim hesaplama
5-Küp hacim hesaplama
6-Koni hacim hesaplama
7-**ÇIKIŞ**""")
    try:
        secim=int(input("\n\n Seçiminiz.....:"))
    except ValueError:
        print("Lütfen belirlenen tam sayı değerlerinden birini giriniz...")
        continue
    if not 0<secim<8:
        print("Lütfen 1-7 aralığında tam sayı değeri giriniz")
        continue
    
#
# KARE ALANI
    if secim==1:
        try:
            boyut1=float(input("Lütfen alanını hesaplamak istediğiniz karenin bir kenar uzunluğunu giriniz..:"))
            print("\nKarenin alanı   =",boyut1*boyut1)
        except ValueError:
            print("Lütfen sayısal bir değer giriniz..:")
        continue
        
        
    #DİKDÖRTGEN ALANI
    if secim==2:
        try:
            boyut1=float(input("Lütfen alanını hesaplamak istediğiniz dikdörtgenin enini giriniz..:"))
            boyut2=float(input("Lütfen alanını hesaplamak istediğiniz dikdörtgenin boyunu giriniz..:"))
            print("\nDikdörtgenin alanı   =",boyut1*boyut2)
        except ValueError:
            print("Lütfen sayısal bir değer giriniz..:")
        continue
        
    # ÜÇGEN ALANI
    if secim==3:
        try:
            boyut1=float(input("Lütfen alanını hesaplamak istediğiniz üçgenin tabanını giriniz..:"))
            boyut2=float(input("Lütfen alanını hesaplamak istediğiniz yüksekliğini giriniz..:"))
            print("\nDikdörtgenin alanı   =",boyut1*boyut2*0.5)
           
        except ValueError:
            print("Lütfen sayısal bir değer giriniz..:")
        print("\nDikdörtgenin alanı   =",boyut1*boyut2*0.5)
        continue

    # KÜRE HACMİ
    if secim==4:
        try:
            boyut1=float(input("Lütfen hacmini hesaplamak istediğiniz kürenin yarıçapını giriniz..:"))
            print("Kürenin hacmi   =",(boyut1**3)*3.14*(4/3))
           
        except ValueError:
            print("Lütfen sayısal bir değer giriniz..:")
        continue

    # KÜPÜN HACMİ
    if secim==5:
        try:
            boyut1=float(input("Lütfen hacmini hesaplamak istediğiniz küpün kenar uzunluğunu giriniz..:"))
            print("Küpün hacmi   =",boyut1**3)
           
        except ValueError:
            print("Lütfen sayısal bir değer giriniz..:")
        continue
        

    # KONİNİN HACMİ
    if secim==6:
        try:
            boyut1=float(input("Lütfen hacmini hesaplamak istediğiniz konini taban yarıçapını giriniz..:"))
            boyut2=float(input("Lütfen hacmini hesaplamak istediğiniz koninin yüksekliğini giriniz ..:"))
            print("\nDikdörtgenin alanı   =",3.14*(boyut1**2)*boyut1*(1/3))
        except ValueError:
            print("Lütfen sayısal bir değer giriniz..:")
        continue
        

    # ÇIKIŞ
    if secim==7:
       print("SİSTEM KAPANIYOR")
       break



        
               
    
