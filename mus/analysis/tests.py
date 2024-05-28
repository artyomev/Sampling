from django.db.models import signals
from django.test import TestCase
from analysis.serializers import AnalysisSerializer
from importfiles.models import InitialUploadedFile
from musauth.models import MusUser
from projects.models import Project



class AnalysisSerializerTest(TestCase):
    """
       Ensure we don't need to pass sampled_units_count.
    """
    def setUp(self):
        user = MusUser.objects.create_superuser(email="test@test.com", username="root", password="admin")
        project = Project.objects.create(title='Test project')
        file = InitialUploadedFile.objects.create(initial_file='media/files_for_test/mus_test2.txt',
                                           txt_column_delimiter="||",
                                           file_name="string",
                                           thousand_separator=",",
                                           decimal_separator=",",
                                           by_user=user,
                                           project_id = 1
                                           )



    def test_serializer_valid_data(self):
        data = {
            "analysis_type": "string",
            "analysis_name": "string",
            "sampled_units_count": 0,
            "sample_name": "string",
            "project": 1,
            "files": [
                1
            ]
        }
        serializer = AnalysisSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def tearDown(self):
        user = MusUser.objects.get(id=1)
        project = Project.objects.get(id=1)
        file = InitialUploadedFile.objects.get(id=1)

        user.delete()
        project.delete()
        file.delete()

