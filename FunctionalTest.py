from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
   
	#def tearDown(self):
	#	self.browser.quit()

	#def test_browser_title(self):
	#	self.browser.get('http://localhost:8000')
	#	self.assertIn('Loan Application', self.browser.title)
	#	self.fail('Finish the test!')
 
	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Loan Application', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Loan Application', headerText)
		inputName1 = self.browser.find_element_by_id('FullName')
		inputEmail = self.browser.find_element_by_id('EmailAddress')
		inputAddress = self.browser.find_element_by_id('ResidenceAddress')
		inputCode = self.browser.find_element_by_id('ZipCode')
		inputDateOfBirth = self.browser.find_element_by_id('DateOfBirth')
		inputStatus = self.browser.find_element_by_id('Status')
		inputCitizenship = self.browser.find_element_by_id('Citizenship')
		inputCPNo = self.browser.find_element_by_id('CellNo')
		#btnMore = self.browser.find_element_by_id('btnMore')
		#self.assertEqual(inputEmail.get_attribute('placeholder'),'Your Email Address')
		selectValidID = self.browser.find_element_by_id('ValidID')
		inputValidIDNo = self.browser.find_element_by_id('ValidIDNo')
		selectIncome = self.browser.find_element_by_id('Income')
		selectEmployment = self.browser.find_element_by_id('Employment')
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		self.assertEqual(inputName1.get_attribute('placeholder'),'Your Full Name')
		#self.assertEqual(inputValidID.get_attribute('placeholder'),'Types of Valid ID')
		time.sleep(2)
		inputName1.send_keys('Juana S. Dela Cruz')
		time.sleep(2)
		inputEmail.send_keys('Juanadelacruz@gmail.com')
		time.sleep(2)
		inputAddress.send_keys('123 Kundiman Street, Sampaloc')
		time.sleep(2)
		inputCode.send_keys('1009')
		time.sleep(2)
		inputDateOfBirth.send_keys('07/26/1987')
		time.sleep(2)
		inputStatus.send_keys('Single')
		time.sleep(2)
		inputCitizenship.send_keys('Filipino')
		time.sleep(2)
		inputCPNo.send_keys('09876543211')
		time.sleep(2)
		#btnMore.click()
		#time.sleep(2)
		selectValidID.send_keys()
		time.sleep(2)
		inputValidIDNo.send_keys()
		time.sleep(2)
		selectIncome.send_keys()
		time.sleep(2)
		selectEmployment.send_keys()
		time.sleep(2)
		btnConfirm.click()
		time.sleep(1)
		table = self.browser.find_element_by_id('idListTable')
		rows = table.find_elements_by_tag_name('tr')
		#self.assertTrue(any(row.text =='1: Juana A. Cruz'))
		#self.fail('Finish the test!')

if __name__ == '__main__':
   unittest.main(warnings='ignore')
