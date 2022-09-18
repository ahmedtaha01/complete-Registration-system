from django.test import TestCase
from django.urls import reverse

from project.models import Project

class ProjectIsExist(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('project_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/home.html')

    def test_create_page(self):
        response = self.client.get(reverse('create_project'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/create.html')

class ProjectModelTest(TestCase):
    def setUp(self):
        Project.objects.create(project_title='GOT',\
            project_details='You know nothing, John Snow', \
                project_total_target=12345, \
                    project_end_date='2023-12-22')
    
    def test_project_title(self):
        project = Project.objects.get(project_title='GOT')
        expected_title = f'{project.project_title}'
        self.assertEqual(expected_title, 'GOT')

    def test_project_details(self):
        project = Project.objects.get(project_title='GOT')
        details = f'{project.project_details}'
        self.assertEqual(details, 'You know nothing, John Snow')
    