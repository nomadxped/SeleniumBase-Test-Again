from seleniumbase import BaseCase
class HomePage(BaseCase):
    logo_icon = "logo pull-left"
    api_list = ".apis_list"
    api_list_header = "h2.title.text-center"
    copyright = "p.pull-left"
    menu = "ul.nav.navbar-nav li"

    def open_home_page(self):
        self.open("https://automationexercise.com/")

    def login(self):
        # LOGIN
        #You can define the variables above and pass the variable instead of the value. I'm lazy so not doing it.
        self.open("https://automationexercise.com/login")
        self.send_keys('input[name="email"]', "jagigeg182@hadvar.com")
        self.send_keys('input[name="password"]', "TeroBau???")
        self.click('button[data-qa="login-button"]')