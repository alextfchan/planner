from django.test import TestCase
from django.urls import reverse
from django.db import models


from apptodolist.models import ToDoList, ToDoListItem


class ToDoListTestCaseModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        '''For object creation that won't be modified or changed in any test methods'''
        cls.list_name = ToDoList.objects.create(list_name='Test List 1')
        cls.list_name2 = ToDoList.objects.create(list_name='Test List 2')
        print('setUpTestData: Run once to set up non-modified data for all class methods.')

    # def tearDown(self):
    #     print('tearDown method.')

    def test_model_str1(self):
        print('Method: Testing for correct list_name')
        self.assertEqual(str(self.list_name), 'Test List 1')
        self.assertEqual(str(self.list_name2), 'Test List 2')

    def test_to_do_list_label(self):
        print('Method: Testing for the correct label (column name).')
        test_for_list_1 = ToDoList.objects.get(id=1)
        field_label = test_for_list_1._meta.get_field('list_name').verbose_name
        self.assertEqual(field_label, 'list name')

    def test_to_do_list_name(self):
        print('Method: Testing for the correct list_name matches with the ID')
        test_for_list_1 = ToDoList.objects.get(id=1)
        test_for_list_2 = ToDoList.objects.get(id=2)
        expected_object_name_1 = test_for_list_1.list_name
        expected_object_name_2 = test_for_list_2.list_name
        self.assertEqual(str(test_for_list_1), expected_object_name_1)
        self.assertEqual(str(test_for_list_2), expected_object_name_2)

    @classmethod
    def tearDownClass(cls):
        print('method: Runs after all tests...')

# https://www.freecodecamp.org/news/how-to-write-unit-tests-for-instance-methods-in-python/
# https://stackoverflow.com/questions/53122131/django-testing-reuse-setup-for-multiple-classes-files
# https://imsadra.me/setup-teardown-in-python-unit-testing
# https://www.valentinog.com/blog/testing-django/

class ToDoListTestCaseRequestResponse(TestCase):

    @classmethod
    def setUpTestData(cls):
        '''For object creation that won't be modified or changed in any test methods'''
        cls.list_name = ToDoList.objects.create(list_name='Test List 1')
        cls.list_name2 = ToDoList.objects.create(list_name='Test List 2')
        print('setUpTestData: Run once to set up non-modified data for all class methods.')

    # def tearDown(self):
    #     print('tearDown method.')

    def test_get_absolute_url(self):
        self.list_name.id = ToDoList.objects.get(id=1)
        print(self.list_name.id.get_absolute_url(), 'HELOEFLWSOFLWESFOELFOESWFLSOFLSEFOSELFSOEFL')
        self.assertEqual('/planner/1/', self.list_name.id.get_absolute_url())

    def test_to_do_list_exists_at_desired_location(self):
        print('Method: Testing if reponse status_code returns 200 when passed valid response.')
        response = self.client.get('/planner/1/')
        self.assertEqual(response.status_code, 200)

    def test_to_do_list_correct_template_used(self):
        response = self.client.get(reverse('app_todo:app_todo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_index.html')

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#test_structure_overview
    # https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase
    # https://docs.djangoproject.com/en/5.0/topics/testing/overview/
    # https://docs.djangoproject.com/en/5.0/topics/testing/
    # https://docs.djangoproject.com/en/5.0/topics/testing/tools/#:~:text=Exceptions%C2%B6&text=You%20can%20then%20use%20a,PermissionDenied%20%2C%20SystemExit%20%2C%20and%20SuspiciousOperation%20.

# class ToDoListItemsTestCaseModels:

#     @classmethod
#     def setUpTestData(cls):
#         pass

#     # def test_to_do_list_one_to_many(self):
#     #     to_do_list = ToDoList.objects.create(list_name='Test List 1')
#     #     to_do_item = ToDoListItem.objects.create()