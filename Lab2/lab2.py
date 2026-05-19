from PIL import Image
from pathlib import Path

paths = ["photo.jpg", "screenshot.png", "logo.png"]

for name in paths:
    path = Path(name)

    img = Image.open(path)

    width, height = img.size
    channels = len(img.getbands())

    compressed = path.stat().st_size

    raw_estimate = width * height * channels  # assumes 8 bits per channel

    print("\nFile:", name)
    print("Format:", img.format)
    print("Mode:", img.mode)
    print("Dimensions:", width, "x", height)
    print("Channels:", channels)
    print("Compressed size:", compressed, "bytes")
    print("Estimated uncompressed size:", raw_estimate, "bytes")
    print("Approx compression ratio:", round(raw_estimate / compressed, 2))