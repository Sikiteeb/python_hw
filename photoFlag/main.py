from PIL import Image, ImageDraw, ImageFont


image = Image.open("photo.jpeg")

estonian_flag = Image.open("estonian_flag.jpeg")

# Convert both images to RGBA and RGB modes
image = image.convert("RGBA")
estonian_flag = estonian_flag.convert("RGB")

# Resize the flag to match the size of the image
estonian_flag = estonian_flag.resize(image.size)

opacity = 0.6

# Create a transparent layer with the same size as the image
transparent_layer = Image.new('RGBA', image.size, (0, 0, 0, 0))

# Paste the Estonian flag onto the transparent layer with opacity
transparent_layer.paste(estonian_flag, (0, 0))
transparent_layer.putalpha(int(255 * opacity))

# Paste the transparent layer onto the image
result = Image.alpha_composite(image, transparent_layer)

result.save("photo_with_estonian_flag.png")

# Load the image
image = Image.open("photo_with_estonian_flag.png")

# Create a drawing context
draw = ImageDraw.Draw(image)

# Define the text to draw
text = "Sigrid Hanni"

# Define the font and size
font = ImageFont.truetype("Arial.ttf", 69)

# Get the size of the text
text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]

# Define the position of the text (bottom right corner)
x = image.width - text_width - 20
y = image.height - text_height - 30

# Draw the text
draw.text((x, y), text, font=font, fill=(46, 46, 46))
# Save the result
image.save("photo_with_name.png")
