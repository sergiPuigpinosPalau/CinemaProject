Feature: Register Session
  In order to keep track of the sessions available for each film
  As a user
  I want to register a session in the corresponding movie

  Background: There is a registered user, a movie, a hall and a schedule set
    Given Exists a user "user" with password "password"
    And Exists a movie
      | name            |
      | Spider     |
    And Exists a hall
      | capacity            |
      | 22     |
    And Exists a schedule
      | starting_time            |
      | 18:00:00     |
      | end_time            |
      | 20:00:00     |


  Scenario: Register session
    Given I login as user "user" with password "password"
    When I register a session at the movie "Spider"
      | date            |
      | 2021-01-02  |
      | hall            |
      | 1  |
      | schedule            |
      | 1  |
    Then I'm viewing the details of the session for the movie "Spider"
      | date            |
      | 2021-01-02  |
      | hall            |
      | 1  |
      | schedule            |
      | 1  |
    And There are 1 sessions


  Scenario: Try to register dish but not logged in
    Given I'm not logged in
    When I register a session at the movie "Spider"
      | date            |
      | 2021-01-02  |
      | hall            |
      | 1  |
      | schedule            |
      | 1  |
    Then I'm redirected to the login form
    And There are 0 sessions