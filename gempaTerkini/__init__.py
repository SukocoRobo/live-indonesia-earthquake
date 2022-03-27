import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    Tanggal: 26 Maret 2022
    Waktu : 16:54:31 WIB
    Magnitudo : 4.3
    Kedalaman : 10 km
    Lokasi : 3.83 lat - 122.72 long
    :return:
    """
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        # print(content.text)
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        waktu = result[1]
        tanggal = result[0]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        ls = None
        bt = None
        kedalaman = None
        pusat = None
        dirasakan = None

        for res in result:
        #    print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                lokasi = res.text.split(' - ')
                ls = lokasi[0]
                bt = lokasi[1]
            elif i == 4:
                pusat = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal  # '26 Maret 2022'
        hasil['waktu'] = waktu  # '16:54:31 WIB'
        hasil['magnitudo'] = magnitudo
        hasil['kedalama'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['pusat'] = pusat
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None


def tampilkan_data(result) -> object:
    if result is None:
        print("Tidak bisa menemukan data gempa terkini")
        return None

    print("Gempa Terakhir berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi: LS={result['koordinat']['ls']} & BT={result['koordinat']['bt']}")
    print(f"{result['pusat']}")
    print(f"{result['dirasakan']}")
#    print(result)

# if __name__ == '__main__':
#     print("package gempa terkini ")
if __name__ == '__main__':
    result = ekstraksi_data()
    tampilkan_data(result)