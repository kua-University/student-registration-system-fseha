

# Create your tests here.
from django.test import TestCase
from .models import Student
from .views import StudentListView
from .forms import StudentRegistrationForm
from django.urls import reverse

class StudentModelTest(TestCase):
    def test_student_creation(self):
        student = Student.objects.create(name="John Doe", email="john@example.com")
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(student.email, "john@example.com")

class StudentListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')

class StudentRegistrationFormTest(TestCase):
    def test_form_valid(self):
        form_data = {'name': 'Jane Doe', 'email': 'jane@example.com'}
        form = StudentRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {'name': '', 'email': 'jane@example.com'}
        form = StudentRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

        

class URLTest(TestCase):
    def test_student_list_url(self):
        url = reverse('student-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class IntegrationTest(TestCase):
    def test_student_registration_integration(self):
        response = self.client.post('/register/', {'name': 'Alice', 'email': 'alice@example.com'})
        self.assertEqual(response.status_code, 302)  # Assuming it redirects after successful registration