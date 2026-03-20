import anvil.server
import anvil.media
from pyzbar import pyzbar
from PIL import Image


@anvil.server.callable
def read_barcodes(image):
  
  # Create a temporary file - from docs: https://anvil.works/docs/media/files_on_disk#media-object-to-temporary-file
  with anvil.media.TempFile(image) as file_name:
    # Read bar codes
    qrcodes = pyzbar.decode(Image.open(file_name))
  
  # Create a list to store the qr
  list_of_decodes = []
  
  for qrcode in qrcodes:

    # Decode the data
    qrcode_info = qrcode.data.decode('utf-8')
    
    # Add it to the list
    list_of_decodes.append(qrcode_info)
    
  return list_of_decodes
    