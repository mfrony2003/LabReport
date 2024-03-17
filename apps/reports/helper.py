import barcode 
from io import BytesIO
from barcode.writer import SVGWriter

def createBarCodes(reportId):
    rv = BytesIO()
    number = reportId+5901234123457 
    b = str(number)
    # Write the barcode to a binary stream
    rv = BytesIO()
    code = barcode.get('code128', b, writer=SVGWriter())
    code.write(rv)

    rv.seek(0)
    # get rid of the first bit of boilerplate
    rv.readline()
    rv.readline()
    rv.readline()
    rv.readline()
    # read the svg tag into a string
    svg = rv.read()
    return svg

import os
import base64

def image_as_base64(image_file, format='png'):
    """
    :param `image_file` for the complete path of image.
    :param `format` is format for image, eg: `png` or `jpg`.
    """
    if not os.path.isfile(image_file):
        return None
    
    encoded_string = ''
    with open(image_file, 'rb') as img_f:
        encoded_string = base64.b64encode(img_f.read())
    return "data:image/jpeg;base64," + encoded_string.decode('utf-8')


