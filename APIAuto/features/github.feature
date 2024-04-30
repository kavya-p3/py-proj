# Created by kp at 15-12-2020
Feature: GitHub API validation

  Scenario: Session management check
    Given I have github cred
    When I hit getRepo API of github
    Then Status code of response should be 200