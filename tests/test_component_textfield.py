# Copyright Nova Code (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from test_component import ComponentTestCase
from formiodata.components import textfieldComponent


class textfieldComponentTestCase(ComponentTestCase):

    def test_object(self):
        # TextfieldComponent
        firstName = self.builder.form_components['firstName']
        self.assertIsInstance(firstName, textfieldComponent)

        lastName = self.builder.form_components['lastName']
        self.assertIsInstance(lastName, textfieldComponent)

        # Not TextfieldComponent
        email = self.builder.form_components['email']
        self.assertNotIsInstance(email, textfieldComponent)
        submit = self.builder.form_components['submit']
        self.assertNotIsInstance(submit, textfieldComponent)

    def test_get_key(self):
        firstName = self.builder.form_components['firstName']
        self.assertEqual(firstName.key, 'firstName')

    def test_get_type(self):
        firstName = self.builder.form_components['firstName']
        self.assertEqual(firstName.type, 'textfield')

    def test_get_label(self):
        firstName = self.builder.form_components['firstName']
        self.assertEqual(firstName.label, 'First Name')

    def test_set_label(self):
        firstName = self.builder.form_components['firstName']
        self.assertEqual(firstName.label, 'First Name')
        firstName.label = 'Foobar'
        self.assertEqual(firstName.label, 'Foobar')

    def test_get_form(self):
        firstName = self.form.components['firstName']
        self.assertEqual(firstName.label, 'First Name')
        self.assertEqual(firstName.value, 'Bob')
        self.assertEqual(firstName.type, 'textfield')
        
    def test_get_form_data(self):
        firstName = self.form.data.firstName
        self.assertEqual(firstName.label, 'First Name')
        self.assertEqual(firstName.value, 'Bob')
        self.assertEqual(firstName.type, 'textfield')

    # i18n translations
    def test_get_label_i18n_nl(self):
        firstName = self.builder_i18n_nl.form_components['firstName']
        self.assertEqual(firstName.label, 'Voornaam')
        lastName = self.builder_i18n_nl.form_components['lastName']
        self.assertEqual(lastName.label, 'Achternaam')

    def test_get_form_data_i18n_nl(self):
        self.assertEqual(self.form_i18n_nl.data.firstName.label, 'Voornaam')
        self.assertEqual(self.form_i18n_nl.data.lastName.label, 'Achternaam')
