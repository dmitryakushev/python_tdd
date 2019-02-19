from selenium import webdriver
import unittest

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
		self.fail('Finish the test!')

# User is presented a text-box, inviting to enter a to-do item

# User types "Take car from repair"

# When user clicks enter, page updates, and now the page lists
# "1: Take car from repear" as an item in to-do list

# There is still a text box, inviting user to write another item in to-do list

# User enters "Write some report tests"

# The page updates again and now there are 2 items in to-do list

# Site generates a URL to store the to-do list
# Info message is showing to user informing about storing to-do list at the URL

# User visits URL and verifys that to-do list is still there

if __name__ == '__main__':
	unittest.main(warnings='ignore')

