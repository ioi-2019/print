import os
import random
import string

from flask import Flask, request

from ioiprint import DEFAULT_PRINTER, PDF_UPLOAD_PATH, PRINTER_FOR_ZONE
from ioiprint.modifier import make_contestant_pdf, make_translation_pdf#, make_cms_request_pdf
from ioiprint.contestant_data import get_contestant_data
from ioiprint.print import print_file
from ioiprint.utils import create_temp_directory, download

app = Flask('ioiprint')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['pdf']
    random_file_name = ''.join(
        random.choice(string.ascii_uppercase + string.digits)
        for _ in range(10)
    ) + '.pdf'
    file.save(os.path.join(PDF_UPLOAD_PATH, random_file_name))
    return random_file_name

# Prints without Cover Page (used for testing)
@app.route('/mass', methods=['POST'])
def mass():
    filename = request.form['filename']
    printer = request.form.get('printer', DEFAULT_PRINTER)
    count = int(request.form['count'])
#    for _ in range(count):
    print_file(os.path.join(PDF_UPLOAD_PATH, filename), printer, count) # Changed by Emil Abbasov (IOI2019)
    return "OK"

# Prints with Cover Page (used in IOI Baku 2019)
@app.route('/translation', methods=['POST'])
def translation():
    filename = request.form['filename']
    country_code = request.form['country_code']
    country_name = request.form['country_name']
    count = int(request.form['count'])
    printer_type = request.form['printer_type']
    temp_directory = create_temp_directory()
    final_pdf_path = make_translation_pdf(
        os.path.join(PDF_UPLOAD_PATH, filename),
        country_code,
        country_name,
        temp_directory
    )

    print_file(final_pdf_path, printer_type, count) # Changed by Emil Abbasov (IOI2019)
    return "OK"


@app.route('/contestant', methods=['POST'])
def contestant():
    filename = request.form['filename']
    ip = request.form['ip']
    cups_job_id = request.form['cups_job_id']
    contestant_data = get_contestant_data(ip)
    temp_directory = create_temp_directory()
    if 'desk_image_url' in contestant_data:
        desk_map_img = download(contestant_data['desk_image_url'],
                                'desk_map.png', temp_directory)
    else:
        desk_map_img = contestant_data['desk_image_path']
    final_pdf_path = make_contestant_pdf(
        os.path.join(PDF_UPLOAD_PATH, filename),
        contestant_data['contestant_id'],
        contestant_data['contestant_name'],
        contestant_data['zone'],
        contestant_data['desk_id'],
        desk_map_img,
        cups_job_id,
        temp_directory
    )
    print_file(final_pdf_path, PRINTER_FOR_ZONE[contestant_data['zone']], 1)
    return "OK"
