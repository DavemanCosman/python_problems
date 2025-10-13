import pytesseract
from pdf2image import convert_from_path
from PIL import Image

file_path = r"C:\Users\david\Documents\Snowflake\SnowPro Core Test Prep.pdf"

# IMPROVEMENT: let user select the file from browser
pages = convert_from_path(file_path, dpi=300, first_page=1, last_page=1)[0] 

text = pytessract.image_to_string(first_page)

print(text)
