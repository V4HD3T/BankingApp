# Finansman türleri ve aylık kâr oranları, vade ve finansman tutarı sınırları
finansman_turleri = {
    1: {"isim": "Konut Finasnsmani Kampanya Paketi Sigortali (Kisa Vade) (0-1.000.000 TL)", "kar_orani": 4.29, "min_vade": 12, "max_vade": 60, "min_tutar": 0, "max_tutar": 1000000},
    2: {"isim": "Konut Finasnsmani Kampanya Paketi Sigortali (Uzun Vade) (0-1.000.000 TL)", "kar_orani": 4.34, "min_vade": 12, "max_vade": 120, "min_tutar": 0, "max_tutar": 1000000},
    3: {"isim": "Konut Finasnsmani (0-1.000.000 TL)", "kar_orani": 4.74, "min_vade": 61, "max_vade": 120, "min_tutar": 0, "max_tutar": 1000000},
    4: {"isim": "Konut Finasnsmani Sigortali (0-1.000.000 TL)", "kar_orani": 4.69, "min_vade": 1, "max_vade": 60, "min_tutar": 0, "max_tutar": 1000000},

    5: {"isim": "Konut Finasnsmani (Kisa Vade) (1.000.001-5.000.000 TL)", "kar_orani": 4.84, "min_vade": 12, "max_vade": 60, "min_tutar": 1000001, "max_tutar": 5000000},
    6: {"isim": "Konut Finasnsmani (Uzun Vade) (1.000.001-5.000.000 TL)", "kar_orani": 4.89, "min_vade": 61, "max_vade": 120, "min_tutar": 1000001, "max_tutar": 5000000},
    7: {"isim": "Konut Finasnsmani Kampanya Paketi Sigortali (Kisa Vade) (1.000.001-5.000.000 TL)", "kar_orani": 5.05, "min_vade": 12, "max_vade": 60, "min_tutar": 1000001, "max_tutar": 5000000},
    8: {"isim": "Konut Finasnsmani Kampanya Paketi Sigortali (Uzun Vade) (1.000.001-5.000.000 TL)", "kar_orani": 4.44, "min_vade": 61, "max_vade": 120, "min_tutar": 1000001, "max_tutar": 5000000},

    9: {"isim": "Tasit Finansmani (Kaskolu-Fatura Bedeli 0-400.000 TL)", "kar_orani": 4.95, "min_vade": 1, "max_vade": 48, "min_tutar": 0, "max_tutar": 400000},
    10: {"isim": "Tasit Finansmani (Kaskolu-Fatura Bedeli 400.001-800.000 TL)", "kar_orani": 4.95, "min_vade": 1, "max_vade": 36, "min_tutar": 400001, "max_tutar": 800000},
    11: {"isim": "Tasit Finansmani (Kaskolu-Fatura Bedeli 800.001-1.200.000 TL)", "kar_orani": 4.95, "min_vade": 1, "max_vade": 24, "min_tutar": 800001, "max_tutar": 1200000},
    12: {"isim": "Tasit Finansmani (Kaskolu-Fatura Bedeli 1.200.001-2.000.000 TL)", "kar_orani": 4.95, "min_vade": 1, "max_vade": 12, "min_tutar": 1200001, "max_tutar": 2000000},

    13: {"isim": "Tasit Finansmani (Kasko Diger-Fatura Bedeli 0-400.000 TL)", "kar_orani": 5.15, "min_vade": 1, "max_vade": 48, "min_tutar": 0, "max_tutar": 400000},
    14: {"isim": "Tasit Finansmani (Kasko Diger-Fatura Bedeli 400.001-800.000 TL)", "kar_orani": 5.15, "min_vade": 1, "max_vade": 36, "min_tutar": 400001, "max_tutar": 800000},
    15: {"isim": "Tasit Finansmani (Kasko Diger-Fatura Bedeli 800.001-1.200.000 TL)", "kar_orani": 5.15, "min_vade": 1, "max_vade": 24, "min_tutar": 800001, "max_tutar": 1200000},
    16: {"isim": "Tasit Finansmani (Kasko Diger-Fatura Bedeli 1.200.001-2.000.000 TL)", "kar_orani": 5.15, "min_vade": 1, "max_vade": 12, "min_tutar": 1200001, "max_tutar": 2000000},

    17: {"isim": "Ihtiyac Finansmani", "kar_orani": 5.25, "min_vade": 1, "max_vade": 36, "min_tutar": 1000, "max_tutar": 50000},
    18: {"isim": "Filika (Finansman Limitli Kart)", "kar_orani": 5.25, "min_vade": 1, "max_vade": 36, "min_tutar": 1000, "max_tutar": 50000},
    19: {"isim": "Bireysel Isyeri Finansmani (0-5.000.000 TL)", "kar_orani": 5.95, "min_vade": 1, "max_vade": 60, "min_tutar": 1, "max_tutar": 5000000},
    20: {"isim": "Arsa Finansmani (0-5.000.000 TL)", "kar_orani": 5.29, "min_vade": 1, "max_vade": 60, "min_tutar": 1, "max_tutar": 5000000},
    21: {"isim": "Yasa Kapsaminda Ipotekli Bireysel Finansman (YIBFK)", "kar_orani": 5.25, "min_vade": 1, "max_vade": 36, "min_tutar": 5000, "max_tutar": 50000},
    22: {"isim": "Ipotekli Bireysel Finansman (IBF)", "kar_orani": 5.25, "min_vade": 1, "max_vade": 36, "min_tutar": 5000, "max_tutar": 50000}
}

def kredi_odemesi(anapara, faiz_orani, aylik_sayisi):
    # Faiz oranını yüzde olarak almak ve oran olarak kullanmak
    aylik_faiz_orani = faiz_orani / 100
    aylik_odeme = anapara * aylik_faiz_orani * (1 + aylik_faiz_orani) ** aylik_sayisi / ((1 + aylik_faiz_orani) ** aylik_sayisi - 1)
    toplam_odeme = aylik_odeme * aylik_sayisi
    return aylik_odeme, toplam_odeme

# Uyarı mesajları
uyarilar = {
    9: "*Fatura/Kasko bedelinin azami %70'i kadar finansman kullanabilirsiniz.",
    8: "*Fatura/Kasko bedelinin azami %50'si kadar finansman kullanabilirsiniz.",
    10: "*Fatura/Kasko bedelinin azami %30'u kadar finansman kullanabilirsiniz.",
    13: "*Fatura/Kasko bedelinin azami %70'i kadar finansman kullanabilirsiniz.",
    14: "*Fatura/Kasko bedelinin azami %50'si kadar finansman kullanabilirsiniz.",
    15: "*Fatura/Kasko bedelinin azami %30'u kadar finansman kullanabilirsiniz.",
    16: "*Fatura/Kasko bedelinin azami %20'si kadar finansman kullanabilirsiniz."
}

# Kullanıcıdan Girdi Alma
print("Finansman Türleri:")
for tur, detaylar in finansman_turleri.items():
    print(f"{tur}: {detaylar['isim']}")

secili_tur_no = int(input("\nBir finansman türü numarası seçin: "))
secili_tur = finansman_turleri[secili_tur_no]
faiz_orani = secili_tur["kar_orani"]
min_vade = secili_tur["min_vade"]
max_vade = secili_tur["max_vade"]
min_tutar = secili_tur["min_tutar"]
max_tutar = secili_tur["max_tutar"]

print("\nKredi Ödeme Planı:")
anapara = float(input(f"Finansman Tutarı (TL) [{min_tutar}-{max_tutar}]: "))
if anapara < min_tutar or anapara > max_tutar:
    print(f"Finansman tutarı {min_tutar} TL ile {max_tutar} TL arasında olmalıdır.")
    anapara = float(input(f"Finansman Tutarı (TL) [{min_tutar}-{max_tutar}]: "))

aylik_sayisi = int(input(f"Vade (Ay) [{min_vade}-{max_vade}]: "))
if aylik_sayisi < min_vade or aylik_sayisi > max_vade:
    print(f"Vade süresi {min_vade} ay ile {max_vade} ay arasında olmalıdır.")
    aylik_sayisi = int(input(f"Vade (Ay) [{min_vade}-{max_vade}]: "))

aylik_odeme, toplam_odeme = kredi_odemesi(anapara, faiz_orani, aylik_sayisi)
print(f"\nFinansman Türü: {secili_tur['isim']}")
print(f"Aylık Kâr Oranı: {faiz_orani}%")
print(f"Finansman Tutarı: {anapara} TL")
print(f"Vade: {aylik_sayisi} Ay")
print("Aylık Ödeme: ", aylik_odeme)
print("Toplam Ödenecek Tutar: ", toplam_odeme)

# Uyarı mesajını göster
if secili_tur_no in uyarilar:
    print(uyarilar[secili_tur_no])
