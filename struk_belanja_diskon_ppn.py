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

def hitung_diskon(total):
    now = datetime.datetime.now().time()
    if now >= datetime.time(18, 0):  # Diskon aktif mulai jam 18:00
        return total * 0.10
    else:
        return 0.0

def buat_struk(daftar_belanja, total_belanja, diskon, pajak, total_bayar, nama_file, nama_kasir):
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = []
    lines.append("========================================")
    lines.append("           TOKO KELONTONG")
    lines.append("        Jl. Pahlawan No.9")
    lines.append(f"        Tanggal: {waktu}")
    lines.append(f"        Kasir  : {nama_kasir}")
    lines.append("========================================")
    lines.append(f"{'Nama Barang':<15} {'Qty':>3} {'Harga':>10} {'Total':>12}")
    lines.append("----------------------------------------")

    for item in daftar_belanja:
        lines.append(f"{item['nama']:<15} {item['jumlah']:>3} {format_rupiah(item['harga']):>10} {format_rupiah(item['total']):>12}")

    lines.append("----------------------------------------")
    lines.append(f"{'Subtotal':<28} {format_rupiah(total_belanja):>12}")
    if diskon > 0:
        lines.append(f"{'Diskon 10% (promo)':<28} -{format_rupiah(diskon):>11}")
    else:
        lines.append(f"{'Diskon':<28} {format_rupiah(0):>12}")
    lines.append(f"{'Pajak 5%':<28} +{format_rupiah(pajak):>11}")
    lines.append(f"{'TOTAL BAYAR':<28} {format_rupiah(total_bayar):>12}")
    lines.append("========================================")
    lines.append("     Terima kasih telah berbelanja!")
    lines.append("========================================")

    # Tampilkan ke terminal
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

total_belanja = sum(item['total'] for item in daftar_belanja)
diskon = hitung_diskon(total_belanja)
setelah_diskon = total_belanja - diskon
pajak = setelah_diskon * 0.05  # <== PAJAK DISESUAIKAN DI SINI
total_bayar = setelah_diskon + pajak

waktu_str = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
nama_kasir = dapatkan_kasir()
nama_file = f"Struk_TokoKelontong_{waktu_str}_Kasir-{nama_kasir}.txt"

buat_struk(daftar_belanja, total_belanja, diskon, pajak, total_bayar, nama_file, nama_kasir)
