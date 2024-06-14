Feature: Search Multiple Products on OpenCart page.

  
  
  Background:
    Given launch chrome browser
    when open opencart login page

  Scenario Outline:Search Products.
    and search "<Product>"
    Then verify we are on the search "<Product>"
    And close browser
    Examples:
      | Product   |
      | Phone     |
      | Camera    |
      |Television |

  Scenario: Add to Cart.
   and search Phone product 
   Then add Phone to cart
   and verify it indeed was added 
   and close browser 


  

   
