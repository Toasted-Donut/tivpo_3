Feature: return date with previous month of given
  Scenario: 18.10.2023
    Given date is 18.10.2023
    When fun is called1
    Then date now is 18.09.2023
  Scenario: 01.01.2023
    Given date is 01.01.2023
    When fun is called2
    Then date now is 01.12.2022
