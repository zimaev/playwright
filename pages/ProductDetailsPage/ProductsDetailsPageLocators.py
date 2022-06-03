
class ProductsDetailsPageLocators:

    PRODUCT_NAME = '.product-information h2'
    CATEGORY = '.product-information p >> nth=0'
    PRICE = '.product-information span span'
    AVAILABILITY = 'text=Availability'
    CONDITION = 'text=Condition'
    BRAND = '.product-information p >> nth=3'

    # REVIEW_FORM
    NAME = "#review-form #name"
    EMAIL = "#review-form #email"
    TEXT = "#review-form #review"
    SUBMIT = "#button-review"
    ALERT_SUCCESS = ".alert-success.alert span"
