##kullanıcıdan username ve parola girmesi istenir
sıra=1
islem=1
kayıt=True
devam=True
#isim ve parola girilmesi istenir
while kayıt==True:
    isim=input("Lütfen bir kullanıcı adı belirleyiniz..:")
    parola=input("Lütfen bir parola belirleyiniz..:")

#isim dosyada kayıtlı mı diye kontrol edilir
    
    with open("isim-parola listesi.txt","r") as isimliste:
        text= isimliste.read()
        if (")"+isim+"**") in text:       
            print("\n\n***  Bu isim başka bir kullanıcı tarafından kullanılıyor, Lütfen Başka bir isim deneyin\n")
            continue
    with open("isim-parola listesi.txt","a") as isimliste:

        print(sıra,")",isim,"**""\t\t",parola,sep="",file=isimliste)
        sıra+=1
        
 #kayda devam edilmesi sorulur ve ona göre hareket edilir
        
    while True:  
        secim=input("\n\ndevam etmek için (e), çıkmak için (h) tuşuna basın....:")
        
        if secim=="e":
            kayıt=True
            break
        if secim=="h":
            kayıt=False
            break
        else:
            print("Lütfen size sunulan seçeneklerden birini tuşlayın")
            continue
        
