import os
import colorama

kategori = []
pendapatan = []
pengeluaran = []


# Fungsi untuk menampilkan menu utama
def main():
    try:
        buatKategori()
    except FileNotFoundError:
        file = open("kategori.csv", "w")
        file.close
    os.system("cls")
    print(
        colorama.Fore.GREEN
        + "=================================================================="
    )
    print("Selamat Datang di Finance Manager")
    print("1. Mencatat Data Keuangan")
    if len(kategori) == 0:
        print(colorama.Fore.LIGHTBLACK_EX + "(Buat Kategori untuk mengakses menu ini)")
        print(colorama.Fore.LIGHTBLACK_EX + "2. Melihat Data Keuangan")
    else:
        print("2. Melihat Data Keuangan")
    print(colorama.Fore.GREEN + "3. Keluar")
    print(colorama.Fore.GREEN + "4. Reset Data Keuangan")
    print("==================================================================")
    print(
        colorama.Fore.LIGHTBLACK_EX
        + "(TIPS: Buat Kategori terlebih dahulu sebelum mencatat data keuangan untuk memberikan konteks pada data)",
        end="\n\n",
    )
    action = inputAction()

    if action == 1:
        menuInputKeuangan()
    elif action == 2:
        if len(kategori) == 0:
            kategori.clear()
            main()
        else:
            menuShowKeuangan()
    elif action == 3:  # action == 3
        os.system("cls")
        print(colorama.Fore.GREEN + "Terima kasih telah menggunakan Finance Manager!")
        os.system("pause")
        os.system("cls")
        return 0
    elif action == 4:
        action = input(
            colorama.Fore.RED + "Apakah Anda yakin ingin mereset data keuangan?(y/n): "
        )
        if action == "y":
            reset()
            print(colorama.Fore.GREEN + "Data keuangan berhasil direset!")
            os.system("pause")
            kategori.clear()
            main()
        elif action == "n":
            kategori.clear()
            main()
        else:
            print(colorama.Fore.RED + "Input tidak valid!")
            os.system("pause")
            kategori.clear()
            main()
    else:
        kategori.clear()
        main()


# Fungsi untuk mengambil input dari user saat memilih menu
def inputAction():
    try:
        action = int(input(colorama.Fore.GREEN + "Pilih aksi yang Anda inginkan: "))
        return action
    except ValueError:
        print(colorama.Fore.RED + "Input tidak valid! Masukkan angka.")
        return inputAction()


# Fungsi untuk menampilkan menu Catat Data Keuangan
def menuInputKeuangan():
    os.system("cls")
    print(
        colorama.Fore.GREEN
        + "=================================================================="
    )
    if len(kategori) == 0:
        print("Anda belum memiliki kategori!")
        print("Silahkan buat kategori terlebih dahulu.")
        print("1. Buat Kategori")
        print("2. Kembali")
        print(
            "==================================================================",
            end="\n\n",
        )
        action = inputAction()

        if action == 1:
            membuatKategori()
            kategori.clear()
            main()
        elif action == 2:
            kategori.clear()
            main()
        else:
            menuInputKeuangan()
    else:
        print("Catat Keuangan Anda")
        print("1. Catat Pemasukan")
        print("2. Catat Pengeluaran")
        print("3. Buat Kategori Baru")
        print("4. Kembali")
        print(
            "==================================================================",
            end="\n\n",
        )
        action = inputAction()

        if action == 1:
            loop = "y"
            while loop == "y":
                mencatatPendapatan()
                loop = input("Ingin mencatat lagi?(y/n): ")
            menuInputKeuangan()
        elif action == 2:
            loop = "y"
            while loop == "y":
                mencatatPengeluaran()
                loop = input("Ingin mencatat lagi?(y/n): ")
            menuInputKeuangan()
        elif action == 3:
            loop = "y"
            while loop == "y":
                membuatKategori()
                loop = input("Ingin membuat kategori baru lagi?(y/n): ")
            menuInputKeuangan()
        elif action == 4:
            kategori.clear()
            main()
        else:
            menuInputKeuangan()


# Fungsi untuk menampilkan menu Melihat Data Keuangan
def menuShowKeuangan():
    os.system("cls")
    print(
        colorama.Fore.GREEN
        + "=================================================================="
    )
    print("Lihat Keuangan Anda")
    print("1. Lihat Jumlah Uang Anda Saat ini")
    print("2. Lihat Data Pendapatan")
    print("3. Lihat Data Pengeluaran")
    print("4. Lihat Rasio Pengeluaran terhadap Pendapatan")
    print("5. Kembali")
    print(
        "==================================================================",
        end="\n\n",
    )
    action = inputAction()

    if action == 1:
        try:
            buatPendapatan(0)
        except:
            file = open("pendapatan.csv", "w")
            file.close
        try:
            buatPengeluaran(0)
        except:
            file = open("pengeluaran.csv", "w")
            file.close
        os.system("cls")
        print(f"Uang Anda saat ini adalah Rp{sumPendapatan() - sumPengeluaran()}")
        os.system("pause")
        pendapatan.clear()
        menuShowKeuangan()
    elif action == 2:
        os.system("cls")
        print(
            colorama.Fore.GREEN
            + "=================================================================="
        )
        print("Lihat jumlah data pendapatan berdasarkan: ")
        print("1. Bulan")
        print("2. Tahun")
        print("3. Kategori")
        print(
            "==================================================================",
            end="\n\n",
        )
        action = inputAction()

        if action == 1:
            try:
                buatPendapatan(1)
            except:
                file = open("pendapatan.csv", "w")
                file.close
            os.system("cls")
            print(f"Total pendapatan pada bulan tersebut Rp{sumPendapatan()}")
            print(f"Rata-rata pendapatan pada bulan tersebut Rp{averagePendapatan()}")
            print(f"Pendapatan terendah pada bulan tersebut Rp{minPendapatan()}")
            print(f"Pendapatan tertinggi pada bulan tersebut Rp{maxPendapatan()}")
            os.system("pause")
            pendapatan.clear()
        elif action == 2:
            try:
                buatPendapatan(2)
            except:
                file = open("pendapatan.csv", "w")
                file.close
            os.system("cls")
            print(f"Total pendapatan pada tahun tersebut Rp{sumPendapatan()}")
            print(f"Rata-rata pendapatan pada tahun tersebut Rp{averagePendapatan()}")
            print(f"Pendapatan terendah pada tahun tersebut Rp{minPendapatan()}")
            print(f"Pendapatan tertinggi pada tahun tersebut Rp{maxPendapatan()}")
            os.system("pause")
            pendapatan.clear()
        elif action == 3:
            try:
                buatPendapatan(3)
            except:
                file = open("pendapatan.csv", "w")
                file.close
            os.system("cls")
            print(f"Total pendapatan pada kategori tersebut Rp{sumPendapatan()}")
            print(
                f"Rata-rata pendapatan pada kategori tersebut Rp{averagePendapatan()}"
            )
            print(f"Pendapatan terendah pada kategori tersebut Rp{minPendapatan()}")
            print(f"Pendapatan tertinggi pada kategori tersebut Rp{maxPendapatan()}")
            os.system("pause")
            pendapatan.clear()

        menuShowKeuangan()
    elif action == 3:
        os.system("cls")
        print(
            colorama.Fore.GREEN
            + "=================================================================="
        )
        print("Lihat jumlah data pengeluaran berdasarkan: ")
        print("1. Bulan")
        print("2. Tahun")
        print("3. Kategori")
        print(
            "==================================================================",
            end="\n\n",
        )
        action = inputAction()

        if action == 1:
            try:
                buatPengeluaran(1)
            except:
                file = open("pengeluaran.csv", "w")
                file.close
            os.system("cls")
            print(f"Total pengeluaran pada bulan tersebut Rp{sumPengeluaran()}")
            print(f"Rata-rata pengeluaran pada bulan tersebut Rp{averagePengeluaran()}")
            print(f"Pengeluaran terendah pada bulan tersebut Rp{minPengeluaran()}")
            print(f"Pengeluaran tertinggi pada bulan tersebut Rp{maxPengeluaran()}")
            os.system("pause")
            pengeluaran.clear()
        elif action == 2:
            try:
                buatPengeluaran(2)
            except:
                file = open("pengeluaran.csv", "w")
                file.close
            os.system("cls")
            print(f"Total pengeluaran pada tahun tersebut Rp{sumPengeluaran()}")
            print(f"Rata-rata pengeluaran pada tahun tersebut Rp{averagePengeluaran()}")
            print(f"Pengeluaran terendah pada tahun tersebut Rp{minPengeluaran()}")
            print(f"Pengeluaran tertinggi pada tahun tersebut Rp{maxPengeluaran()}")
            os.system("pause")
            pengeluaran.clear()
        elif action == 3:
            try:
                buatPengeluaran(3)
            except:
                file = open("pengeluaran.csv", "w")
                file.close
            os.system("cls")
            print(f"Total pengeluaran pada kategori tersebut Rp{sumPengeluaran()}")
            print(
                f"Rata-rata pengeluaran pada kategori tersebut Rp{averagePengeluaran()}"
            )
            print(f"Pengeluaran terendah pada kategori tersebut Rp{minPengeluaran()}")
            print(f"Pengeluaran tertinggi pada kategori tersebut Rp{maxPengeluaran()}")
            os.system("pause")
            pengeluaran.clear()

        menuShowKeuangan()
    elif action == 4:
        try:
            buatPendapatan(0)
        except:
            file = open("pendapatan.csv", "w")
            file.close
        try:
            buatPengeluaran(0)
        except:
            file = open("pengeluaran.csv", "w")
            file.close
        os.system("cls")
        print(
            f"Rasio Pengeluaran dan Pendapatan Anda saat ini adalah {round(rasio())}%"
        )
        os.system("pause")
        pendapatan.clear()
        menuShowKeuangan()
    elif action == 5:
        kategori.clear()
        main()


# Fungsi untuk membuat kategori baru
def membuatKategori():
    file = open("kategori.csv", "a")
    namaKategori = input("Masukan nama kategori: ")
    file.write(namaKategori + ",")
    file.close()


# Fungsi untuk mengisi array kategori
def buatKategori():
    file = open("kategori.csv", "r")
    items = file.readline().split(",")
    for item in items:
        if item != "":
            kategori.append(item)
    file.close()


# Fungsi untuk memilih kategori yang tersedia
def pilihKategori():
    print(colorama.Fore.GREEN)
    print("Kategori yang tersedia: ")
    for i in range(len(kategori)):
        print(f"{i+1}. {kategori[i]}")
    try:
        pilihan = int(input("Masukan kategori yang ingin dipilih: "))
        if pilihan > len(kategori) or pilihan - 1 < 0:
            return pilihKategori()
        else:  # pilihan <= len(kategori) and pilihan - 1 >= 0
            return pilihan - 1
    except ValueError:
        print(colorama.Fore.RED + "Input tidak valid! Masukkan angka.")
        return pilihKategori()


# Fungsi untuk mencatat pendapatan yang diinput user ke file csv
def mencatatPendapatan():
    file = open("pendapatan.csv", "a")

    tanggal = input("Masukan tanggal(DD): ")
    bulan = input("Masukan bulan(MM): ")
    tahun = input("Masukan tahun(YYYY): ")
    uang = input("Masukan pendapatan(Rp tanpa titik): ")
    indeksKategori = pilihKategori()

    file.write(tanggal + ",")
    file.write(bulan + ",")
    file.write(tahun + ",")
    file.write(uang + ",")
    file.write(kategori[indeksKategori] + ",")
    file.write("\n")
    file.close()


# Fungsi untuk mencatat pengeluaran yang diinput user ke file csv
def mencatatPengeluaran():
    file = open("pengeluaran.csv", "a")

    tanggal = input("Masukan tanggal(DD): ")
    bulan = input("Masukan bulan(MM): ")
    tahun = input("Masukan tahun(YYYY): ")
    pengeluaran = input("Masukan pengeluaran(Rp tanpa titik): ")
    indeksKategori = pilihKategori()

    file.write(tanggal + ",")
    file.write(bulan + ",")
    file.write(tahun + ",")
    file.write(pengeluaran + ",")
    file.write(kategori[indeksKategori] + ",")
    file.write("\n")
    file.close()


# Fungsi untuk mengisi array pendapatan
def buatPendapatan(jenis):
    file = open("pendapatan.csv", "r")

    if jenis == 0:
        for line in file:
            pendapatan.append(line.split(",")[3])
    elif jenis == 1:
        dataBulan = input("Masukkan Bulan(MM): ")
        dataTahun = input("Masukkan Tahun(YYYY): ")
        for line in file:
            if dataBulan in line.split(",")[1] and dataTahun in line.split(",")[2]:
                pendapatan.append(line.split(",")[3])
    elif jenis == 2:
        dataTahun = input("Masukkan Tahun(YYYY): ")
        for line in file:
            if dataTahun in line.split(",")[2]:
                pendapatan.append(line.split(",")[3])
    elif jenis == 3:
        indeksKategori = pilihKategori()
        for line in file:
            if kategori[indeksKategori] in line:
                pendapatan.append(line.split(",")[3])

    file.close()


# Fungsi untuk mengisi array pengeluaran
def buatPengeluaran(jenis):
    file = open("pengeluaran.csv", "r")

    if jenis == 0:
        for line in file:
            pengeluaran.append(line.split(",")[3])
    elif jenis == 1:
        dataBulan = input("Masukkan Bulan(MM): ")
        dataTahun = input("Masukkan Tahun(YYYY): ")
        for line in file:
            if dataBulan in line.split(",")[1] and dataTahun in line.split(",")[2]:
                pengeluaran.append(line.split(",")[3])
    elif jenis == 2:
        dataTahun = input("Masukkan Tahun(YYYY): ")
        for line in file:
            if dataTahun in line.split(",")[2]:
                pengeluaran.append(line.split(",")[3])
    elif jenis == 3:
        indeksKategori = pilihKategori()
        for line in file:
            if kategori[indeksKategori] in line:
                pengeluaran.append(line.split(","[3]))

    file.close()


def sumPendapatan():
    sum = 0
    for i in pendapatan:
        sum += int(i)
    return sum


def sumPengeluaran():
    sum = 0
    for i in pengeluaran:
        sum += int(i)
    return sum


def averagePendapatan():
    try:
        average = sumPendapatan() / len(pendapatan)
    except ZeroDivisionError:
        average = 0
    return average


def averagePengeluaran():
    try:
        average = sumPengeluaran() / len(pengeluaran)
    except ZeroDivisionError:
        average = 0
    return average


def minPendapatan():
    try:
        min = pendapatan[0]
    except IndexError:
        min = 0
    for i in pendapatan:
        if i < min:
            min = i
    return min


def minPengeluaran():
    try:
        min = pengeluaran[0]
    except IndexError:
        min = 0
    for i in pengeluaran:
        if i < min:
            min = i
    return min


def maxPendapatan():
    try:
        max = pendapatan[0]
    except IndexError:
        max = 0
    for i in pendapatan:
        if i > max:
            max = i
    return max


def maxPengeluaran():
    try:
        max = pengeluaran[0]
    except IndexError:
        max = 0
    for i in pengeluaran:
        if i > max:
            max = i
    return max


def rasio():
    try:
        rasio = (sumPengeluaran() / sumPendapatan()) * 100
    except ZeroDivisionError:
        rasio = 0
    return rasio


def reset():
    try:
        os.remove("kategori.csv")
    except:
        print(colorama.Fore.RED + "Kategori tidak dapat dihapus(Not Found)")
    try:
        os.remove("pendapatan.csv")
    except FileNotFoundError:
        print(colorama.Fore.RED + "Pendapatan tidak dapat dihapus(Not Found)")
    try:
        os.remove("pengeluaran.csv")
    except FileNotFoundError:
        print(colorama.Fore.RED + "Pengeluaran tidak dapat dihapus(Not Found)")


main()
