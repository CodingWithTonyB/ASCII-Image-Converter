import datetime
import os

timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
output_filename = f"output_{timestamp}.png"
output_path = os.path.join(r"C:\Users\Crypt\Documents\Code\ASCII\ASCII-Image-Converter\outputs/", output_filename)