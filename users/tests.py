from django.test import TestCase, Client
from .models import User
# Create your tests here.

class ActivationTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="Som Tambe", roll="190847", email="somvt@iitk.ac.in")
        User.objects.create(name="Yatharth Goswami", roll="191178", email="ygoswami@iitk.ac.in")
        return print("Added objects to model database.")

    def test_activation(self):
        c = Client()
        response = c.post('/users/verify/',{'roll': '190847'})
        status_code = response.status_code
        return print("Test successful! API status_code =",status_code) if status_code==206 else print("Test unsuccessful! API status_code =",status_code)

