from importfiles.models import InitialUploadedFile
from mus.settings import EXCEL_EXTENSIONS, TEXT_EXTENSIONS


class BaseParser:
    excel_extensions = EXCEL_EXTENSIONS
    text_extensions = TEXT_EXTENSIONS

    def __init__(self, file, file_id: int):
        self.file = file
        self.file_id = file_id

    @property
    def ext(self):
        return get_extension(self.file.name)

    def _get_txt_column_delimeter(self) -> str:
        if self.ext == 'txt':
            initial_file = InitialUploadedFile.objects.filter(id=self.file_id).first()
            col_del = initial_file.txt_column_delimiter
        else:
            col_del = ","
        return col_del

def get_extension(file_name: str) -> str:
    return file_name.split('.')[-1]