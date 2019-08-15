import subprocess

from ioiprint import CUPS_SERVER_ADDRESS

# Changes made by Emil Abbasov (IOI2019) to print N copies, with Collate true:
def print_file(file_path, printer, count):
    subprocess.run(['lpr', '-#', str(count), '-o Collate=true', '-H', CUPS_SERVER_ADDRESS, '-P', printer,
                    file_path], check=True)
