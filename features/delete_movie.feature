Feature: Delete Movie
  In order to get rid of unwanted or outdated movies
  As a user
  I want to delete a movie

  Background: There is a registered movie and a user
    Given Exists a user "user" with password "password"
    And Exists a movie
      | name   |
      | Spider |

  Scenario: Delete movie
    Given I login as user "user" with password "password"
    Then I'm viewing the details page of a movie
      | name        |
      | Spider |
    And I delete the current movie
    And There are 0 movies

  Scenario: Try to delete a movie but not logged in
    Given I'm not logged in
    Then I'm viewing the details page of a movie
      | name        |
      | Spider |
    And I delete the current movie
    Then I'm redirected to the login form
    And There are 1 movies