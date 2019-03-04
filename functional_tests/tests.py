from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()


	def wait_for_row_in_list_table(self, row_text):
		start_time = time.time()
		while True:
			try:
				table = self.browser.find_element_by_id('id_list_table')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except(AssertionError, WebDriverException) as e:
				if time.time() - start_time > MAX_WAIT:
					raise e
				time.sleep(0.5)

	def test_can_start_a_list_and_retrieve_it_later(self):
		# User opens homapage of the inline to-do app
		self.browser.get(self.live_server_url)

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
		# "1: Take car from repair" as an item in to-do list
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Take car from repair')

		
		# There is still a text box, inviting user to write another item in to-do list
		# User enters "Write some report tests"
		# User hits "Enter"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Write some report tests')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		# The page updates again and now there are 2 items in to-do list
		self.wait_for_row_in_list_table('1: Take car from repair')
		self.wait_for_row_in_list_table('2: Write some report tests')

		# Site generates a URL to store the to-do list
		# Info message is showing to user informing about storing to-do list at the URL
		self.fail('Finish the test!')

# User visits URL and verifys that to-do list is still there

if __name__ == '__main__':
	unittest.main(warnings='ignore')

