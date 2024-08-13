from flask import Flask, render_template, request
import pyodbc
import math

app = Flask(__name__)

def kredi_odemesi(anapara, faiz_orani, aylik_sayisi):
    aylik_faiz_orani = faiz_orani / 100
    aylik_odeme = anapara * aylik_faiz_orani * (1 + aylik_faiz_orani) ** aylik_sayisi / ((1 + aylik_faiz_orani) ** aylik_sayisi - 1)
    toplam_odeme = aylik_odeme * aylik_sayisi
    return aylik_odeme, toplam_odeme

def yuvarla_ve_formatla(deger):
    yuvarlanmis_deger = math.ceil(deger * 100) / 100
    if yuvarlanmis_deger.is_integer():
        return "{:,.0f}".format(yuvarlanmis_deger).replace(',', '.')
    else:
        return "{:,.2f}".format(yuvarlanmis_deger).replace(',', 'X').replace('.', ',').replace('X', '.')

def get_finansman_turleri():
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=MSI;'
                              'Database=FinansmanDB;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute('SELECT ID, İsim, Kar_Orani, Min_Vade, Max_Vade, Min_Tutar, Max_Tutar FROM dbo.FinansmanDB')

        finansman_turleri = {}
        for row in cursor:
            finansman_turleri[row.ID] = {
                "isim": row.İsim,
                "kar_orani": row.Kar_Orani,
                "min_vade": row.Min_Vade,
                "max_vade": row.Max_Vade,
                "min_tutar": row.Min_Tutar,
                "max_tutar": row.Max_Tutar
            }

        cursor.close()
        conn.close()
        return finansman_turleri

    except Exception as e:
        print("Veritabanı bağlantı hatası:", str(e))
        return {}

uyarilar = {
    9: "*Fatura/Kasko bedelinin azami %70'i kadar finansman kullanabilirsiniz.",
    8: "*Fatura/Kasko bedelinin azami %50'si kadar finansman kullanabilirsiniz.",
    7: "*Fatura/Kasko bedelinin azami %30'u kadar finansman kullanabilirsiniz."
}

@app.route('/', methods=['GET', 'POST'])
def hesaplama():
    finansman_turleri = get_finansman_turleri()
    hata_mesaji = None
    sonuc = False
    secili_tur = None
    secili_tur_no = None
    anapara = None
    aylik_sayisi = None
    aylik_odeme = None
    toplam_odeme = None
    uyarı = None

    if request.method == 'POST':
        try:
            anapara = float(request.form['anapara'].replace('.', '').replace(',', '.'))
            aylik_sayisi = int(request.form['vade'])
            secili_tur_no = int(request.form['finansman_turu'])

            if secili_tur_no in finansman_turleri:
                secili_tur = finansman_turleri[secili_tur_no]
                min_tutar = secili_tur['min_tutar']
                max_tutar = secili_tur['max_tutar']
                min_vade = secili_tur['min_vade']
                max_vade = secili_tur['max_vade']

                if anapara < min_tutar or anapara > max_tutar or aylik_sayisi < min_vade or aylik_sayisi > max_vade:
                    hata_mesaji = f"Geçersiz giriş! Finansman Tutarı {min_tutar} - {max_tutar} TL ve Vade {min_vade} - {max_vade} ay arasında olmalıdır."
                else:
                    aylik_odeme, toplam_odeme = kredi_odemesi(anapara, secili_tur['kar_orani'], aylik_sayisi)
                    aylik_odeme = yuvarla_ve_formatla(aylik_odeme)
                    toplam_odeme = yuvarla_ve_formatla(toplam_odeme)
                    sonuc = True
                    uyarı = uyarilar.get(secili_tur_no, "")

        except Exception as e:
            hata_mesaji = "Geçersiz giriş! Lütfen tekrar deneyiniz."

    return render_template('index.html',
                           finansman_turleri=finansman_turleri,
                           hata_mesaji=hata_mesaji,
                           sonuc=sonuc,
                           secili_tur=secili_tur,
                           secili_tur_no=secili_tur_no,
                           anapara=anapara,
                           aylik_sayisi=aylik_sayisi,
                           aylik_odeme=aylik_odeme,
                           toplam_odeme=toplam_odeme,
                           uyarı=uyarı)

if __name__ == '__main__':
    app.run(debug=True)
