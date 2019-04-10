from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

	def test_cannot_add_empty_list_items(self):
		# User goes to the home page and accidentally tries to submit
		# an empty list item. She hits Enter on the empty input box

		self.browser.get(self.live_server_url)
		self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)


		# The home page refreshes, and there is an error message saying
		# that list items cannot be blank

		self.wait_for (lambda: self.assertEqual(
			self.browser.find_element_by_css_selector('.has-error').text,
			"You can't have an empty list item"
			))

		# User tries again with some text for the item, which now works
		self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
		self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy milk')

		# Perversely, user now decides to submit a second blank list item
		self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

		# User receives a similar warning on the list page
		self.wait_for(lambda: self.assertEqual(
			self.browser.find_element_by_css_selector('.has-error').text,
			"You can't have an empty list item"
			))

		# And user can correct it by filling some text in
		self.browser.find_element_by_id('id_new_item').send_keys('Make tee')
		self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy milk')
		self.wait_for_row_in_list_table('2: Make tea')



if __name__ == '__main__':
	unittest.main(warnings='ignore')

