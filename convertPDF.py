from PIL import Image

img1 = Image.open("p1.jpg").convert("RGB")
img2 = Image.open("p2.jpg").convert("RGB")

img1.save("resultat.pdf", save_all=True, append_images=[img2])
