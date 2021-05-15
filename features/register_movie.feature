Feature: Register Movie
  In order to keep track of the movies the cinema has
  As a user
  I want to register a movie

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register movie
    Given I login as user "user" with password "password"
    When I register a movie
      | name        |
      | Spider  |
    Then I'm viewing the details page of a movie
      | name        |
      | Spider |
    And There are 1 movies

  Scenario: Try to register a movie but not logged in
    Given I'm not logged in
    When I register a movie
      | name        |
      | Spider |
    Then I'm redirected to the login form
    And There are 0 movies