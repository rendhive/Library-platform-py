# Library-platform-py
Platform — Informasi Sistem dan Lingkungan Python

Modul platform menyediakan cara yang sederhana untuk mendapatkan informasi tentang sistem operasi, versi, arsitektur mesin, dan detail lingkungan Python. Berguna ketika Anda membuat aplikasi yang perlu menyesuaikan perilaku berdasarkan OS atau spesifikasi sistem.


---

Apa yang Bisa Dilakukan platform?

• Mengetahui jenis OS yang digunakan (Windows, Linux, macOS)
• Mendapatkan versi OS
• Mengecek arsitektur CPU
• Melihat implementasi dan versi Python
• Mengambil detail mesin seperti nama perangkat


---

Contoh Dasar

import platform

print(platform.system())      # Nama OS
print(platform.release())     # Versi OS
print(platform.version())     # Detail versi lengkap


---

Informasi Arsitektur

import platform

print(platform.machine())     # Contoh: x86_64, arm64
print(platform.architecture()) # Info 32-bit / 64-bit


---

Informasi Python

import platform

print(platform.python_version())         # Versi Python
print(platform.python_implementation())  # CPython, PyPy, dll


---

Informasi Lengkap Sistem

import platform

print(platform.uname())  # Mengembalikan informasi lengkap dalam bentuk struktur

Hasilnya mencakup: system, node, release, version, machine, processor.


---

Kapan Menggunakan platform?

• Saat aplikasi perlu menyesuaikan fitur berdasarkan OS
• Ketika Anda membuat installer, logger, atau diagnosa sistem
• Saat debugging untuk mengetahui lingkungan pengguna
• Untuk menampilkan informasi versi pada aplikasi CLI


---

Modul platform memberikan akses cepat dan rapi ke informasi sistem tanpa setup tambahan. Cocok untuk program yang butuh penyesuaian lintas platform.
