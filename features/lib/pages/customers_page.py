from .base_page import BasePage


class CustomersPageLocators:
    CLEAR_BUTTON = "#clear-button"
    SEARCH_INPUT = "#search-input"
    DROP_DOWN = "#search-column"
    MATCH_CASE = "#match-case"
    SUMMARY = "#table-resume"
    SEARCH_TERM = "#search-slogan"
    TABLE = "//table"


class CustomersPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def clear_button_click(self):
        """
        Click on Clear Filters Button.

        :return: the Button element
        """
        loop = self.context.async_context.loop
        clear_button = self.find_element(CustomersPageLocators.CLEAR_BUTTON)
        loop.run_until_complete(clear_button.click())
        return clear_button

    def set_search_input(self, search_input):
        """
        Set value to searchInput field.

        :param search_input: input which should be typed into the field
        """
        loop = self.context.async_context.loop
        loop.run_until_complete(self.context.page.type(CustomersPageLocators.SEARCH_INPUT, search_input))

    def set_search_column_drop_down_list_field(self, value):
        """
        Set value to Search Column Drop Down List field.

        :param value: String which should match with one of values visible on the dropdown
        """
        loop = self.context.async_context.loop
        loop.run_until_complete(self.context.page.select_option(CustomersPageLocators.DROP_DOWN, value))

    def set_match_case_checkbox_field(self, value):
        """
        Set Match Case Checkbox field to required value.

        :param value: boolean value of the checkbox status true - checked, false - unchecked
        """
        loop = self.context.async_context.loop
        case_checkbox = self.find_element(CustomersPageLocators.MATCH_CASE)
        checkbox_is_checked = loop.run_until_complete(case_checkbox.is_checked())
        if str(checkbox_is_checked) != value:
            loop.run_until_complete(case_checkbox.click())

    def get_summary_text(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.find_element(CustomersPageLocators.SUMMARY).inner_text())

    def get_search_term_text(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.find_element(CustomersPageLocators.SEARCH_TERM).inner_text())

    def get_search_input_text(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.find_element(CustomersPageLocators.SEARCH_INPUT).input_value())

    def get_search_results_table_text(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.find_element(CustomersPageLocators.TABLE).text_content())

    def open(self):
        application_url = self.context.config.userdata.get("applicationUrl",
                                                           "http://localhost:8080/root/sample-page/pages/index.html")
        loop = self.context.async_context.loop
        loop.run_until_complete(self.context.page.goto(application_url))
