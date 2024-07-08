Feature: Search Multiple Products on OpenCart page.

  
  
  Background:
    Given launch chrome browser
    When open opencart login page

  Scenario Outline:Search Products.
    And search "<Product>"
    Then verify we are on the search "<Product>"
    And close browser
    Examples:
      | Product   |
      | Phone     |
      | Camera    |
      |Television |

  Scenario: Add to Cart.
   And search Phone product 
   Then add Phone to cart
   And verify it indeed was added 
   And close browser 


  

   
