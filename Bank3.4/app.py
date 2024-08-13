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
    return "{:.2f}".format(yuvarlanmis_deger)

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
    10: "*Fatura/Kasko bedelinin azami %30'u kadar finansman kullanabilirsiniz.",
    13: "*Fatura/Kasko bedelinin azami %70'i kadar finansman kullanabilirsiniz.",
    14: "*Fatura/Kasko bedelinin azami %50'si kadar finansman kullanabilirsiniz.",
    15: "*Fatura/Kasko bedelinin azami %30'u kadar finansman kullanabilirsiniz.",
    16: "*Fatura/Kasko bedelinin azami %20'si kadar finansman kullanabilirsiniz."
}

@app.route('/', methods=['GET', 'POST'])
def index():
    finansman_turleri = get_finansman_turleri()
    hata_mesaji = None
    secili_tur_no = None

    if request.method == 'POST':
        secili_tur_no = int(request.form['finansman_turu'])
        secili_tur = finansman_turleri[secili_tur_no]
        anapara = float(request.form['anapara'])
        aylik_sayisi = int(request.form['vade'])

        if anapara < secili_tur["min_tutar"] or anapara > secili_tur["max_tutar"]:
            hata_mesaji = f"Finansman tutarı {int(secili_tur['min_tutar'])} TL ile {int(secili_tur['max_tutar'])} TL arasında olmalıdır."
        elif aylik_sayisi < secili_tur["min_vade"] or aylik_sayisi > secili_tur["max_vade"]:
            hata_mesaji = f"Vade süresi {secili_tur['min_vade']} ay ile {secili_tur['max_vade']} ay arasında olmalıdır."
        else:
            aylik_odeme, toplam_odeme = kredi_odemesi(anapara, secili_tur["kar_orani"], aylik_sayisi)
            aylik_odeme = yuvarla_ve_formatla(aylik_odeme)
            toplam_odeme = yuvarla_ve_formatla(toplam_odeme)

            uyarı = uyarilar.get(secili_tur_no, "")

            return render_template('index.html', finansman_turleri=finansman_turleri, sonuc=True,
                                   secili_tur=secili_tur, anapara=anapara, aylik_sayisi=aylik_sayisi,
                                   aylik_odeme=aylik_odeme, toplam_odeme=toplam_odeme, uyarı=uyarı,
                                   secili_tur_no=secili_tur_no, hata_mesaji=None)

    return render_template('index.html', finansman_turleri=finansman_turleri, sonuc=False, hata_mesaji=hata_mesaji, secili_tur_no=secili_tur_no)

if __name__ == '__main__':
    app.run(debug=True)
