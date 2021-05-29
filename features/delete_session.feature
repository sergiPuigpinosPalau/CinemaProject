Feature: Delete Session
  In order to get rid of unwanted or outdated sessions
  As a user
  I want to delete a session

  Background: There is a registered session and a user
    Given Exists a user "user" with password "password"
    And Exists a movie
      | name   |
      | Spider |
    And Exists a hall
      | capacity |
      | 22       |
    And Exists a hall
      | capacity |
      | 38       |
    And Exists a schedule
      | starting_time | end_time |
      | 18:00:00      | 20:00:00 |
    And Exists a session for the movie "Spider"
      | duration | date       | hall_id | schedule_id |
      | 2:00:00  | 2021-01-02 | 1       | 1           |


  Scenario: Delete session
    Given I login as user "user" with password "password"
    Then I'm viewing the details of the session for the movie "Spider"
      | duration | date         | hall    | schedule                           |
      | 2:00:00  | Jan. 2, 2021 | Hall: 1 | Schedule from 18:00:00 to 20:00:00 |
    And I delete the current session
    And There are 0 sessions

  Scenario: Try to delete a session but not logged in
    Given I'm not logged in
    Then I'm viewing the details of the session for the movie "Spider"
      | duration | date         | hall    | schedule                           |
      | 2:00:00  | Jan. 2, 2021 | Hall: 1 | Schedule from 18:00:00 to 20:00:00 |
    Then There is no "delete_session" link available