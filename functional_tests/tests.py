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

	def test_can_start_a_list_for_one_user(self):
		# User_1 opens homapage of the inline to-do app
		self.browser.get(self.live_server_url)

		# User_1 see that page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# User_1 is presented an input text-box, inviting to enter a to-do item
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			)

		# User_1 types "Take car from repair"
		inputbox.send_keys('Take car from repair')

		# When user clicks enter, page updates, and now the page lists
		# "1: Take car from repair" as an item in to-do list
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Take car from repair')

		
		# There is still a text box, inviting user to write another item in to-do list
		# User_1 enters "Write some report tests"
		# User_1 hits "Enter"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Write some report tests')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		# The page updates again and now there are 2 items in to-do list
		self.wait_for_row_in_list_table('1: Take car from repair')
		self.wait_for_row_in_list_table('2: Write some report tests')


	def test_multiple_users_can_start_lists_at_different_urls(self):
		# User_1 starts a new to-do list
		self.browser.get(self.live_server_url)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Take car from repair')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Take car from repair')

		# Site generates a uniq URL to store the to-do list of User_1
		user1_list_url = self.browser.current_url
		self.assertRegex(user1_list_url, '/lists/.+')
		
		# User_2 opens a to-do website

		## We use new browser session to make sure that no information of User_1 is coming
		## from cookies etc
		self.browser.quit()
		self.browser = webdriver.Firefox()

		# User_2 visits homepage. There is  no sign of User_1 list
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Take car from repair', page_text)
		self.assertNotIn('Write some report tests', page_text)

		# User_2 starts a new to-do list by entering a new item
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(keys.ENTER)
		seld.wait_for_row_in_list_table('1: Buy milk')

		# User_2 gets his own URL
		user2_list_url = self.browser.current_url
		self.assertRegex(user2_list_url, '/lists/.+')
		self.assertNotEqual(user1_list_url, user2_list_url)

		# Again there is no trace of User_1 list
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Take car from repair', page_text)
		self.assertIn('Buy milk')

		self.fail('Finish the test!')

# User_1 visits URL and verifys that to-do list is still there

if __name__ == '__main__':
	unittest.main(warnings='ignore')

