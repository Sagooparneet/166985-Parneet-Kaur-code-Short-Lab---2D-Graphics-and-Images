from PIL import Image

img = Image.open("camera_photo.jpg")

clean = Image.new(img.mode, img.size)
clean.putdata(list(img.getdata()))

clean.save("camera_photo_metadata_stripped.jpg")

print("Saved metadata-stripped copy.")