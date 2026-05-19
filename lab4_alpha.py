from PIL import Image, ImageDraw

# canvas size
W, H = 400, 250

# background (blue-ish)
background = Image.new("RGB", (W, H), (30, 65, 120))

# transparent foreground layer
foreground = Image.new("RGBA", (W, H), (0, 0, 0, 0))

draw = ImageDraw.Draw(foreground)

# draw semi-transparent rectangle
draw.rectangle((80, 50, 320, 200), fill=(255, 80, 40, 128))

# combine images using alpha compositing
combined = Image.alpha_composite(background.convert("RGBA"), foreground)

# save output
combined.save("alpha_composite.png")

print("Image saved successfully!")