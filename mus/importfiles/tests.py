from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from importfiles.models import InitialUploadedFile
from musauth.models import MusUser
from projects.models import Project


class FilesTests(APITestCase):

    def setUp(self):
        self.user = MusUser.objects.create_superuser(email="test@test.com", username="root", password="admin")
        self.project = Project.objects.create(title='Test project')

    def test_create_file(self):
        """
        Ensure we can create a new file object.
        """
        url = reverse('upload')
        with open('files_for_test/mus_test2.txt', 'rb') as test_file:
            data = {
                'initial_file': test_file,
                'txt_column_delimiter': '||',
                'file_name': 'txt_test_file',
                'thousand_separator': ',',
                'decimal_separator': '.',
                'project': self.project.id,
                'by_user': self.user.id
            }
            response = self.client.post(url, data, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(InitialUploadedFile.objects.first().file_name, 'txt_test_file')


    def tearDown(self):

        self.user.delete()
        self.project.delete()
