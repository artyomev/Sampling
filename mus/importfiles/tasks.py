import sys
import logging

logger = logging.getLogger(__name__)
from celery import shared_task
from django.core.files.uploadedfile import UploadedFile

from importfiles.models import InitialUploadedFile, FileMetaData
from importfiles.services.file_processors import FileProcessor
from importfiles.services.parsers import update_file_meta, Parser


@shared_task()
def post_save_process_file(id:int):
    logger.info('Started Processing file')
    file_obj = InitialUploadedFile.objects.filter(id=id)
    file = file_obj.first().initial_file.file
    processor = FileProcessor(file, id)

    update_file_meta(file_obj, 'processing_file', False)
    validation_passed, status_result, sum_of, num = processor.process_file()

    meta = FileMetaData(file = file_obj.first(), sum = sum_of, elements_number = num)
    meta.save()

    update_file_meta(file_obj, status_result, validation_passed)
    logger.info('Finished Processing file')

@shared_task()
def post_save_parse_file(id:int):
    logger.info('Started Parsing file')
    file_obj = InitialUploadedFile.objects.filter(id=id)
    file = file_obj.first().initial_file.file
    parser = Parser(file, id)

    update_file_meta(file_obj, 'checking_columns_format', False)
    validation_passed, status_result = parser.parse_file()
    update_file_meta(file_obj, status_result, validation_passed)
    logger.info('Finished Parsing file')
