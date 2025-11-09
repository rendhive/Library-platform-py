import platform

if hasattr(platform, 'virtual_environment'):
    print("Virtual Environment:", platform.virtual_environment)
else:
    print("Tidak dalam Virtual Environment.")

#Fungsi: Menentukan apakah skrip dijalankan dalam virtual environment.
#Kondisi: Ketika Anda perlu mengkonfigurasi perilaku aplikasi tergantung pada apakah dijalankan di dalam virtual environment atau tidak.