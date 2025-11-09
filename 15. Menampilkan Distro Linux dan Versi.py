import platform

if platform.system() == "Linux":
    distro = platform.linux_distribution()
    print("Distribusi dan Versi Linux:", distro)

#Fungsi: Mengambil informasi distribusi sistem Linux.
#Kondisi: Ketika aplikasi perlu mengidentifikasi opsi tertentu berdasarkan distribusi Linux.