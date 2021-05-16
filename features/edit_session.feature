Feature: Edit Session
  In order to keep updated the different sessions available for a movie
  As a user
  I want to edit a session

  Background: There is a registered session and a user
    Given Exists a user "user" with password "password"
    And Exists a movie
      | name   |
      | Spider |
    And Exists a session
      | date       | hall | schedule |
      | 2021-01-02 | 1    | 1        |

  Scenario: Edit session
    Given I login as user "user" with password "password"
    Then I'm viewing the details of the session for the movie "Spider"
      | date       | hall | schedule |
      | 2021-01-02 | 1    | 1        |
    And I edit the current session
       | hall |
      | 2    |
    Then I'm viewing the details of the session for the movie "Spider"
      | date       | hall | schedule |
      | 2021-01-02 | 2    | 1        |
    And There are 1 sessions

  Scenario: Try to edit dish but not logged in
    Given I'm not logged in
    Then I'm viewing the details of the session for the movie "Spider"
      | date       | hall | schedule |
      | 2021-01-02 | 1    | 1        |
    Then There is no "edit" link available
