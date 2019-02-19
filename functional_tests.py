from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# User opens homapage of the inline to-do app
		self.browser.get('http://localhost:8000')

		# User see that page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# User is presented an input text-box, inviting to enter a to-do item
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			)

		# User types "Take car from repair"
		inputbox.send_keys('Take car from repair')

		# When user clicks enter, page updates, and now the page lists
		# "1: Take car from repear" as an item in to-do list
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Take car from repear' for row in rows),
			"New to-do item did not appear in table"
			)

		
		# There is still a text box, inviting user to write another item in to-do list

		# User enters "Write some report tests"
		self.fail('Finish the test!')

# The page updates again and now there are 2 items in to-do list

# Site generates a URL to store the to-do list
# Info message is showing to user informing about storing to-do list at the URL

# User visits URL and verifys that to-do list is still there

if __name__ == '__main__':
	unittest.main(warnings='ignore')

