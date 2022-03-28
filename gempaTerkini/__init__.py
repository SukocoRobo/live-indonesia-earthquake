import requests
from bs4 import BeautifulSoup
"""
methode = fungsi
field \ attribute = variable
constructor = (__init__) metode yang dipanggil pertaman kali saat object diciptakan, gunakan untuk mendeklarasikan semua 
fungsi pada class init
"""

class Bencana:
    def __init__(self, url, description):
        self.description = description
        self.result = None
        self.url = url

    def tampilkanKeterangan(self):
        print(self.description)

    def scraping_data(self):
        pass

    def tampilkan_data(self):
        pass

    def run(self):
        self.scraping_data()
        self.tampilkan_data()

class banjirTerkini(Bencana):
    def __init__(self, url):
        super(banjirTerkini, self).__init__(url, 'Not yet implemented   ')

    def tampilkanKeterangan(self):
        print(f'Under Construction {self.description}')



class gempaTerkini(Bencana):
    def __init__(self, url):
        super(gempaTerkini, self).__init__(url, 'to get the latest earthquake in idonesia from BMKG.go.id')

    def scraping_data(self):
        """
        Tanggal: 26 Maret 2022
        Waktu : 16:54:31 WIB
        Magnitudo : 4.3
        Kedalaman : 10 km
        Lokasi : 3.83 lat - 122.72 long
        :return:
        """
        try:
            content = requests.get(self.url)
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
            lat = None
            lon = None
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
            hasil['koordinat'] = {'ls': lat, 'bt': lon}
            hasil['pusat'] = pusat
            hasil['dirasakan'] = dirasakan
            self.result = hasil
        else:
            return None


    def tampilkan_data(self):
        if self.result is None:
            print("Tidak bisa menemukan data gempa terkini")
            return None

        print("Gempa Terakhir berdasarkan BMKG")
        print(f"Tanggal {self.result['tanggal']}")
        print(f"Waktu {self.result['waktu']}")
        print(f"Magnitudo {self.result['magnitudo']}")
        print(f"Lokasi: lat {self.result['koordinat']['ls']} & lon {self.result['koordinat']['bt']}")
        print(f"{self.result['pusat']}")
        print(f"{self.result['dirasakan']}")
    #    print(result)

    def run(self):
        self.scraping_data()
        self.tampilkan_data()




# if __name__ == '__main__':
#     print("package gempa terkini ")
if __name__ == '__main__':

    gempaIndonesia = gempaTerkini('https://bmkg.go.id')
    gempaIndonesia.tampilkanKeterangan()
    gempaIndonesia.run()

    banjirIndonesia = banjirTerkini('Notyet')
    gempaIndonesia.tampilkanKeterangan()
    banjirIndonesia.run()

    daftarBencana = [gempaIndonesia, banjirIndonesia]
    print('\nSemua bencana yang ada')
    for Bencana in daftarBencana:
        Bencana.tampilkanKeterangan()
