from openpyxl.reader.excel import load_workbook

from importfiles.models import InitialUploadedFile, FileMetaData
from importfiles.services.BaseParser import BaseParser
from importfiles.services.parsers import update_file_meta
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
            wb = load_workbook(self.file.path)
            sheet = wb.worksheets[0]
            num = sheet.max_row-1
            sum_of = sum(cl.value for cl in sheet['B'] if cl.row !=1)
            wb.close()
            return [True, 'Excel File has been processed!', sum_of, num]
        except:
            return [False, 'Could not open the file! It may be corrupted!', sum_of, num]

    def process_file(self) -> (bool,str, float, int):
        if self.ext in self.text_extensions:
            validation_passed, status_result, sum_of, num = self._process_txt_file()
        else:
            validation_passed, status_result, sum_of, num = self._process_excel_file()
        return validation_passed, status_result, sum_of, num


# def post_save_process_file(file, id:int):
#     processor = FileProcessor(file, id)
#     file_obj = InitialUploadedFile.objects.filter(pk=id)
#
#     update_file_meta(file_obj, 'processing_file', False)
#     validation_passed, status_result, sum_of, num = processor.process_file()
#
#     meta = FileMetaData(file = file_obj.first(), sum = sum_of, elements_number = num)
#     meta.save()
#
#     update_file_meta(file_obj, status_result, validation_passed)
#
#
