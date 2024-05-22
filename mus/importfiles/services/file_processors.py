from openpyxl.reader.excel import load_workbook

from importfiles.models import InitialUploadedFile, FileMetaData
from importfiles.services.BaseParser import BaseParser
from importfiles.services.parsers import update_file_meta, get_excel_workbook
from importfiles.storage import uploads_storage


class FileProcessor(BaseParser):
    def _process_txt_file(self)-> list:
        col_del = self._get_txt_column_delimeter()
        num: int = 0
        sum_of: float = 0
        try:
            with uploads_storage.open(self.file.name, 'r') as f:
                for line in f.readlines()[1:]:
                    line = line.rstrip('\n').rstrip('\r')
                    if line != '':
                        num += 1
                        sum_of += float((line.split(col_del)[1]).strip())
                return [True, 'Text File has been processed!', sum_of, num]
        except Exception as e:
            print(e)
            return [False, 'Could not read the file! Something went wrong!', 0, 0]

    def _process_excel_file(self) -> list:
        sum_of =0
        num=0
        try:
            with get_excel_workbook(self.file.path) as wb:
                sheet = wb.worksheets[0]
                num = sheet.max_row-1
                sum_of = sum(cl.value for cl in sheet['B'] if cl.row !=1)
                return [True, 'Excel File has been processed!', sum_of, num]
        except Exception as e:
            return [False, repr(e) + self.file.path, sum_of, num]

    def process_file(self) -> (bool,str, float, int):
        if self.ext in self.text_extensions:
            validation_passed, status_result, sum_of, num = self._process_txt_file()
        else:
            validation_passed, status_result, sum_of, num = self._process_excel_file()
        return validation_passed, status_result, sum_of, num


