# Copyright Nova Code (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from test_component import ComponentTestCase
from formiodata.components import phoneNumberComponent


class PhoneNumberComponentTestCase(ComponentTestCase):

    def test_object(self):
        # phoneNumberComponent
        phoneNumber = self.builder.form_components['phoneNumber']
        self.assertIsInstance(phoneNumber, phoneNumberComponent)

        # Not phoneNumberComponent
        firstName = self.builder.form_components['firstName']
        self.assertNotIsInstance(firstName, phoneNumberComponent)
        submit = self.builder.form_components['submit']
        self.assertNotIsInstance(submit, phoneNumberComponent)

    def test_get_key(self):
        phoneNumber = self.builder.form_components['phoneNumber']
        self.assertEqual(phoneNumber.key, 'phoneNumber')

    def test_get_type(self):
        phoneNumber = self.builder.form_components['phoneNumber']
        self.assertEqual(phoneNumber.type, 'phoneNumber')

    def test_get_label(self):
        phoneNumber = self.builder.form_components['phoneNumber']
        self.assertEqual(phoneNumber.label, 'Phone Number')

    def test_set_label(self):
        phoneNumber = self.builder.form_components['phoneNumber']
        self.assertEqual(phoneNumber.label, 'Phone Number')
        phoneNumber.label = 'Foobar'
        self.assertEqual(phoneNumber.label, 'Foobar')

    def test_get_form(self):
        phoneNumber = self.form.components['phoneNumber']
        self.assertEqual(phoneNumber.label, 'Phone Number')
        self.assertEqual(phoneNumber.value, '(069) 999-9999')
        self.assertEqual(phoneNumber.type, 'phoneNumber')

    def test_get_form_data(self):
        phoneNumber = self.form.data.phoneNumber
        self.assertEqual(phoneNumber.label, 'Phone Number')
        self.assertEqual(phoneNumber.value, '(069) 999-9999')
        self.assertEqual(phoneNumber.type, 'phoneNumber')
