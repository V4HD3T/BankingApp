# Finansman turleri ve aylik kar oranlari ve vade sinirlari
finansman_turleri = {
    1: {"isim": "Tur 1", "kar_orani": 0.01, "max_vade": 24},
    2: {"isim": "Tur 2", "kar_orani": 0.015, "max_vade": 36},
    3: {"isim": "Tur 3", "kar_orani": 0.02, "max_vade": 48},
    4: {"isim": "Tur 4", "kar_orani": 0.025, "max_vade": 60},
    5: {"isim": "Tur 5", "kar_orani": 0.03, "max_vade": 72},
    6: {"isim": "Tur 6", "kar_orani": 0.035, "max_vade": 84},
    7: {"isim": "Tur 7", "kar_orani": 0.04, "max_vade": 96},
    8: {"isim": "Tur 8", "kar_orani": 0.045, "max_vade": 108},
    9: {"isim": "Tur 9", "kar_orani": 0.05, "max_vade": 120},
    10: {"isim": "Tur 10", "kar_orani": 0.055, "max_vade": 132},
    11: {"isim": "Tur 11", "kar_orani": 0.06, "max_vade": 144},
    12: {"isim": "Tur 12", "kar_orani": 0.065, "max_vade": 156},
    13: {"isim": "Tur 13", "kar_orani": 0.07, "max_vade": 168},
    14: {"isim": "Tur 14", "kar_orani": 0.075, "max_vade": 180},
    15: {"isim": "Tur 15", "kar_orani": 0.08, "max_vade": 192},
    16: {"isim": "Tur 16", "kar_orani": 0.085, "max_vade": 204},
    17: {"isim": "Tur 17", "kar_orani": 0.09, "max_vade": 216},
    18: {"isim": "Tur 18", "kar_orani": 0.095, "max_vade": 228},
    19: {"isim": "Tur 19", "kar_orani": 0.10, "max_vade": 240},
    20: {"isim": "Tur 20", "kar_orani": 0.105, "max_vade": 252},
    21: {"isim": "Tur 21", "kar_orani": 0.11, "max_vade": 264},
    22: {"isim": "Tur 22", "kar_orani": 0.115, "max_vade": 276}
}
    
def basit_faiz(anapara, faiz_orani, zaman):
    return anapara * faiz_orani * zaman

def bilesik_faiz(anapara, faiz_orani, zaman, bilesik_sayisi):
    return anapara * (1 + faiz_orani / bilesik_sayisi) ** (bilesik_sayisi * zaman)

def kredi_odemesi(anapara, faiz_orani, aylik_sayisi):
    aylik_faiz_orani = faiz_orani / 12
    aylik_odeme = anapara * aylik_faiz_orani * (1 + aylik_faiz_orani) ** aylik_sayisi / ((1 + aylik_faiz_orani) ** aylik_sayisi - 1)
    toplam_odeme = aylik_odeme * aylik_sayisi
    return aylik_odeme, toplam_odeme

# Kullanıcıdan Girdi Alma
print("Finansman Türleri:")
for tur, detaylar in finansman_turleri.items():
    print(f"{tur}: {detaylar['isim']}")

secili_tur_no = int(input("\nBir finansman türü numarası seçin: "))
secili_tur = finansman_turleri[secili_tur_no]
faiz_orani = secili_tur["kar_orani"]
max_vade = secili_tur["max_vade"]

print("\nBasit Faiz Hesaplama:")
anapara = float(input("Anapara (TL): "))
zaman = int(input(f"Vade (Ay) [Maksimum {max_vade} ay]: "))
if zaman > max_vade:
    print(f"Maksimum vade {max_vade} ay olabilir. {max_vade} ay olarak ayarlanıyor.")
    zaman = max_vade
print("Toplam Faiz: ", basit_faiz(anapara, faiz_orani, zaman))

print("\nBileşik Faiz Hesaplama:")
anapara = float(input("Anapara (TL): "))
zaman = int(input(f"Vade (Ay) [Maksimum {max_vade} ay]: "))
if zaman > max_vade:
    print(f"Maksimum vade {max_vade} ay olabilir. {max_vade} ay olarak ayarlanıyor.")
    zaman = max_vade
bilesik_sayisi = int(input("Yılda Kaç Kez Bileşik Faiz Uygulanıyor: "))
print("Toplam Miktar: ", bilesik_faiz(anapara, faiz_orani, zaman / 12, bilesik_sayisi))

print("\nKredi Ödeme Planı:")
anapara = float(input("Kredi Tutarı (TL): "))
aylik_sayisi = int(input(f"Kredi Süresi (Ay) [Maksimum {max_vade} ay]: "))
if aylik_sayisi > max_vade:
    print(f"Maksimum kredi süresi {max_vade} ay olabilir. {max_vade} ay olarak ayarlanıyor.")
    aylik_sayisi = max_vade
aylik_odeme, toplam_odeme = kredi_odemesi(anapara, faiz_orani, aylik_sayisi)
print("Aylık Ödeme: ", aylik_odeme)
print("Toplam Ödenecek Tutar: ", toplam_odeme)
