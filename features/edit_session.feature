Feature: Edit Session
  In order to keep updated the different sessions available for a movie
  As a user
  I want to edit a session

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

  Scenario: Edit session
    Given I login as user "user" with password "password"
    Then I'm viewing the details of the session for the movie "Spider"
      | duration | date         | hall    | schedule                           |
      | 2:00:00  | Jan. 2, 2021 | Hall: 1 | Schedule from 18:00:00 to 20:00:00 |
    And I edit the current session
      | id_hall |
      | 2       |
    Then I'm viewing the details of the session for the movie "Spider"
      | duration | date         | hall    | schedule                           |
      | 2:00:00  | Jan. 2, 2021 | Hall: 2 | Schedule from 18:00:00 to 20:00:00 |
    And There are 1 sessions

  Scenario: Try to edit a session but not logged in
    Given I'm not logged in
    Then I'm viewing the details of the session for the movie "Spider"
      | duration | date         | hall    | schedule                           |
      | 2:00:00  | Jan. 2, 2021 | Hall: 1 | Schedule from 18:00:00 to 20:00:00 |
    Then There is no "Edit" link available
