Feature: return date from given time delta and start date
  Scenario: step down from today
    Given start date is today
    When step back is 5 days
    Then date now is 5 days back
  Scenario: step back from 12.03.2023
    Given start date is 12.03.2023
    When step back is 4 days
    Then date now is 8 march 2023