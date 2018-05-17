from behave import *
from jsonschema import *
from features.schemas.authenticate.successfull_athentication_schema import SUCCESSFUL_LOGIN_SCHEMA


@then('I verify that the user authentication response schema is valid')
def step_verify_the_user_gets_the_token_structure(context):
    try:
        validate(context.client_response.json(), SUCCESSFUL_LOGIN_SCHEMA)
    except ValidationError as e:
        raise SchemaError('The authentication response is invalid', e)
