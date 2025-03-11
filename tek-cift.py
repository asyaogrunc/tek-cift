sayi = int(input("Bir sayı giriniz: "))

if sayi < 0:
    print("Negatif sayı girdiniz!")
else:
    if sayi % 2 == 0:
        print("Sayınız çift.")
    else:
        print("Sayınız tek.")