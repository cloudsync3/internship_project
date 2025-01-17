Feature: Support Community Navigation

  Scenario: User can access Whatsapp and Telegram communities
    Given Open Reelly main page
    When Enter credentials and login to the app
    Then Click on settings option
    Then Click on support option
    When Switch to the new tab
    Then Verify the right Whatsapp page opens
    And Go back to previous page
    When Click on t.me news option
    Then Verify the right page opens