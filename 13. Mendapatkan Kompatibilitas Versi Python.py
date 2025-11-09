import platform

if platform.python_version_tuple()[0] == '3':
    print("Menggunakan Python versi 3.")
else:
    print("Menggunakan Python versi yang lebih lama.")

#Fungsi: Memeriksa apakah versi Python yang digunakan adalah 3.x.
#Kondisi: Untuk memastikan bahwa fitur yang digunakan tersedia di versi Python yang sesuai.