from importfiles.models import InitialUploadedFile


def post_save_initial_file(file, id: int):
    file_obj = InitialUploadedFile.objects.filter(pk=id)
    file_obj.update(
        status='is_being_processed',
    )
