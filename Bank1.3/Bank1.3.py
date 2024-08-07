# Finansman turleri ve aylik kar oranlari ve vade sinirlari
finansman_turleri = {
    1: {"isim": "Konut Finasnsmani Kampanya Paketi Sigortali (Kisa Vade) (0-1.000.000 TL)", "kar_orani": 4.29, "max_vade": 60},
    2: {"isim": "Konut Finasnsmani Kampanya Paketi Sigortali (Uzun Vade) (0-1.000.000 TL)", "kar_orani": 4.34, "max_vade": 120},

    3: {"isim": "Konut Finasnsmani Sigortali (0-1.000.000 TL)", "kar_orani": 4.69, "max_vade": 60},
    4: {"isim": "Konut Finasnsmani (0-1.000.000 TL)", "kar_orani": 4.74, "max_vade": 120},
    5: {"isim": "Konut Finasnsmani (Kisa Vade) (1.000.001-5.000.000 TL)", "kar_orani": 4.84, "max_vade": 60},
    6: {"isim": "Konut Finasnsmani (Uzun Vade) (1.000.001-5.000.000 TL)", "kar_orani": 4.89, "max_vade": 120},

    7: {"isim": "Konut Finasnsmani Kampanya Paketi Sigortali (Kisa Vade) (1.000.001-5.000.000 TL)", "kar_orani": 5.05, "max_vade": 60},
    8: {"isim": "Konut Finasnsmani Kampanya Paketi Sigortali (Uzun Vade) (1.000.001-5.000.000 TL)", "kar_orani": 4.44, "max_vade": 120},

    9: {"isim": "Tasit Finansmani (Kaskolu-Fatura Bedeli 0-400.000 TL)", "kar_orani": 4.95, "max_vade": 48},
    10: {"isim": "Tasit Finansmani (Kaskolu-Fatura Bedeli 400.001-800.000 TL)", "kar_orani": 4.95, "max_vade": 36},
    11: {"isim": "Tasit Finansmani (Kaskolu-Fatura Bedeli 800.001-1.200.000 TL)", "kar_orani": 4.95, "max_vade": 24},
    12: {"isim": "Tasit Finansmani (Kaskolu-Fatura Bedeli 1.200.001-2.000.000 TL)", "kar_orani": 4.95, "max_vade": 12},
    
    13: {"isim": "Tasit Finansmani (Kasko Diger-Fatura Bedeli 0-400.000 TL)", "kar_orani": 5.15, "max_vade": 48},
    14: {"isim": "Tasit Finansmani (Kasko Diger-Fatura Bedeli 400.001-800.000 TL)", "kar_orani": 5.15, "max_vade": 36},
    15: {"isim": "Tasit Finansmani (Kasko Diger-Fatura Bedeli 800.001-1.200.000 TL)", "kar_orani": 5.15, "max_vade": 24},
    16: {"isim": "Tasit Finansmani (Kasko Diger-Fatura Bedeli 1.200.001-2.000.000 TL)", "kar_orani": 5.15, "max_vade": 12},

    17: {"isim": "Ihtiyac Finansmani", "kar_orani": 5.25, "max_vade": 36},
    19: {"isim": "Filika (Finansman Limitli Kart)", "kar_orani": 5.25, "max_vade": 36},
    20: {"isim": "Bireysel Isyeri FInansmani (0-5.000.000 TL)", "kar_orani": 5.95, "max_vade": 60},
    21: {"isim": "Arsa Finansmani (0-5.000.000 TL)", "kar_orani": 5.29, "max_vade": 60},
    22: {"isim": "Yasa Kapsaminda Ipotekli Bireysel Finansman (YIBFK)", "kar_orani": 5.25, "max_vade": 36},
    23: {"isim": "Ipotekli Bireysel Finansman (IBF)", "kar_orani": 5.25, "max_vade": 36}
}

def kredi_odemesi(anapara, faiz_orani, aylik_sayisi):
    aylik_faiz_orani = faiz_orani
    aylik_odeme = anapara * aylik_faiz_orani * (1 + aylik_faiz_orani) ** aylik_sayisi / ((1 + aylik_faiz_orani) ** aylik_sayisi - 1)
    toplam_odeme = aylik_odeme * aylik_sayisi
    return aylik_odeme, toplam_odeme

# Kullanicidan Girdi Alma
print("Finansman Turleri:")
for tur, detaylar in finansman_turleri.items():
    print(f"{tur}: {detaylar['isim']}")

secili_tur_no = int(input("\nBir finansman turu numarasi secin: "))
secili_tur = finansman_turleri[secili_tur_no]
faiz_orani = secili_tur["kar_orani"]
max_vade = secili_tur["max_vade"]

print("\nKredi Odeme Plani:")
anapara = float(input("Finansman Tutari (TL): "))
aylik_sayisi = int(input(f"Vade (Ay) [Maksimum {max_vade} ay]: "))
if aylik_sayisi > max_vade:
    print(f"Maksimum kredi suresi {max_vade} ay olabilir. {max_vade} ay olarak ayarlaniyor.")
    aylik_sayisi = max_vade

aylik_odeme, toplam_odeme = kredi_odemesi(anapara, faiz_orani, aylik_sayisi)
print(f"\nFinansman Turu: {secili_tur['isim']}")
print(f"Aylik Kar Orani: {faiz_orani}")
print(f"Finansman Tutari: {anapara} TL")
print(f"Vade: {aylik_sayisi} Ay")
print("Aylik Odeme: ", aylik_odeme)
print("Toplam Odenecek Tutar: ", toplam_odeme)
