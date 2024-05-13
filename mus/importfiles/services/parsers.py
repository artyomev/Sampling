from importfiles.models import InitialUploadedFile
from importfiles.storage import uploads_storage


def get_extension(file_name: str) -> str:
    return file_name.split('.')[-1]


def parse_txt_file(ext:str,file, id:int):
    if ext == 'txt':
        initial_file = InitialUploadedFile.objects.filter(id=id).first()
        col_del = initial_file.txt_column_delimiter
    else:
        col_del = ","
    with uploads_storage.open(file.name, 'r') as f:
        first_line = f.readline()

    if len(first_line.split(col_del))>2:
        print('Format error')


def post_save_parse_file(file, id:int):
    excel_extensions = ['xslx', 'xlsb', 'xls', 'xlsm']
    python_extensions = ['txt', 'csv']
    ext = get_extension(file.name)
    if ext in python_extensions:
        parse_txt_file(ext, file, id)
    else:
        print('This feature not created yet')