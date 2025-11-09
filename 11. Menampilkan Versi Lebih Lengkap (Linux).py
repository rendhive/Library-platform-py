import platform

if platform.system() == "Linux":
    linux_version = platform.linux_distribution()
    print("Versi Linux:", linux_version)

#Fungsi: Menampilkan versi distribusi Linux yang sedang digunakan.
#Kondisi: Ketika Anda ingin menyesuaikan aplikasi untuk distribusi Linux tertentu.