from playwright.sync_api import expect
from pages.BasePage import BasePage
from pages.ContactUsPage.ContactUsPageLoators import ContactUsPageLocator


class ContactUsPage(BasePage):

    def fill_form(self, message):
        self.type(ContactUsPageLocator.NAME, message.name)
        self.type(ContactUsPageLocator.EMAIL, message.email)
        self.type(ContactUsPageLocator.SUBJECT, message.subject)
        self.type(ContactUsPageLocator.MESSAGE, message.message)
        # self.page.locator("input[name=\"upload_file\"]").set_input_files("activiti.txt")
        self.click(ContactUsPageLocator.SUBMIT_BUTTON)
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.page.locator("text=Submit").click()

    def visible_success_message(self):
        expect(self.page.locator(ContactUsPageLocator.SUCCESS_MSG)).to_be_visible()
        expect(self.page.locator(ContactUsPageLocator.SUCCESS_MSG)).to_have_text('Success! Your details have been submitted successfully.')

    def visible_form(self):
        expect(self.page.locator(ContactUsPageLocator.GET_IN_TOUCH)).to_be_visible()
        expect(self.page.locator(ContactUsPageLocator.GET_IN_TOUCH)).to_have_text('Get In Touch')

