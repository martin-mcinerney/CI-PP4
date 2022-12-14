from django.test import TestCase
from .forms import SiteUpload, GalleryUpload, ContactForm
from .models import FlyingSite

# form validation
# test ideas came from ci django testing 

class TestFormValidation(TestCase):
    def test_site_upload_form(self):
        form = SiteUpload({'site_name': "",
                        'pilot': "jim",
                        'wind_direction': "N",
                        'overview': 'cornflakes',
                        'landing_information': 'some text',
                        'warnings': 'some text',
                        'featured_image': "",
                        'status': 1})
        self.assertFalse(form.is_valid())
        self.assertIn('site_name', form.errors.keys())
        self.assertEqual(
            form.errors['site_name'][0],
            'This field is required.')


    def test_gallery_upload_form(self):
        form = GalleryUpload(
            {'featured_image': "", 'site_name': "", 'status': 1, })
        self.assertFalse(form.is_valid())
        self.assertIn('site_name', form.errors.keys())
        self.assertEqual(
            form.errors['site_name'][0],
            'This field is required.')


    def test_contact_form(self):
        form = ContactForm(
            {'first_name': "", 'email_address': "", 'message': "", })
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(
            form.errors['first_name'][0],
            'This field is required.')

# views


class TestViews(TestCase):
    def test_get_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


    def test_get_sites(self):
        response = self.client.get("/sites", follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'site_list.html')


    def test_add_site(self):
        response = self.client.get("/site_upload", follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'site_upload.html')


    def test_get_form_error(self):
        response = self.client.get("/form_error")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form_error.html')


    def test_get_contact_page(self):
        response = self.client.get("/contact", follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
