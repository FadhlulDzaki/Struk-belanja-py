import datetime

def format_rupiah(angka):
    return f"Rp{angka:,.0f}".replace(",", ".")

def dapatkan_kasir():
    now = datetime.datetime.now().time()
    if now < datetime.time(8, 0):
        return "Andi"
    elif now < datetime.time(16, 0):
        return "Budi"
    else:
        return "Cahya"

def buat_struk(daftar_belanja, total_bayar, nama_file, nama_kasir):
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = []
    lines.append("========================================")
    lines.append("           TOKO KELONTONG")
    lines.append("        Jl. Pahlawan No.9")
    lines.append(f"        Tanggal: {waktu}")
    lines.append(f"        Kasir: {nama_kasir}")
    lines.append("========================================")
    lines.append(f"{'Nama Barang':<15} {'Qty':>3} {'Harga':>10} {'Total':>12}")
    lines.append("----------------------------------------")

    for item in daftar_belanja:
        lines.append(f"{item['nama']:<15} {item['jumlah']:>3} {format_rupiah(item['harga']):>10} {format_rupiah(item['total']):>12}")

    lines.append("----------------------------------------")
    lines.append(f"{'TOTAL BAYAR':<28} {format_rupiah(total_bayar):>12}")
    lines.append("========================================")
    lines.append("     Terima kasih telah berbelanja!")
    lines.append("========================================")

    # Tampilkan di terminal
    for line in lines:
        print(line)

    # Simpan ke file
    with open(nama_file, "w") as file:
        for line in lines:
            file.write(line + "\n")
    print(f"\n>> Struk berhasil disimpan di: {nama_file}")

# Program utama
daftar_belanja = []
jumlah_barang = int(input("Masukkan jumlah item yang dibeli: "))

for i in range(jumlah_barang):
    print(f"\nItem ke-{i+1}")
    nama = input("Nama barang: ")
    jumlah = int(input("Jumlah: "))
    harga = float(input("Harga satuan (Rp): "))
    total = jumlah * harga
    daftar_belanja.append({
        "nama": nama,
        "jumlah": jumlah,
        "harga": harga,
        "total": total
    })

total_bayar = sum(item['total'] for item in daftar_belanja)
waktu_str = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
nama_kasir = dapatkan_kasir()
nama_file = f"Struk_TokoKelontong_{waktu_str}_Kasir-{nama_kasir}.txt"

buat_struk(daftar_belanja, total_bayar, nama_file, nama_kasir)
