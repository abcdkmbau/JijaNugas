class Masak:
    def __init__(self,namapemasak,burger):
        self.namapemasak = namapemasak
        self.burger = burger

    def jual(self, jumlah_burger):
        print('Jumlah burger awal : ', self.burger)
        print('Jumlah burger dipesan : ' , jumlah_burger)
        self.burger -= jumlah_burger
        print('Sisa burger : ' , self.burger)

    def burger_dibeli(self, pembeli, jumlah_dibeli, total_beli):
        print('Nama Penjual : ' + self.namapemasak)
        print('Nama Pembeli : ' + pembeli.namapemasak)
        pembeli.burger -= jumlah_dibeli
        self.burger += jumlah_dibeli
        print()
        print('Stok burger : ', self.burger)
        print('Sisa burger : ' , pembeli.burger)
        print('Total pembelian '+ pembeli.burger + "Rp " total_beli)

jijah = Masak('Azizah', 100) 
risa = Masak('Risa', 75)

jijah.jual(7)
jijah.burger_dibeli(risa,20)
