from PIL import Image, ImageDraw, ImageFilter

xmb_icon_size = (512, 512)
style = Image.open("mask-style.png")
icon = Image.open("game.jpg").resize(xmb_icon_size)
cover = Image.open("mask.jpg").resize(xmb_icon_size).convert("L")

mask = style.copy()
mask.paste(icon, (0, 0), cover) # Apply mask on style according to the cover(B&W photo)
mask.save("result.png")