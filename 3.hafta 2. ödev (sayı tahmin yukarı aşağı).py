
sayımız=48
deneme=0

#kullanıcıdan tahmin isminde bir değer alıyoruz
#alınan değeri deniyoruz int mı değil ise uyarı yapıp tekrar değer alıyoruz
while True:
    try:
        tahmin=int(input("\n1 ile 100 arasında tuttuğum sayıyı bul bakalım...")) 
    except ValueError:
        print(" \n***Lütfen bir tam sayı giriniz***")
        continue
    deneme+=1
    if tahmin-sayımız>15:
        print("\nFazla yukarı çıktın biraz aşağıya in..")
        continue
    
    elif tahmin-sayımız>0:
        print("\nÇok yaklaştın biraz aşağıya in..")
        continue

    elif tahmin-sayımız==0:
        print("Aferin", deneme,"inci denemede tuttuğum sayıyı buldun")
        break
    elif tahmin-sayımız>-15:
        print("\nÇok yaklaştın biraz yukarı çık..")
        continue
    
    elif tahmin-sayımız<-15:
        print("\nÇok düşük tahminde bulundun daha yüksek bir sayı girmelisin...")
        continue

        
