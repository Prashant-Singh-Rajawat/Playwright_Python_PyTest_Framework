from Pages.BasePage import BasePage
from faker import Faker

data = Faker()
class GenerateUserData:
    @staticmethod
    def generate():
        return {
            'f_name': data.first_name(),
            'l_name': data.last_name(),
            'email_add': data.email(),
            'country_name': data.country(),
            'city_name': data.city(),
            'full_address': data.address(),
            'zip_code': data.zipcode(),
            'phone_no': data.phone_number(),
            'name': data.name(),
            'security_code': data.credit_card_security_code()
        }


class BillingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.address_drpdwn = '#billing-address-select'
        self.first_name = '#BillingNewAddress_FirstName'
        self.last_name = '#BillingNewAddress_LastName'
        self.email = '#BillingNewAddress_Email'
        self.country_id = '#BillingNewAddress_CountryId'
        self.city_field = '#BillingNewAddress_City'
        self.address = '#BillingNewAddress_Address1'
        self.zip = '#BillingNewAddress_ZipPostalCode'
        self.phone = '#BillingNewAddress_PhoneNumber'
        self.continue_bill = "//input[@onclick='Billing.save()']"
        self.in_store_pickup = '#PickUpInStore'
        self.continue_ship = "//input[@onclick='Shipping.save()']"
        self.credit_card = '#paymentmethod_2'
        self.continue_pay_method = "//input[@class='button-1 payment-method-next-step-button']"
        self.select_cc = '#CreditCardType'
        self.card_holder = '#CardholderName'
        self.card_number = '#CardNumber'
        self.expire_month = '#ExpireMonth'
        self.expire_year = '#ExpireYear'
        self.card_code = '#CardCode'
        self.continue_card = "//input[@class='button-1 payment-info-next-step-button']"
        self.confirm_btn = "//input[@value='Confirm']"
        self.continue_final = "//input[@value='Continue']"  # Not Used For Now
        self.order_details_link = 'text=Click here for order details.'
        self.pdf_invoice = 'text=PDF Invoice'
        self.pdf_button = '.button-2.pdf-order-button'

    def select_address(self):
        self.drop_down(self.address_drpdwn, 'New Address')

    def billing_address(self):
        user_data = GenerateUserData.generate()

        self.fill(self.first_name, user_data['f_name'])
        self.fill(self.last_name, user_data['l_name'])
        self.fill(self.email, user_data['email_add'])
        self.drop_down(self.country_id, 'Canada')
        self.fill(self.city_field, user_data['city_name'])
        self.fill(self.address, user_data['full_address'])
        self.fill(self.zip, user_data['zip_code'])
        self.fill(self.phone, user_data['phone_no'])
        self.click(self.continue_bill)

    def shipping_address(self):
        self.click(self.in_store_pickup)
        self.click(self.continue_ship)

    def payment_method(self):
        self.click(self.credit_card)
        self.click(self.continue_pay_method)

    def payment_information(self):
        user_data = GenerateUserData.generate()

        self.drop_down(self.select_cc, 'Master card')
        self.fill(self.card_holder, user_data['name'])
        self.fill(self.card_number, '5555 5555 5555 4444')
        self.fill(self.card_code, user_data['security_code'])
        self.click(self.continue_card)

    def confirm_order(self):
        self.click(self.confirm_btn)

    def order_details(self):
        self.click(self.order_details_link)
        self.click(self.pdf_invoice)

    def verify_billing(self):
        return self.page.locator(self.pdf_button)