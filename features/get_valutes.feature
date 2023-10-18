Feature: returns dictionary of currencies for delta day and adds Ruble currency if flagged
  Scenario: without rouble
    Given today date
    When flag is false
    Then dictionary have currencies values for today without rub
  Scenario: with rouble
    Given yesterday date
    When flag is true
    Then dictionary have currencies values for yesterday with rub