def login():
    from prettytable import PrettyTable  

    tabela = PrettyTable()
    tabela.field_names = ["No", "pilihan"]
    def deta(no, pilihan):
        tabela.add_row([no, pilihan])

    deta("1", "Admin")
    deta("2", "Peminjam")
    deta("3", "Keluar")
    print(tabela)
    pengguna = input("Pilih pengguna: ")
    password = input("Masukan password: ")
    if pengguna == "1":
        if password == "admin123":
            admin()
    elif pengguna == "2":
        if password == "peminjam123":
            user()
    elif pengguna == "3":
        print("Triema kasih dan sampai jumpa lagi ")
    else:
        print("Maaf tidak ada inputan")

# prettytable
from prettytable import PrettyTable  

table = PrettyTable()
table.field_names = ["No", "Nomor kelas", "Nama kelas", "Waktu kosong "]
def pinjaman_kelas(no, nomor_kelas, nama_kelas, waktu_kosong):
    table.add_row([no, nomor_kelas,nama_kelas, waktu_kosong])

pinjaman_kelas("1", "C301", "Komputer", "12:40")
pinjaman_kelas("2", "C302", "Lab", "10:30")
pinjaman_kelas("3", "C303", "kelas 1", "13:50")
pinjaman_kelas("4", "C401", "Kelas 3", "07:30")
pinjaman_kelas("5", "C402", "Kelas 4", "11:20")

def admin():
    nama = input("Masukan Nama Anda: ")
    while True:
        print(f"Selamat Datang ({nama}) silahkan pilih pilihan anda")
        from prettytable import PrettyTable  

        tabel = PrettyTable()
        tabel.field_names = ["No", "pilihan"]

        def data(no, pilihan):
            tabel.add_row([no, pilihan])

        data("1", "tambah kelas")
        data("2", "lihat kelas")
        data("3", "update kelas")
        data("4", "delete kelas")
        data("5", "keluar")
        print(tabel)
        pilihan = input("Masukan pilihan: ")
        if pilihan == "1":
            cread_kelas()
        elif pilihan == "2":
            lihat_kelas()
        elif pilihan == "3":
            update_kelas()
        elif pilihan == "4":
            hapus_kelas()
        elif pilihan == "5":
            print("Terima kasih dan sampai jumpa")
            return True
        else:
            print("maaf tidak ada pilihan")

def user():
    nama = input("Masukan Nama Anda: ")
    while True:
        print(f"Selamat Datang ({nama}) silahkan pilih pilihan anda")
        from prettytable import PrettyTable  

        masa = PrettyTable()
        masa.field_names = ["No", "Pilihan"]
        def date(no, pilihan):
            masa.add_row([no, pilihan])

        date("1", "Lihat kelas")
        date("2", "Pinjam kelas")
        date("3", "Keluar")
        print(masa)
        pilihan = input("Masukan pilihan: ")
        if pilihan == "1":
            lihat_kelas()
        elif pilihan == "2":
            pinjam_kelas()
        elif pilihan == "3":
            print("Terima kasih dan sampai jumpa")
            return True
        else:
            print("maaf tidak ada pilihan")

def cread_kelas():
    while True:
        lihat_kelas()
        no = input("Masukan nomor: ")
        nomor_kelas = input("Masukan Nomor Kelas: ")
        nama_kelas = input("Masukan Nama Kelas: ")
        waktu_kosong = input("Masukan Waktu Kosong: ")
        pinjaman_kelas(no, nomor_kelas, nama_kelas, waktu_kosong)
        print(table)
        lanjut = input("Mau tambah/tidak: ")
        if lanjut == "tambah":
            cread_kelas()
        elif lanjut == "tidak":
            return True
        else:
            print("program anda berhenti")

def lihat_kelas():
    print(table)

def update_kelas():
    while True:
        print(table)
        no = input("Masukkan Nomor Kelas yang ingin diupdate: ")
        for ubah in table._rows:
            if ubah[0] == no:
                nomor_kelas = input("Masukan Nomor Kelas baru: ")
                nama_baru = input("Masukkan Nama Kelas baru: ")
                waktu_baru = input("Masukkan Waktu Kosong baru: ")
                ubah[1] = nomor_kelas
                ubah[2] = nama_baru
                ubah[3] = waktu_baru
                print("Kelas berhasil diupdate!")
                print(table)
                return True
        else:
            print("Kelas tidak ditemukan.")

def hapus_kelas():
    while True:
        print(table)
        no = input("Masukkan Nomor Kelas yang ingin dihapus: ")
        for hapus in table._rows:
            if hapus[0] == no:
                table._rows.remove(hapus)
        print(table)
        return True


def pinjam_kelas():
    while True:
        print(table)
        no = input("Masukkan Nomor Kelas yang ingin dipinjam: ")
        for pinjam in table._rows:
            if pinjam[0] == no:
                print(f"Anda telah meminjam kelas ({pinjam[1]}) dengan nama ({pinjam[2]}) dan waktu ({pinjam[3]}.")
                table._rows.remove(pinjam)
                print("Kelas yang tersedia setelah peminjaman:")
                print(table)
                return True
            
login()