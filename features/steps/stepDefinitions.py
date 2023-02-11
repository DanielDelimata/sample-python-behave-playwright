from assertpy import assert_that
from behave import given, when, then

from features.lib.pages.customers_page import CustomersPage


@given(u'The user is on the page')
def the_user_is_on_the_page(context):
    customers_page = CustomersPage(context)
    customers_page.open()
    context.search_summary_at_very_beginning = customers_page.get_summary_text()


@when(u'the user enters the value "{value}" in the text-input')
def the_user_enters_the_value_in_the_text_input(context, value):
    customers_page = CustomersPage(context)
    customers_page.set_search_input(value)


@when(u'the user selects value "{value}" in the drop-down')
def the_user_selects_value_in_the_drop_down(context, value):
    customers_page = CustomersPage(context)
    customers_page.set_search_column_drop_down_list_field(value)


@when(u'the user sets case sensitivity switch to "{value}"')
def the_user_sets_case_sensitivity_switch_to(context, value):
    customers_page = CustomersPage(context)
    customers_page.set_match_case_checkbox_field(value)


@then(u'the user should see the following result summary "{value}"')
def the_user_should_see_the_following_result_summary(context, value):
    customers_page = CustomersPage(context)
    summary_text = customers_page.get_summary_text()
    assert_that(summary_text).is_equal_to(value)


@then(u'the user should see that the search term is "{value}"')
def the_user_should_see_that_the_search_term_is(context, value):
    customers_page = CustomersPage(context)
    search_term_text = customers_page.get_search_term_text()
    assert_that(search_term_text).starts_with(value)


@when(u'the user clears filters')
def the_user_clears_filters(context):
    customers_page = CustomersPage(context)
    customers_page.clear_button_click()


@then(u'the user should see that search criteria are cleared')
def the_user_should_see_that_search_criteria_are_cleared(context):
    customers_page = CustomersPage(context)
    assert_that(customers_page.get_search_input_text()).is_empty()


@then(u'the user should see that the search result summary is as in the very beginning')
def the_user_should_see_that_the_search_result_summary_is_as_in_the_very_beginning(context):
    customers_page = CustomersPage(context)
    summary_text = customers_page.get_summary_text()
    assert_that(summary_text).is_equal_to(context.search_summary_at_very_beginning)


@then(u'the user should see that the search results are as follows: "{value}"')
def the_user_should_see_that_the_search_results_are_as_follows(context, value):
    customers_page = CustomersPage(context)
    result = customers_page.get_search_results_table_text()
    assert_that(" ".join(result.split())).is_equal_to(value)
