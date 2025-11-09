import platform

if platform.system() == "Windows":
    print("Melakukan operasi khusus untuk Windows.")
else:
    print("Melakukan operasi pada sistem lain.")

#Fungsi: Menjalankan logika berbeda berdasarkan sistem operasi yang digunakan.
#Kondisi: Ketika Anda perlu menyesuaikan perilaku aplikasi tergantung pada OS.