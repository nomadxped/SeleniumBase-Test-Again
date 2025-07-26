from selenium.webdriver import Keys
from seleniumbase import BaseCase



class ContactTest(BaseCase):
    def test_contact_page(self):
        #open page
        self.open("https://automationexercise.com/contact_us")

        #fill in all the fields
        self.send_keys('input[name = "name"]', 'Test Name')
        self.send_keys('input[name = "email"]', 'testmail@lyang.com')
        self.send_keys('input[name = "subject"]', 'AutomationExercise')
        self.send_keys('textarea[name = "message"]', 'Test Message For You')

        #click the submit button
        self.click('input[name = "submit"]')





        # verify submit message
        self.assert_text("Success! Your details have been submitted successfully.", ".status.alert.alert-success")