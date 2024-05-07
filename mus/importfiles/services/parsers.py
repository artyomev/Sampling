
def get_extension(file_name: str) -> str:
    return file_name.split('.')[-1]


def parse_txt_file(file):
    with open(file) as f:
        first_line = f.readline()
    if len(first_line.split('.')):
        print('Format error')


def post_save_parse_file(file, id:int):
    excel_extensions = ['xslx', 'xlsb', 'xls', 'xlsm']
    python_extensions = ['txt', 'csv']

    if get_extension(file.name) in python_extensions:
        parse_txt_file(file)
    else:
        print('This feature not created yet')