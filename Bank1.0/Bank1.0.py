def basit_faiz(anapara, faiz_orani, zaman):
    return anapara * faiz_orani * zaman

def bilesik_faiz(anapara, faiz_orani, zaman, bileşik_sayisi):
    return anapara * (1 + faiz_orani / bileşik_sayisi) ** (bileşik_sayisi * zaman)

def kredi_odemesi(anapara, faiz_orani, yil_sayisi):
    aylik_faiz_orani = faiz_orani / 12
    toplam_odeme_sayisi = yil_sayisi * 12
    aylik_odeme = anapara * aylik_faiz_orani * (1 + aylik_faiz_orani) ** toplam_odeme_sayisi / ((1 + aylik_faiz_orani) ** toplam_odeme_sayisi - 1)
    return aylik_odeme

# Kullanıcıdan Girdi Alma
print("Basit Faiz Hesaplama:")
anapara = float(input("Anapara (TL): "))
faiz_orani = float(input("Yıllık Faiz Oranı (desimal olarak, örn. 0.05): "))
zaman = int(input("Yıl Sayısı: "))
print("Toplam Faiz: ", basit_faiz(anapara, faiz_orani, zaman))

print("\nBileşik Faiz Hesaplama:")
anapara = float(input("Anapara (TL): "))
faiz_orani = float(input("Yıllık Faiz Oranı (desimal olarak, örn. 0.05): "))
zaman = int(input("Yıl Sayısı: "))
bilesik_sayisi = int(input("Yılda Kaç Kez Bileşik Faiz Uygulanıyor: "))
print("Toplam Miktar: ", bilesik_faiz(anapara, faiz_orani, zaman, bilesik_sayisi))

print("\nKredi Ödeme Planı:")
anapara = float(input("Kredi Tutarı (TL): "))
faiz_orani = float(input("Yıllık Faiz Oranı (desimal olarak, örn. 0.05): "))
yil_sayisi = int(input("Kredi Süresi (Yıl): "))
print("Aylık Ödeme: ", kredi_odemesi(anapara, faiz_orani, yil_sayisi))
