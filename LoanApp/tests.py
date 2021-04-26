#from django.urls import resolve
from django.test import TestCase
#from LoanApp.views import MainPage
#from django.http import HttpRequest
#from django.template.loader import render_to_string
from LoanApp.models import Item

class HomePageTest(TestCase):
   
	def test_mainpage_returns_correct_views(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'mainpage.html')

	def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(),0)

	def test_save_POST_request(self):
		response = self.client.post('/', data={'FullName': 'NewFullName'})
		#self.assertIn('NewFullName', response.content.decode())
		#self.assertTemplateUsed(response,'mainpage.html')

		self.assertEqual(Item.objects.count(),1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text, 'NewFullName')

		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

class ORMTest(TestCase):
	def test_saving_retrieving_list(self):
		txtItem1 = Item()
		txtItem1.text = 'Item one'
		txtItem1.save()
		txtItem2 = Item()
		txtItem2.text = 'Item two'
		txtItem2.save()
		savedItems = Item.objects.all()
		self.assertEqual(savedItems.count(), 2)
		savedItem1 = savedItems[0]
		savedItem2 = savedItems[1]
		self.assertEqual(savedItem1.text, 'Item one')
		self.assertEqual(savedItem2.text, 'Item two')

'''	def test_mainpage_returns_correct_views(self):
		response = self.client.get('/')
		html = response.content.decode('utf8')
		string_html = render_to_string('mainpage.html')
		self.assertEqual(html, string_html)
		self.assertTemplateUsed(response, 'mainpage.html')

	def test_root_url_resolves_to_mainpage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, MainPage)

	def test_mainpage_returns_correct_view(self):
		request = HttpRequest()
		response = MainPage(request)
		html = response.content.decode('utf8')
		string_html = render_to_string('mainpage.html')
		self.assertEqual(html, string_html)

	def test_mainpage_returns_correct_view(self):
		request = HttpRequest()
		response = MainPage(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.strip().startswith('<html>'))
		self.assertIn('<title>Loan Application</title>', html)
		self.assertTrue(html.strip().endswith('</html
		'''