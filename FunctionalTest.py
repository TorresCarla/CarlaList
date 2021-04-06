from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
   
	def tearDown(self):
		self.browser.quit()
      
	def test_browser_title(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Recipe List', self.browser.title)
		#self.fail('Finish the test!')
    
    def test_start_list_and_retrieve_it(self):
    	self.browser.get('http://localhost:8000')
    	self.assertIn('Recipe List', self.browser.title)
    	headertext = self.browser.find_element_by_tag_name('h1').text
    	self.assertIn('Recipe List', headerText)
    	inputbox = self.browser.find_element_by_id('idNewEntry')
    	self.assertEqual(inputbox.get_attribute('placeholder'),'Favorite Recipe.')
    	inputbox.send_keys('Sapin Sapin')
    	inputbox.send_keys(Keys.ENTER)
    	time.sleep(1)
    	table = self.browser.find_element_by_id('idListTable')
    	rows = table.find_elements_by_tag_name('tr')
    	self.assertTrue(any(row.text == '1: Sapin Sapin'))
    	self.fail('Finish the test!')

if __name__ == '__main__':
   unittest.main()
