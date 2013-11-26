Feature: Test SendGrid Mail API
    I'd like to test out all the features of the Mail API
    First I'm going to test it by sending an email that just has the required fields
    And then I will expand from there
    
Scenario: Test the required fields
    When I fill in the fields to, from, subject, and text
    Then make the mail.send.json call
    I should receive a successful response
    
Scenario: Test all the fields
    When I fill out all the fields of the Mail API
    Then make the mail.send.json call
    I should receive a successful response