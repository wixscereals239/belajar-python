#Sebagai Mesin ATM
import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input('Masukan pin Anda dengan benar: '))
    trial = 0
    while (id != int(atm.cekPin()) and trial < 3):
        id = int(input('Pin Anda salah silakan masukan kembali: '))
        trial += 1
        if trial == 3:
            print("Error. Silakan ambil kartu dan coba lagi..")
            exit()
    while True:
        print('\n Selamat datang di ATM..')
        print('\n 1 - Cek Saldo \n 2 - Tarik Tunai \n 3 - Setor Tunai \n 4 - Ganti Pin \n 5 - Keluar')
        selectmenu = int(input('\n Silakan pilih menu: '))
        if selectmenu == 1:
            print('\n Saldo Anda sekarang: Rp. ' + str(atm.cekSaldo()) + '\n')
            kembali = input('Apakah ingin transaksi ulang? Y/N : ')
            if kembali == 'y':
                break
            else:
                print('Terima kasih telah memakai ATM..')
                exit() 
        elif selectmenu == 2:
            nominal = float(input('Masukkan Nominal Saldo: '))
            verify_tarikTunai = input('Konfirmasi: Anda akan melakukan tarik tunai dengan nominal tersebut? Y/N ' + str(nominal) + " ") 
            print('Saldo Awal Anda Adalah: Rp. ' + str(atm.cekSaldo()) + " ")
            if verify_tarikTunai == 'y':
                if nominal < atm.cekSaldo():
                    atm.tarikSaldo(nominal)
                    print('Tarik tunai Berhasil!!!')
                    print('Saldo anda Sekarang: Rp. ' + str(atm.cekSaldo()) + " ")
                    kembali = input('Apakah ingin transaksi ulang? Y/N : ')
                    if kembali == 'y':
                        break
                    else:
                        print('Terima kasih telah memakai ATM..')
                        exit() 
                else:
                    print('Maaf, Saldo Anda Tidak Cukup Untuk Melakukan Debet!')
                    print('Silakan Lakukan Penambahan nominal Saldo')
                    break
            else:
                print('Transaksi dibatalkan')
                break
        elif selectmenu == 3:
            nominal = float(input('Masukkan nominal saldo: '))
            verify_setorTunai = input('Konfirmasi: Anda akan melakukan penyimpanan dengan nominal tersebut? Y/N ' + str(nominal) +" ")
            if verify_setorTunai == 'Y':
                atm.setorSaldo(nominal)
                print('Saldo Anda sekarang adalah: Rp. ' + str(atm.cekSaldo()) + "\n")
            else:
                print('Transaksi dibatalkan')
                break
        elif selectmenu == 4:
            verify_pin = int(input('Masukan pin lama Anda: '))
            while verify_pin != int(atm.cekPin()):
                print('Pin anda salah, Silahkan masukkan dengan benar: ')
            update_pin = int(input('Silakan masukan pin baru: '))
            print('Pin Anda berhasil diganti')
            verify_pinBaru = int(input('Coba masukkan pin baru: '))
            if verify_pin == update_pin:
                print('Pin baru anda sukses')
            else:
                print('Maaf, pin Anda salah')
        elif selectmenu == 5:
            print('Resi tercetak otomatis. \n Harap simpan tanda terima ini \n Sebagai bukti transaksi anda')
            print('No. rekord: ', random.randint(100000, 1000000))
            print('Saldo akhir: ', atm.cekSaldo())
            print('Terima kasih')
            exit()
        else:
            print('Error. Menu tidak tersedia')