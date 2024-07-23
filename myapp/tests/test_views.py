from django.test import TestCase, Client
from django.urls import reverse
from myapp.forms import PasswordForm

class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_view_get(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertIsInstance(response.context['form'], PasswordForm)

    def test_home_view_post_valid_form(self):
        response = self.client.post(reverse('home'), {'password': 'validpassword'})
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertRedirects(response, reverse('welcome', kwargs={'password': 'validpassword'}))

    def test_home_view_post_invalid_form(self):
        response = self.client.post(reverse('home'), {'password': ''})
        self.assertEqual(response.status_code, 200)  # Form is invalid, so it should re-render the home page
        self.assertTemplateUsed(response, 'home.html')
        self.assertFormError(response, 'form', 'password', 'This field is required.')

    def test_welcome_view(self):
        response = self.client.get(reverse('welcome', kwargs={'password': 'testpassword'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome.html')
        self.assertContains(response, 'testpassword')

    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertRedirects(response, reverse('home'))
