from behave import *
from hamcrest import assert_that, equal_to


@then('the response code should be "{status_code:d}"')
def step_verify_response_code(context, status_code):
    assert_that(context.response.status_code, equal_to(status_code), 'Verify status code of the response')
