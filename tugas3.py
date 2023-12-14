from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

# TODO: Buka gambar menggunakan Pillow.
gambar = Image.open("/content/umm.png")  # Ganti dengan path gambar Anda

# TODO: Ubah tingkat kecerahan menjadi 1.5 kali lipat dan tingkat kontras menjadi 1.2 kali lipat.
brightness_factor = 1.5
contrast_factor = 1.2

enhancer = ImageEnhance.Brightness(gambar)
gambar_brightness = enhancer.enhance(brightness_factor)

enhancer = ImageEnhance.Contrast(gambar_brightness)
gambar_brightness_contrast = enhancer.enhance(contrast_factor)

# TODO: Simpan gambar hasil edit dengan nama "brightness_contrast_image.jpg".
gambar_brightness_contrast.save("HASILTUGAS3.png")

# TODO: Tampilkan hasilnya
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(gambar)
axes[0].set_title("Gambar Asli")
axes[0].axis("off")

axes[1].imshow(gambar_brightness_contrast)
axes[1].set_title("Brightness & Contrast")
axes[1].axis("off")

plt.show()
