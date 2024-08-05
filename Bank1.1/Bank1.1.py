# Finansman turleri ve aylik kar oranlari
finansman_turleri = {
    "Tur 1": 0.01,
    "Tur 2": 0.015,
    "Tur 3": 0.02,
    "Tur 4": 0.025,
    "Tur 5": 0.03,
    "Tur 6": 0.035,
    "Tur 7": 0.04,
    "Tur 8": 0.045,
    "Tur 9": 0.05,
    "Tur 10": 0.055,
    "Tur 11": 0.06,
    "Tur 12": 0.065,
    "Tur 13": 0.07,
    "Tur 14": 0.075,
    "Tur 15": 0.08,
    "Tur 16": 0.085,
    "Tur 17": 0.09,
    "Tur 18": 0.095,
    "Tur 19": 0.10,
    "Tur 20": 0.105,
    "Tur 21": 0.11,
    "Tur 22": 0.115
}

def basit_faiz(anapara, faiz_orani, zaman):
    return anapara * faiz_orani * zaman

def bilesik_faiz(anapara, faiz_orani, zaman, bilesik_sayisi):
    return anapara * (1 + faiz_orani / bilesik_sayisi) ** (bilesik_sayisi * zaman)

def kredi_odemesi(anapara, faiz_orani, aylik_sayisi):
    aylik_faiz_orani = faiz_orani / 12
    aylik_odeme = anapara * aylik_faiz_orani * (1 + aylik_faiz_orani) ** aylik_sayisi / ((1 + aylik_faiz_orani) ** aylik_sayisi - 1)
    return aylik_odeme

# Kullanicidan Girdi Alma
print("Finansman Turleri:")
for tur in finansman_turleri:
    print(tur)

secili_tur = input("\nBir finansman turu secin: ")
faiz_orani = finansman_turleri[secili_tur]

print("\nBasit Faiz Hesaplama:")
anapara = float(input("Anapara (TL): "))
zaman = int(input("Ay Sayisi: "))
print("Toplam Faiz: ", basit_faiz(anapara, faiz_orani, zaman))

print("\nBilesik Faiz Hesaplama:")
anapara = float(input("Anapara (TL): "))
zaman = int(input("Ay Sayisi: "))
bilesik_sayisi = int(input("Yilda Kac Kez Bilesik Faiz Uygulaniyor: "))
print("Toplam Miktar: ", bilesik_faiz(anapara, faiz_orani, zaman / 12, bilesik_sayisi))

print("\nKredi Odeme Plani:")
anapara = float(input("Kredi Tutari (TL): "))
aylik_sayisi = int(input("Kredi Suresi (Ay): "))
print("Aylik Odeme: ", kredi_odemesi(anapara, faiz_orani, aylik_sayisi))
