cimbom=open("galatasaraylı oyuncular.txt","w")
fener=open("fenerbahceli oyuncular.txt","w")
kartal=open("besiktaslı oyuncular.txt","w")
try:
    with open("futbolcular.txt","r") as analiste:
        analiste.seek(0)
        satır=1
        while satır<71:
           
            kisi=analiste.readline()

            if ("Fenerbahçe") in kisi:
                isim=""
                for i in kisi:
                    if i==",":
                        break
                    else:
                        isim +=i
                
                isim+="\n"
                fener.write(isim)
                satır+=1


            elif ("Galatasaray") in kisi:
                isim=""
                for i in kisi:
                    if i==",":
                        break
                    else:
                        isim +=i
                
                isim+="\n"
                cimbom.write(isim)
                satır+=1


            elif ("Beşiktaş") in kisi:
                isim=""
                for i in kisi:
                    if i==",":
                        break
                    else:
                        isim +=i
                
                isim+="\n"
                kartal.write(isim)
                satır+=1
except FileNotFoundError:
    print("Futbolcular listesi bulunamadı. bu sebeple işleminiz gerçekleşemedi..")
cimbom.close()
fener.close()
kartal.close()
print("Program kapanıyor")


