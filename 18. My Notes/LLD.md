# SOLID Principle
# Advantages of Solid Priciples
 - Avoid duplicate code
 - Easy to maintain
 - Easy to understand
 - Flexible software
 - Reduce Complexity

1. Single Responsibility Principle
- A class should have only one reason to change

class Marker:
    def __init__(self, name, color, year, price):
       self.name = name
       self.color = color
       self.year = year
       self.price = price

# Invoice has-a marker Relationship    

class Invoice:
    def __init__(self, marker_obj, quantity):
       self.marker = marker_obj
       self.quantity = quantity
    
    def calculate_totale(self):
       return self.marker.price * self.qunatity
    
    def print_invoice(self):
       pass
    
    def save_to_db(self):
       pass

# is this following single resposibility principles - NO
- Only one Reason to change
- lets add gst, discount than calulation logic got changes
- Invoice class is going to change because change in calculation Logic
- save to db --> save to File again class need to change
more than one reason to change !.e 3 but SRP said only one reason to change This Invoice Class
is not Following SRP Principles

# How to correct it
Make class Like that only one Reason ho change hone ka
class Invoice:
    def __init__(self, marker_obj, quantity):
       self.marker = marker_obj
       self.quantity = quantity
    
    def calculate_totale(self):
       return self.marker.price * self.qunatity

class InvoicePrinter
   def print()

class InvoiceDao:
   def save_to_db()

Now thease class have single reason to change
- InvoicePrinter, Lets say want to print some other things different type of invoice
  that is also possible
- InvoiceDao - save in db or file - save karna kam haii iska
- Invoice - ka kam calculate the price, if anything change in calculation logic
  Than only class will change not impact other classes

# Advantages
- Easy to maintains
- 
   

# O - Open/closed Priciples
Open for Extension
Closed for Modification
EG:

Dao = data axcess objects 
class InvoiceDao:
   def save_to_db()

- This is already tested and Live, taking Live Traffic
- new Req - save to File 
- write one methods to save in File 

class InvoiceDao:
   def save_to_db()
   def save_to_file() 
   - not following open closed principles
   - why modify, just extend if extra capability required 
   
   InvoiceDao
     1. DB
     2. File
    
    # implemnts the interface
    class DBInvoioceDao(InvoiceDao)
      def save(self, invoice_obj):
        # saving to db
    class FileInvoioceDao(InvoiceDao)
      def save(self, invoice_obj):
        # saving to File
    # In future if some other came just extend it


# L - Liskob Substitution Principles

- if class B is subtypes of class A, Than we should able to replace
  objects of A with B without breaking the behaviour of the Programe

  Subclass should extend the capability of Parent class not narrow it Down

  Interfcae # abstarct class

  class Bike:
      def turnOnEngine() pass
      def accelarate() pass

  # extending the class
  class MotorCycle(Bike):
    
    def __init__(self):
       self.is_engine_on = True
       self.speed = 0
    
    def turnOnEngine(self):
        self.is_endine_on = True
    
    def accelarate():
       self.speed = self.speed + 10

- code behave as if turn on engine, speed increase it will work

class BiCycle(Bike):
    
    def __init__(self):
       self.is_engine_on = True
       self.speed = 0
    
    def turnOnEngine(self):
        raise NotImplemnted() # narrow parent class capbaility so breaking LSP
    
    def accelarate():
       self.speed = self.speed + 10


# I - Interfcae Segmented Priciples
- Interface should be such that client should not implement Unnecessary functions
  They do not need

- Interfcae - abstarct class
class RestaurantEmployee():
    def washDishes():
      pass
    def ServerCustome():
      pass
    def cook_Food():
       pass

class Waiter(RestaurantEmployee):
    def washDishes():
      # not my job
      pass
    def ServerCustome():
      print("")
    def cook_Food():
       # not my job
    
    # Breaking ISP - washDishes, cook_Food not required

Segmented - xota xota tukde me interfcae ko divide kar do taa ki client need not
            to implemnt unnecssary Functions
        
        WaiterInterface()  
          - ServerCustomer()
          - takeOrder()
        
        ChefInterfcae()
          - CookFood()
          - decideMenu()

# Dependecy Inversion Principles
- class should depend on Interfcae rather than Concrete Class

KeyBorad Interfcae  -- Interfaces(abstract class)
 - WireedKeyboard - Concrete class
 - BluthoothKeyboard -  - Concrete class
Mouse Interfcae
 - WiredMouse  - Concrete class
 - BluthoothMouse  - Concrete class

class MackBook:
   def MacBook(self):
     # this is wrong - assign concrete class itself
     # if in future want to make bluthooth than can't possiblen assigned concrete class itself
     # not follow dependecy inversion principles
     self.keyboard = WireedKeyboard()
     self.wiredMouse = WiredMouse()

# To Fix this
class MackBook:
   # keyboard - can send wired keyboard obj or Bluthooth keyword
   # can send WiredMouse or BluthoothMouse
   # can capable to take any objects
   # depend on interfcae rather on concrete class
   def MacBook(self, keyboard, Mouse):
     # take interfcae(abstarct objects), not concrete one !.e KeyBorad Interfcae, Mouse Interfcae
     self.keyboard = keyboard
     self.Mouse = Mouse
   
   
    
   
   
          

    


   
    


