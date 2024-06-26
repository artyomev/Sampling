from contextlib import contextmanager

import openpyxl
import io

from django.core.files.storage import default_storage

from importfiles.services.BaseParser import BaseParser
from importfiles.storage import uploads_storage
from mus import settings


class Parser(BaseParser):

    def _parse_txt_file_columns(self) -> (bool,str):
        col_del = self._get_txt_column_delimeter()
        try:
            with default_storage.open(self.file.name, 'r') as f:
                first_line = f.readline()

            if len(first_line.split(col_del)) > 2:
                return False,'There should be only 2 columns in a file!'
            return True, 'Column format ok'
        except Exception as e:
            return False, repr(e)
    
    def _parse_excel_file_columns(self) -> (bool, str):
        try:
            with get_excel_workbook(self.file.name) as wb:
                sheet = wb.worksheets[0]
                if sheet.max_column > 2:
                    wb.close()
                    return False,'There should be only 2 columns in a file!'
            return True, 'Column format ok'
        except Exception as e:
            raise ValueError(repr(e), self.file.path, uploads_storage.location, settings.BASE_DIR)
        #     return False, repr(e) + " | " + self.file.path

    def parse_file(self)-> (bool, str):
        if self.ext in self.text_extensions:
            validation_passed,status_result = self._parse_txt_file_columns()
        else:
            validation_passed,status_result = self._parse_excel_file_columns()
        return validation_passed,status_result



def update_file_meta(obj, status, validation_passed):
    obj.update(
        status= status,
        validation_passed = validation_passed
    )

@contextmanager
def get_excel_workbook(path: str) -> openpyxl.workbook.workbook.Workbook:
    """Читает и возвращает файл экселя.

    Args:
        path (str): путь к файлу

    Yields:
        openpyxl.workbook.workbook.Workbook: excel workbook
    """
    # with uploads_storage.open(path, "rb") as f:
    with default_storage.open(path, "rb") as f:
        in_mem_file = io.BytesIO(f.read())

    wb = openpyxl.load_workbook(in_mem_file, data_only=True, read_only=False)
    try:
        yield wb
    finally:
        wb.close()
        del wb
        del in_mem_file