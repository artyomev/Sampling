from importfiles.models import InitialUploadedFile


def post_save_initial_file(file, id:int):
    print('post save signal!!!')
