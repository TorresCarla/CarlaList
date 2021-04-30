from selenium import webdriver
#import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

cWait = 3
class PageTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
   
	def tearDown(self):
		self.browser.quit()

	def wait_rows_in_idlisttable(self, row_text):
		start_time = time.time()
		while time.time()-start_time<cWait:
			time.sleep(0.1)
			try:
				table = self.browser.find_element_by_id('idListTable')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				if time.time()-start_time>cWait:
					raise e


	#	table = self.browser.find_element_by_id('idListTable')
	#	rows = table.find_elements_by_tag_name('tr')
	#	self.assertIn(row_text, [row.text for row in rows])


 
	def test_start_list_one_user(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Loan Application', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Loan Application', headerText)
		inputName = self.browser.find_element_by_id('FullName')
		inputEmail = self.browser.find_element_by_id('EmailAddress')
		inputAddress = self.browser.find_element_by_id('ResidenceAddress')
		inputCode = self.browser.find_element_by_id('ZipCode')
		inputDateOfBirth = self.browser.find_element_by_id('DateOfBirth')
		inputStatus = self.browser.find_element_by_id('Status')
		inputCitizenship = self.browser.find_element_by_id('Citizenship')
		inputCPNo = self.browser.find_element_by_id('CellNo')
		#self.assertEqual(inputEmail.get_attribute('placeholder'),'Your Email Address')
		selectValidID = self.browser.find_element_by_id('ValidID')
		inputValidIDNo = self.browser.find_element_by_id('ValidIDNo')
		selectIncome = self.browser.find_element_by_id('Income')
		selectEmployment = self.browser.find_element_by_id('Employment')
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		self.assertEqual(inputName.get_attribute('placeholder'),'Your Full Name')
		#self.assertEqual(inputValidID.get_attribute('placeholder'),'Types of Valid ID')
		time.sleep(1)
		inputName.send_keys('Jane S. Dela Cruz')
		time.sleep(1)
		inputEmail.send_keys('Janedelacruz@gmail.com')
		time.sleep(1)
		inputAddress.send_keys('123 Kundiman Street, Sampaloc')
		time.sleep(1)
		inputCode.send_keys('1009')
		time.sleep(1)
		inputDateOfBirth.send_keys('07/26/1987')
		time.sleep(1)
		inputStatus.send_keys('Single')
		time.sleep(1)
		inputCitizenship.send_keys('Filipino')
		time.sleep(1)
		inputCPNo.send_keys('09876543211')
		time.sleep(1)
		selectValidID.send_keys(Keys.ARROW_DOWN)
		time.sleep(1)
		inputValidIDNo.send_keys('123-4567-890')
		time.sleep(1)
		selectIncome.send_keys(Keys.ARROW_DOWN)
		time.sleep(1)
		selectEmployment.send_keys(Keys.ARROW_DOWN)
		btnConfirm.click()
		time.sleep(1)
		self.wait_rows_in_idlisttable('1: Jane S. Dela Cruz') #in Juanadelacruz@gmail.com')
		time.sleep(1)
		inName = self.browser.find_element_by_id('FullName')
		inName.click()
		inName.send_keys('Prince J. Valdez')
		time.sleep(1)
		inEmail = self.browser.find_element_by_id('EmailAddress')
		inEmail.click()
		inEmail.send_keys('Valdez_PrinceJ@gmail.com')
		time.sleep(1)
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		self.wait_rows_in_idlisttable('2: Prince J. Valdez') #in Valdez_PrinceJ@gmail.com")

	def test_other_user_different_urls(self):
		self.browser.get(self.live_server_url)
		time.sleep(1)
		inName = self.browser.find_element_by_id('FullName')
		inName.click()
		inName.send_keys('Julianna L. Madrid')
		time.sleep(1)
		inEmail = self.browser.find_element_by_id('EmailAddress')
		inEmail.click()
		inEmail.send_keys('JuliannaLM45@gmail.com')
		time.sleep(1)
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		self.wait_rows_in_idlisttable('1: Julianna L. Madrid') #in JuliannaLM45@gmail.com')
		viewlist_url = self.browser.current_url
		self.assertRegex(viewlist_url, '/LoanApp/.+')

		self.browser.quit()
		self.browser = webdriver.Firefox()
		self.browser.get(self.live_server_url)
		pageBody = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Julianna L. Madrid in JuliannaLM45@gmail.com', pageBody)
		time.sleep(1)
		inName = self.browser.find_element_by_id('FullName')
		inName.click()
		inName.send_keys('Miguel C. Tolentino')
		time.sleep(1)
		inEmail = self.browser.find_element_by_id('EmailAddress')
		inEmail.click()
		inEmail.send_keys('MiggyTolentino@gmail.com')
		time.sleep(1)
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		self.wait_rows_in_idlisttable('1: Miguel C. Tolentino') #in MiggyTolentino@gmail.com')
		user2_url = self.browser.current_url
		self.assertRegex(user2_url, '/LoanApp/.+')
		self.assertNotEqual(viewlist_url, user2_url)
		pageBody = self.browser.find_element_by_tag_name('body').text
		#self.assertNotIn('Julianna L. Madrid in JuliannaLM45@gmail.com', pageBody)
		self.assertIn('Miguel C. Tolentino in MiggyTolentino@gmail.com', pageBody)











	#self.fail('Finish the test!')

#def test_browser_title(self):
	#	self.browser.get('http://localhost:8000')
	#	self.assertIn('Loan Application', self.browser.title)
	#	self.fail('Finish the test!')

	#btnMore.click()
	#time.sleep(2)
	#btnMore = self.browser.find_element_by_id('btnMore')

	#table = self.browser.find_element_by_id('idListTable')
	#rows = table.find_elements_by_tag_name('tr')
	#self.assertIn('1:Juana S. Dela Cruz in Juanadelacruz@gmail.com', [row.text for row in rows])
	#self.assertIn('2:Prince J. Valdez in Valdez_PrinceJ@gmail.com', [row.text for row in rows])
	#self.assertTrue(any(row.text =='1: Juana A. Cruz'))


#if __name__ == '__main__':
#   unittest.main(warnings='ignore')
