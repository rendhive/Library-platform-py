import platform

with open('system_info.txt', 'w') as f:
    f.write(f"Sistem: {platform.system()}\n")
    f.write(f"Versi: {platform.version()}\n")
    f.write(f"Python: {platform.python_version()}\n")
print("Informasi sistem telah disimpan ke 'system_info.txt'.")


#Fungsi: Menyimpan informasi sistem ke dalam file teks.
#Kondisi: Ketika Anda ingin melakukan pencatatan atau log informasi sistem.