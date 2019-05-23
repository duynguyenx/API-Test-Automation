@collection
Feature: Create Collection successfully
  As a user, I want to create a new collection (Private or Public)

  @create_private_collection @id-1
  Scenario: User create private collection successfully
    When the user creates a new private collection
    Then the response code should be "201"
    And the create collection response json schema is valid
    And title, description and private values of response data are correct
