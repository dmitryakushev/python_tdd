from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

	def test_cannot_add_empty_list_items(self):
		# User goes to the home page and accidentally tries to submit
		# an empty list item. She hits Enter on the empty input box

		# The home page refreshes, and there is an error message saying
		# that list items cannot be blank

		# User tries again with some text for the item, which now works

		# Perversely, user now decides to submit a second blank list item

		# User receives a similar warning on the list page

		# And user can correct it by filling some text in

		self.fail('finish the tests')



if __name__ == '__main__':
	unittest.main(warnings='ignore')

