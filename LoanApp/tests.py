from django.test import TestCase
from LoanApp.models import Item, Loaner
	
class HomePageTest(TestCase):
	def test_mainpage_returns_correct_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'mainpage.html')
		
class ORMTest(TestCase):
	def test_saving_retrieving_list(self):
		newLoaner = Loaner()
		newLoaner.save()
		txtItem1 = Item()
		txtItem1.text = 'Item one'
		txtItem1.LoanId = newLoaner
		txtItem1.save()
		txtItem2 = Item()
		txtItem2.LoanId = newLoaner
		txtItem2.text = 'Item two'
		txtItem2.save()
		savedItems = Item.objects.all()
		savedLoaner = Loaner.objects.first()
		self.assertEqual(savedItems.count(), 2)
		self.assertEqual(savedLoaner,newLoaner)
		savedItem1 = savedItems[0]
		savedItem2 = savedItems[1]
		self.assertEqual(savedItem1.text, 'Item one')
		self.assertEqual(savedItem2.text, 'Item two')
		self.assertEqual(savedItem1.LoanId, newLoaner)
		self.assertEqual(savedItem2.LoanId, newLoaner)			

class ViewTest(TestCase):
	def test_displays_each_loaner(self):
		newLoaner = Loaner.objects.create()
		Item.objects.create(LoanId=newLoaner, text='Jennifer Miasco')
		Item.objects.create(LoanId=newLoaner, text='Roli Anne Maestre')
		response = self.client.get(f'/LoanApp/{newLoaner.id}/')
		self.assertContains(response, 'Jennifer Miasco')
		self.assertContains(response, 'Roli Anne Maestre')
		self.assertNotContains(response, 'Rafael Carvajal')
		self.assertNotContains(response, 'Sharalyn Dela Cerna')
		
		newLoaner_2 = Loaner.objects.create()
		Item.objects.create(LoanId=newLoaner_2, text='Rafael Carvajal')
		Item.objects.create(LoanId=newLoaner_2, text='Sharalyn Dela Cerna')
		response = self.client.get(f'/LoanApp/{newLoaner_2.id}/')
		self.assertContains(response, 'Rafael Carvajal')
		self.assertContains(response, 'Sharalyn Dela Cerna')

		
	def test_listview_uses_loanaf(self):
		newLoaner = Loaner.objects.create()
		response = self.client.get(f'/LoanApp/{newLoaner.id}/')
		self.assertTemplateUsed(response, 'LoanAF.html')

	def test_pass_list_to_template(self):
		dummyList1 = Loaner.objects.create()
		dummyList2 = Loaner.objects.create()
		passList = Loaner.objects.create()
		response = self.client.get(f'/LoanApp/{passList.id}/')
		self.assertEqual(response.context['LoanId'], passList)

class CreateListTest(TestCase):
	def test_save_POST_request(self):
		response = self.client.post('/LoanApp/newlist_url',data={'FullName':'New FullName'})	
		self.assertEqual(Item.objects.count(),1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text, 'New FullName')

	def test_redirects_POST(self):
		response = self.client.post('/LoanApp/newlist_url',data={'FullName':'New FullName'})
		newList = Loaner.objects.first()
		self.assertRedirects(response, f'/LoanApp/{newList.id}/')

class AddItemTest(TestCase):
	def test_add_POST_request_to_existing_list(self):
		DummyList1 = Loaner.objects.create()
		DummyList2 = Loaner.objects.create()
		existingList = Loaner.objects.create()
		self.client.post(f'/LoanApp/{existingList.id}/addItem',data={'FullName': 'New item for existing list'})
		self.assertEqual(Item.objects.count(),1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text, 'New item for existing list')
		self.assertEqual(newItem.LoanId, existingList)

	def test_redirects_to_list_view(self):
	 	DummyList1 = Loaner.objects.create()
	 	DummyList2 = Loaner.objects.create()
	 	DummyList3 = Loaner.objects.create()
	 	existingList = Loaner.objects.create()
	 	response = self.client.post(f'/LoanApp/{existingList.id}/addItem',data={'FullName': 'New item for existing list'})
	 	self.assertRedirects(response, f'/LoanApp/{existingList.id}/')		








#def test_template_display_list(self):
	#	Item.objects.create(text='List item 1')
	#	Item.objects.create(text='List item 2')
	#	response = self.client.get('/')
	#	self.assertIn('List item 1', response.content.decode())
	#	self.assertIn('List item 2', response.content.decode())

#def test_only_saves_items_if_necessary(self):
#		self.client.get('/')
#		self.assertEqual(Item.objects.count(), 0)

#		#self.assertEqual(response.status_code, 302)
#		#self.assertEqual(response['location'], '/LoanApp/viewlist_url/')

	#from django.urls import resolve
	#from LoanApp.views import MainPage
	#from django.http import HttpRequest
	#from django.template.loader import render_to_string

	#def test_mainpage_returns_correct_views(self):
	#	response = self.client.get('/')
	#	html = response.content.decode('utf8')
	#	string_html = render_to_string('mainpage.html')
	#	self.assertEqual(html, string_html)
	#	self.assertTemplateUsed(response, 'mainpage.html')

	#def test_root_url_resolves_to_mainpage_view(self):
	#	found = resolve('/')
	#	self.assertEqual(found.func, MainPage)

	#def test_mainpage_returns_correct_view(self):
	#	request = HttpRequest()
	#	response = MainPage(request)
	#	html = response.content.decode('utf8')
	#	string_html = render_to_string('mainpage.html')
	#	self.assertEqual(html, string_html)

	#def test_mainpage_returns_correct_view(self):
	#	request = HttpRequest()
	#	response = MainPage(request)
	#	html = response.content.decode('utf8')
	#	self.assertTrue(html.strip().startswith('<html>'))
	#	self.assertIn('<title>Loan Application</title>', html)
	#	self.assertTrue(html.strip().endswith('</html
	
		#def test_save_POST_request(self):
	#	response = self.client.post('/', data={'FullName': 'NewFullName'})
		#self.assertIn('NewFullName', response.content.decode())
		#self.assertTemplateUsed(response,'mainpage.html')
	#	self.assertEqual(Item.objects.count(),1)
	#	newItem = Item.objects.first()
	#	self.assertEqual(newItem.text, 'NewFullName')

	#def test_redirects_POST(self):
	#	response = self.client.post('/', data={'FullName': 'NewFullName'})
	#	self.assertEqual(response.status_code, 302)
	#	self.assertEqual(response['location'], '/LoanApp/viewlist_url/')
