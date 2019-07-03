while True:
    try:
        sayı=int(input("\nAsal olup olmadığını kontrol etmek  istediğiniz sayıyı giriniz..   :"))

    except ValueError:
        print("***Lütfen tam sayı değeri giriniz!!!")
        continue
# asal sayı olduğunu kontrol ederiz
    for i in range(2,sayı):
        if sayı%i==0:
            print("\nBu sayı asal değildir, en küçük böleni ",i,"dir")
            break
        if i==sayı-1:
            print ("\nGirdiğiniz sayı asal sayıdır..")
    devam=input("\n Tekrar denemek için (e) tuşuna, çıkmak için her hangi bir tuşa basınız    :")
    if devam=="e":
        continue
    else:
        break
