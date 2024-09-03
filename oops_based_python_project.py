import random
class store:
    stock = {"laptop":{"Dell":[1, 50000]},"desktop":{"Dell":[1, 10000]}}
    opening_bal = {"card":0,"cash":0}
    def updatestock(self,item, brand, qty, price):
        self.stock[item][brand]=[qty,price]
        return True
    def payment(self, payment_mode, item, brand, qty):
        item_price = self.stock[item][brand][1]
        if payment_mode=='cash':
            print("Price of the item(s) are ",int(item_price)*int(qty))
            print("Discount applied ", int(item_price)*int(qty)*.1)
            print("Payable Amount is ",int(item_price)*int(qty)*.9)
        elif payment_mode=='card':
            print("Price of the item(s) are ",int(item_price)*int(qty))
            print("Discount applied ", int(item_price)*int(qty)*.05)
            print("Payable Amount is ",int(item_price)*int(qty)*.95)
        else:
            print("enter valid payment mode")
        
    def list_items(self):
        for category, brands in self.stock.items():
            print(f"Category: {category}")
            for brand, details in brands.items():
                if isinstance(details, list):
                    print(f"  Brand: {brand}, Price: {details[1]}")
                else:
                    print(f"  Brand: {brand}, Price: {details}")
        
    def order_prepare(self,payment_mode, item, brand, qty):
        ordernumber = random.randint(1000,10000)
        print("Your order number is: ", ordernumber)
        print("You have selected {} qty of {} {}".format(qty,brand, item))
        self.checkstock(item, brand, qty, payment_mode)      
    def stockupdate(self,item, brand, qty):
        self.stock[item][brand][0] = self.stock[item][brand][0]-int(qty)
    def checkstock(self, item, brand, qty, payment_mode):
        if self.stock[item][brand][0]>=int(qty):
            print("Requested item is available, please go ahead with further details")
            self.orderprocessing(item, brand, qty, payment_mode)
        else:
            print("Requested item is not available at this moment, please try after sometime")
    def orderprocessing(self,item, brand, qty, payment_mode):
        self.payment(payment_mode, item, brand, qty)
        self.stockupdate(item, brand, qty) 
    def support(self):
        print("please contact thesehere")

class customer(store):
    def support(self):
        print("please contact here")
        super().support()

cust = customer()
print("welcome to the Gupta Ji world \n")
while True:
    print("Enter: 1 for List the items")
    print("Enter: 2 for update the item list")
    print("Enter: 3 for buy a product")
    print("Enter: 4 for exit the process")
    usermenuchoice = input()
    if usermenuchoice == "1":
        print("\n You have selected LIst the items menu : We have the following quantities in stock\n")
        cust.list_items()
    elif usermenuchoice == "2":
        print("Please enter the category[laptop/desktop] you want to add")
        user_cat = input()
        print("Please enter the brand you want to add")
        user_brand = input()
        print("Please enter the quantity you want to add")
        user_qty = input()
        print("Please enter the price you want to add")
        user_price = input()
        cust.updatestock(user_cat,user_brand,user_qty,user_price)
    elif usermenuchoice == "3":
        print("Please enter the category[laptop/desktop] you want to buy")
        user_cat_buy = input()
        print("Please enter the brand you want to buy")
        user_brand_buy = input()
        print("Please enter the quantity you want to buy")
        user_qty_buy = input()
        print("Please enter the payment mode [card/cash] you would like to select")
        user_paymode = input()
        cust.order_prepare(user_paymode,user_cat_buy,user_brand_buy, user_qty_buy)
        cust.support()
    elif usermenuchoice == "4":
        quit()




