from Methods.CreateCustomer import *
from Methods.CreatePaymentMethod import *
# This is the CLI for interacting with our DB
print("""\
.----.   .--.  .-. .-. .---.   .--.  .---.  .----. .-. .-.
| {}  } / {} \ |  `| |/   __} / {} \{_   / /  {}  \|  `| |
| {}  }/  /\  \| |\  |\  {_ }/  /\  \/    }\      /| |\  |
`----' `-'  `-'`-' `-' `---' `-'  `-'`---'  `----' `-' `-'
                                                      """) 
print("""                    
      	    =*===
           $.  . $$$
           $ <    D$$
           $ __  $$$
     ,     $$$$  |
    ///; ,---' _ |----.
     \ )(           /  )
     | \/ \.   '  _.|  \              $
     |  \ /(   /    /\_ \          $$$$$
      \ /  (       / /  )         $$$ $$$
           (  ,   /_/ ,`_,-----.,$$  $$$
           |   <----|  \---##     \   $$
           /         \\\           |    $
          '   '                    |
          |                 \      /
          /  \_|    /______,/     /
         /   / |   /    |   |    /
        (   /--|  /.     \  (\  (_
         `----,( ( _\     \ / / ,/
               | /        /,_/,/
              _|/        / / (
             / (        ^-/, |
            /, |          ^-   
 """)
firstPage = input("Hello client developer! I am Bangazon the Centaur. I will be your virtual guide.")
nextPage = input("Press Enter to begin your journey.")

# Initiate a loop 
while True: 

  print(""" Enter a Number: 

      ******************************
         WELCOME TO BANGAZON API
      ******************************
      1.     Create a customer account
      2.     Choose active customer
      3.     Create Payment Option
      4.     Add a product to shopping cart 
      5.     Complete an Order
      6.     See product Popularity
      7.     Leave Bangazon
      """)
  # Store input values to pass as parameters in a new Customer argument 
  try:

    choice = int(input(">"))

    if choice == 1: 

      Customer.add_new()
      
    elif choice == 2:

      Customer.change_status()

    elif choice == 3: 


      print("Create a payment type:")  
      nameOnCard = input("Enter name on card:") 
      cardType = input("Card type:")
      cardNumber = input("Card number:") 
      expDate = input("Exp. Date:") 
      cvv = input('CVV:') 
      customer = Customer.get_active_customer() 
      newPaymentType = PaymentMethod(nameOnCard, cardType, cardNumber, expDate, cvv, customer)
      newPaymentType.save(newPaymentType)
      print("Payment Type Added! Great work.")
  
  except ValueError: 
    print("ERROR")



                                                            
                                                            
                                                            