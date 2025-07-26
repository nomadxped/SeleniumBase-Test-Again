from seleniumbase import BaseCase

class CartPage(BaseCase):
   #selectors
   product_add = 'a[data-product-id="37"]'
   added_alert = 'h4.modal-title.w-100'
   current_total_price = 'p.cart_total_price'

   def open_page(self):
     self.open("https://automationexercise.com/view_cart")