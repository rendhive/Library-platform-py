import platform

sys_info = platform.uname()
print("Informasi Sistem:")
for attr in sys_info:
    print(attr)

#Fungsi: Mencetak setiap atribut informasi sistem.
#Kondisi: Ketika Anda ingin melihat semua informasi sistem yang relevan.