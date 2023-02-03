urunler={
    "ekmek":5,
    "yumurta":80,
    "tavuk":120,
    "et":200,
    "muz":30,
    "sigara":35
}
tutar=0
answer="e"
urunCikar="e"
while answer=="e":
    answer=input("Alışveriş yapmak ister misin ? \n(e veya h)")
    if answer!="e":
            while urunCikar=="e":
                urunCikar=input("Çıkarmak istediğiniz ürün var mı ? \n(e veya h)")
                if urunCikar=="e":
                    cikanUrun=input("Çıkarmak istediğiniz ürünü giriniz : \n")
                    for k,v in urunler.items():
                        cikar=urunler[cikanUrun]
                        tutar-=cikar
                        print(f"Alışverişi Tamamladınız!\nÖdemeniz Gereken Tutar\n{tutar} TL")
                        break   
                elif urunCikar!="e":
                    print(f"Alışverişi Tamamladınız!\nÖdemeniz Gereken Tutar\n{tutar} TL")
                    break
            break
    urun=input("Ne almak istersin\n(Küçük harflerle ürün adını giriniz.) : \nEkmek = 5 tl\nYumurta = 80tl\nTavuk = 120tl\nEt = 200 tl\nMuz = 30 tl\nSigara = 35 tl\n")
    for k,v in urunler.items():
        fiyat=urunler[urun]
    tutar+=fiyat