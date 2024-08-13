import pyodbc

def kredi_odemesi(anapara, faiz_orani, aylik_sayisi):
    aylik_faiz_orani = faiz_orani / 100
    aylik_odeme = anapara * aylik_faiz_orani * (1 + aylik_faiz_orani) ** aylik_sayisi / ((1 + aylik_faiz_orani) ** aylik_sayisi - 1)
    toplam_odeme = aylik_odeme * aylik_sayisi
    return aylik_odeme, toplam_odeme

# Baglanti ayarlari
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MSI;'
                      'Database=FinansmanDB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT ID, Isim, Kar_Orani, Min_Vade, Max_Vade, Min_Tutar, Max_Tutar FROM dbo.FinansmanDB')

finansman_turleri = {}
for row in cursor:
    finansman_turleri[row.ID] = {
        "isim": row.Isim,
        "kar_orani": row.Kar_Orani,
        "min_vade": row.Min_Vade,
        "max_vade": row.Max_Vade,
        "min_tutar": row.Min_Tutar,
        "max_tutar": row.Max_Tutar
    }

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
while anapara < min_tutar or anapara > max_tutar:
    print(f"Finansman tutarı {min_tutar} TL ile {max_tutar} TL arasında olmalıdır.")
    anapara = float(input(f"Finansman Tutarı (TL) [{min_tutar}-{max_tutar}]: "))

aylik_sayisi = int(input(f"Vade (Ay) [{min_vade}-{max_vade}]: "))
while aylik_sayisi < min_vade or aylik_sayisi > max_vade:
    print(f"Vade süresi {min_vade} ay ile {max_vade} ay arasında olmalıdır.")
    aylik_sayisi = int(input(f"Vade (Ay) [{min_vade}-{max_vade}]: "))

aylik_odeme, toplam_odeme = kredi_odemesi(anapara, faiz_orani, aylik_sayisi)
print(f"\nFinansman Türü: {secili_tur['isim']}")
print(f"Aylık Kâr Oranı: {faiz_orani}%")
print(f"Finansman Tutarı: {anapara} TL")
print(f"Vade: {aylik_sayisi} Ay")
print(f"Aylık Ödeme: {aylik_odeme}")
print(f"Toplam Ödenecek Tutar: {toplam_odeme}")

# Uyarı mesajını göster
if secili_tur_no in uyarilar:
    print(uyarilar[secili_tur_no])
