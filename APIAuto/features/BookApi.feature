# Created by kp at 15-12-2020
Feature: Verify if books are added and deleted using Library API
  @lib
  Scenario: Verify add book functionality
    Given Book details which needs to be added to library
    When we execute the AddBook POSTAPI method
    Then book is successfully added
    And Status code of response should be 200

  @lib
  Scenario Outline: Verify ADD book API functionality
    Given the book details with <isbn> and  <aisle>
    When we execute the AddBook POSTAPI method
    Then book is successfully added
      Examples:
      |isbn   | aisle |
      |KJ09LL | 98    |
      |Kjo12ll|89     |