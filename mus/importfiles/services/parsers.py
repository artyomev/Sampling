from importfiles.models import InitialUploadedFile, FileMetaData
from importfiles.storage import uploads_storage
from openpyxl import load_workbook

def get_extension(file_name: str) -> str:
    return file_name.split('.')[-1]


class Parser:
    excel_extensions = ['xslx', 'xlsb', 'xls', 'xlsm']
    text_extensions = ['txt', 'csv']

    def __init__(self, file, file_id:int):
        self.file = file
        self.file_id = file_id
    @property
    def ext(self):
        return get_extension(self.file.name)

    def _parse_txt_file_columns(self) -> (bool,str):
        if self.ext == 'txt':
            initial_file = InitialUploadedFile.objects.filter(id=self.file_id).first()
            col_del = initial_file.txt_column_delimiter
        else:
            col_del = ","
        try:
            with uploads_storage.open(self.file.name, 'r') as f:
                first_line = f.readline()

            if len(first_line.split(col_del)) > 2:
                return False,'There should be only 2 columns in a file!'
            return True, 'Column format ok'
        except:
            return False, 'Could not open the file! It may be corrupted!'
    
    def _parse_excel_file_columns(self) -> (bool, str):
        try:
            wb =load_workbook(self.file.path)
            sheet = wb.worksheets[0]
            if sheet.max_column > 2:
                wb.close()
                return False,'There should be only 2 columns in a file!'
            wb.close()
            return True, 'Column format ok'
        except:
            return False, 'Could not open the file! It may be corrupted!'

    def parse_file(self)-> (bool, str):
        if self.ext in self.text_extensions:
            validation_passed,status_result = self._parse_txt_file_columns()
        else:
            validation_passed,status_result = self._parse_excel_file_columns()
        return validation_passed,status_result


def post_save_parse_file(file, id:int):
    parser = Parser(file, id)
    file_obj = InitialUploadedFile.objects.filter(pk=id)

    update_file_meta(file_obj, 'checking_columns_format', False)
    validation_passed, status_result = parser.parse_file()
    update_file_meta(file_obj, status_result, validation_passed)


def update_file_meta(obj, status, validation_passed):
    obj.update(
        status= status,
        validation_passed = validation_passed
    )
