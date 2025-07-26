from seleniumbase import BaseCase
from page_objects.home_page import HomePage


class HomeTest(HomePage): #Inheriting from  BaseCase

    def setUp(self): #This is for running anything you want to do on every test
        super().setUp()
        print("Running Before each test")

        #Login
        self.login()



        # open home page
        self.open_home_page()

    def tearDown(self):
        print("Running After each test")
        # self.click('a[href="/logout"]') #After each test logout

        super().tearDown()

    def test_home_page(self):

        #assert page title
        self.assert_title("Automation Exercise")

        #assert logo
        self.assert_element_not_visible(HomePage.logo_icon)

        #click on products and assert the url
        self.click(HomePage.api_list) # click the botton with api_list class
        api_list = self.get_current_url() #get the url of that page
        self.assert_equal(api_list, "https://automationexercise.com/api_list") # make sure the url match with this
        self.assert_true("api_list" in api_list) #make sure the api_list in the link

        self.assert_text("APIS LIST FOR PRACTICE", HomePage.api_list_header) # verify the text in the header match
        #Exercise scroll all to the bottom and assert the copyright text
        self.scroll_to_bottom()
        self.assert_text("Copyright © 2021 All rights reserved", HomePage.copyright)

    def test_menu_link(self): #test_menu_link <- we can use this to do individual test with pytest
        expected_links = ['Home',' Products','Cart','Signup / Login','Test Cases','API Testing','Video Tutorials','Contact us']

        # find menu links elements
        # if you want to use css selector - ul.nav.navbar-nav li
        # for xpath - //i[starts-with(@class, 'fa')] This is for reference only
        # -># symbol is used before id . symbol is used before class // symbol for xpath

        menu_links_el = self.find_elements(HomePage.menu)
        # to test individual test like this e.g.-> 'pytest -k "test_menu_link" -s' here -s is used to print out result
        #Loop through nav links
        for idx,menu_link in enumerate(menu_links_el):
            print(idx,menu_link.text)
            self.assertEqual(menu_link.text, expected_links[idx]) #asserting the index and the links match



