

class CheckoutPageLocators:

    PLACE_ORDER = ".btn.btn-default.check_out"
    TEXT_AREA = '[name = "message"]'

    # DELIVERY ADDRESS
    DELIVERY_FIRST_NAME = "#address_delivery .address_firstname.address_lastname"
    DELIVERY_COMPANY = '#address_delivery .address_address1.address_address2  >> nth=0'
    DELIVERY_CITY = "#address_delivery .address_city.address_state_name.address_postcode"
    DELIVERY_COUNTY = '#address_delivery .address_country_name'
    DELIVERY_PHONE = '#address_delivery .address_phone'

    # BILLING ADDRESS
    BILLING_FIRST_NAME = "#address_invoice .address_firstname.address_lastname"
    BILLING_CITY = "#address_invoice .address_address1.address_address2 >> nth=1"
    BILLING_COMPANY = "#address_invoice .address_address1.address_address2 >> nth=0"
    BILLING_COUNTY = "#address_invoice .address_country_name"
    BILLING_PHONE = "#address_invoice .address_phone"


