from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

now = datetime.now().strftime("%d %B %Y")
name_text = "Dr. Halid Hasan, M.STRAT.HRM."  # Replace with signer's name
roles_text = "Pembantu Direktur II"  # Replace with signer's roles
footnote = f"Signed at {now}" # The Fotnote

name_font = ImageFont.load_default(16)
roles_font = ImageFont.load_default(14)
footnote_font = ImageFont.load_default(12)

# Load your logo image
logo = Image.open("assets/logo.jpeg")  # Adjust file path
# font = ImageFont.load_default(16)  # Load the default system font

logo.thumbnail((96, 96))

name_width = name_font.getlength(name_text)  # Get width of roles text
roles_width = roles_font.getlength(roles_text)
footnote_width = footnote_font.getlength(footnote)
total_content_width = max(name_width, roles_width, footnote_width)  # Choose wider element width

padding = 24 + 96 + 8 + 20  # 96 is the size of image, 8 is the begin x of image paste see line  38, 20 is padding of image and text, see line 40
canvas_height = 125 # Adjust as needed
canvas_width = total_content_width + padding


canvas = Image.new("RGBA", (int(canvas_width), canvas_height), (255, 255, 255, 255))  # White background

draw = ImageDraw.Draw(canvas)

# Paste logo at desired position
logo_x = 8  # Adjust as needed
logo_y = 8  # Adjust as needed
canvas.paste(logo, (logo_x, logo_y))

text_x = logo_x + logo.width + 20  # Adjust spacing as needed
text_y = 8  # Adjust as needed
draw.text((text_x, text_y), name_text, font=name_font, fill=(0, 0, 0))
draw.text((text_x, text_y + 24), roles_text, font=roles_font, fill=(0, 0, 0))
draw.text((text_x, text_y + 24 + 48), footnote, font=footnote_font, fill=(0, 0, 0))


canvas.save("assets/digital_stamp.png", save_all=True)