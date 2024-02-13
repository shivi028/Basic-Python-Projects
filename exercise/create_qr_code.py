import pyqrcode
import png
from pyqrcode import QRCode


# s = "https://www.linkedin.com/in/shivi-tiwari-7a669b289/";
# url = pyqrcode.create(s);
# url.png('LinkedIn_profile_QR.png', scale=6);

content = 'kesa lga qr scan krke';
url = pyqrcode.create(content);
url.svg('content_QR.svg', scale=8);