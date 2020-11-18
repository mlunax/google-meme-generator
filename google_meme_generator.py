from PIL import Image, ImageDraw, ImageFont

im = Image.open("source.png").convert("RGBA")
txt = Image.new("RGBA", im.size, (255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text(
    (160, 27),
    "Rust",
    font=ImageFont.truetype("LiberationSans-Regular.ttf", 16),
    fill=(0, 0, 0, 255),
)
d.text(
    (282, 170),
    "Examples of bad programming languages",
    font=ImageFont.truetype("LiberationSans-BoldItalic.ttf", 16),
    fill=(26, 13, 171, 255),
)
out = Image.alpha_composite(im, txt)
out.show()
# out.save("test.PNG", "PNG")