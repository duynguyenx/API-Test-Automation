from behave import *
from hamcrest import assert_that, equal_to
from jsonschema import *
from features.request_payload.collection import PRIVATE_COLLECTION
from features.hooks.api.data_helper import DataHelper
from features.hooks.api.collection_helper import CollectionHelper
from conf.environment_setup import EnvSetup
from features.schemas.collection.successfull_create_collection_schema import SUCCESSFUL_CREATE_COLLECTION_SCHEMA
from features.expected_responses.collection.create_collection_response import CREATE_COLLECTION_RESPONSE


@step('the user creates a new private collection')
def step_create_private_collection(context):
    context.datetime_string = DataHelper.get_unique_string_by_time()
    request_payload = PRIVATE_COLLECTION.format(datetime=context.datetime_string)
    context.response = CollectionHelper.create_company(EnvSetup.API_USER_HARD_TOKEN, request_payload)


@then("the create collection response json schema is valid")
def step_verify_create_collection_response_schema(context):
    validate(context.response.json(), SUCCESSFUL_CREATE_COLLECTION_SCHEMA)


@then("title, description and private values of response data are correct")
def step_verify_create_collection_response(context):
    actual_collection_response = {}
    response = context.response.json()
    actual_collection_response.update({"title": response['title']})
    actual_collection_response.update({"description": response['description']})
    actual_collection_response.update({"private": response['private']})

    CREATE_COLLECTION_RESPONSE["title"] = CREATE_COLLECTION_RESPONSE["title"].format(datetime=context.datetime_string)

    assert_that(actual_collection_response, equal_to(CREATE_COLLECTION_RESPONSE),
                'Verify return values of response')
