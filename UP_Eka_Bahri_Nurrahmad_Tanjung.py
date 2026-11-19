# Program Penghitungan Biaya Parkir Kendaraan
# Berdasarkan ketentuan pada studi kasus

print("=== APLIKASI PEMBAYARAN PARKIR KAMPUS ===")

# 5. Perulangan untuk memproses beberapa kendaraan
jumlah_kendaraan = int(input("Masukkan jumlah kendaraan yang ingin diproses: "))
total_pendapatan = 0

for i in range(1, jumlah_kendaraan + 1):
    print(f"\n--- Kendaraan ke-{i} ---")
    
    # 1. Input Data: Jenis kendaraan dan lama parkir
    jenis = input("Masukkan jenis kendaraan (motor / mobil / bus): ").lower()
    lama_parkir = int(input("Masukkan lama parkir (dalam jam): "))
    
    # 2. Pilih Tarif menggunakan percabangan
    tarif_per_jam = 0
    if jenis == "motor" or jenis == "sepeda motor":
        tarif_per_jam = 2000
        nama_kendaraan = "Sepeda Motor"
    elif jenis == "mobil":
        tarif_per_jam = 5000
        nama_kendaraan = "Mobil"
    elif jenis == "bus":
        tarif_per_jam = 10000
        nama_kendaraan = "Bus"
    else:
        print("Jenis kendaraan tidak valid! Mengabaikan kendaraan ini.")
        continue

    # 3. Hitung Biaya dasar berdasarkan lama parkir
    biaya_dasar = tarif_per_jam * lama_parkir
    
    # 4. Cek Biaya Tambahan (jika lama parkir > 5 jam, tambah Rp5.000)
    biaya_tambahan = 0
    if lama_parkir > 5:
        biaya_tambahan = 5000
        
    # Total biaya untuk kendaraan ini
    total_biaya = biaya_dasar + biaya_tambahan
    total_pendapatan += total_biaya
    
    # 6. Tampilkan Hasil (Struk Parkir per kendaraan)
    print("\n--- STRUK PARKIR ---")
    print(f"Jenis Kendaraan  : {nama_kendaraan}")
    print(f"Lama Parkir      : {lama_parkir} jam")
    print(f"Tarif per Jam    : Rp {tarif_per_jam:,}")
    print(f"Biaya Dasar      : Rp {biaya_dasar:,}")
    print(f"Biaya Tambahan   : Rp {biaya_tambahan:,} (Jika > 5 jam)")
    print(f"Total Bayar      : Rp {total_biaya:,}")
    print("--------------------")

# Menampilkan total pembayaran seluruh kendaraan
print("\n========================================")
print(f"TOTAL Keseluruhan Pendapatan Parkir: Rp {total_pendapatan:,}")
print("========================================")