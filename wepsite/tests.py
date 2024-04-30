from django.test import TestCase, tag
from wepsite.forms import ContactForm

class ShopTestCase( TestCase):
    def test_something(self):
        """Test a feature."""
        print("Testing something.")
    def test_something_else(self):
        """Test another feature."""
        print("Testing something else.")


class WepsiteTestCase(TestCase):
    @tag("form", "contact")
    def test_form_is_valid(self):
        form = ContactForm()
        self.assertEqual(form.is_valid(), True)


    @tag("form", "check_valid")
    def test_form_data_true(self):
        data = {'name': 'Alex', 'email': 'alex@test.com', 'Subject': 'subject', 'message': 'text'}
        form = ContactForm(data)
        self.assertEqual(form.is_valid(), True)


    @tag("check_valid")
    def test_form_data_false(self):
        data = {'name': 'Alex', 'email': 'alex@test.com', 'Subject': 'subject', 'message': 'text'}
        form = ContactForm(data)
        self.assertEqual(form.is_valid(), False)
        
        