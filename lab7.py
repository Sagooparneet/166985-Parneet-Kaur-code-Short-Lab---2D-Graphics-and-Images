from PIL import Image
import numpy as np
import math

orig = Image.open("photo_original.png").convert("RGB")
comp = Image.open("photo_jpeg50.jpg").convert("RGB").resize(orig.size)

A = np.asarray(orig).astype(np.float32)
B = np.asarray(comp).astype(np.float32)

mse = np.mean((A - B) ** 2)
psnr = 10 * math.log10((255 ** 2) / mse) if mse > 0 else float("inf")

print("MSE:", mse)
print("PSNR:", psnr, "dB")