from PIL import Image, ImageDraw, ImageFont

# TODO 0: Import library lain yang dibutuhkan

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open("umm.png")

# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert("L")

# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
direktoriFont = "arial.ttf"  # Ganti dengan path yang benar
size = 24
font = ImageFont.truetype(direktoriFont, size)
text = "Nama: Rangga Saputra Hari Pratama\nNIM: 202110370311182"
text_bbox = draw.textbbox((0, 0), text, font=font)
text_x = (gambarBW.width - text_bbox[2]) // 2
text_y = (gambarBW.height - text_bbox[3]) // 2
text_color = "blue"  # Ganti dengan warna yang diinginkan
draw.text((text_x, text_y), text, font=font, fill=text_color)

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save("HASILTUGAS1.jpg")

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()
