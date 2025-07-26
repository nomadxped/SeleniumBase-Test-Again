from page_objects.cart_page import CartPage

class CartTest(CartPage):

    def setUp(self):
        super().setUp()
        self.open("https://automationexercise.com/")

    def test_add_to_cart(self):
        #add item to the cart
        self.click(self.product_add)
        # assert the product is added to the cart
        self.assert_text("Added", self.added_alert) #successed
        #open Cart Page
        self.open_page()

        #get_the current_subtotal
        text = self.get_text(self.current_total_price)
        print(text)

        #change cart quantity
        #Not possible in this site

        #To wait few seconds while something loading
        #time.slee(5) option-1 . This is bad practice
        #option-2
        # self.wait_for_element_visible(selector_of_loading_element)
        # self.wait_for_element_not_visible(selector_og _loading_element)
        # option-3
        # self.wait_for_text()


        #asset subtotal tobe different than the original subtotal