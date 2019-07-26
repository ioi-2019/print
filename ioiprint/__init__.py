import json
import os

PATH = os.path.dirname(os.path.realpath(__file__))

STATIC_PATH = os.path.join(PATH, 'static')
TEMPLATES_PATH = os.path.join(PATH, 'template')

MAX_NUM_OF_PAGES_FOR_CONTESTANTS = 12

PRINTER_FOR_ZONE = json.loads(os.getenv('PRINTERS_FOR_ZONES'))

DEFAULT_PRINTER = os.getenv('DEFAULT_PRINTER')

WEBSERVICE_URL = os.getenv('WEBSERVICE_URL')
CONTESTANT_DATA_ADDRESS_URL = 'http://{url}/contestant/{{ip}}/'.format(
    url=WEBSERVICE_URL)

PDF_UPLOAD_PATH = os.getenv('UPLOADS_DIRECTORY')

CUPS_SERVER_ADDRESS = os.getenv('CUPS_ADDRESS')
