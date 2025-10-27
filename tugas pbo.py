class Kosmetik(object):
    nama = None
    merk = None
    harga = None

    def _init_(self, nama, merk, harga):
        self.nama = nama
        self.merk = merk
        self.harga = harga

    def info(self):
        print('Produk {} merek {} seharga Rp{:,}'.format(self.nama, self.merk, self.harga))

    def pakai(self):
        print('{} merek {} sedang digunakan.'.format(self.nama, self.merk))


class KosmetikWanita(Kosmetik):
    jenis = None
    warna = None

    def _init_(self, nama, jenis, merk, harga):
        super()._init_(nama, merk, harga)  # memanggil konstruktor dari Kosmetik
        self.jenis = jenis

    def set_warna(self, warna):
        self.warna = warna

    def pakai(self):
        print('{} merek {} jenis {} warna {} sedang digunakan. Harganya Rp{:,}'.format(
            self.nama, self.merk, self.jenis, self.warna, self.harga))


# Contoh objek
lipstik = KosmetikWanita('Lipstik', 'Matte', 'Wardah', 55000)
lipstik.set_warna('Merah Muda')

bedak = KosmetikWanita('Bedak', 'Two Way Cake', 'Emina', 65000)
bedak.set_warna('Natural Beige')

# Menampilkan informasi produk dan pemakaian
lipstik.info()
lipstik.pakai()

bedak.info()
bedak.pakai()