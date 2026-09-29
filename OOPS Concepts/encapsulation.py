class order:

    def __init__(self , customer_name , items , total_amount , discount):
        self.customer_name = customer_name
        self.items = items
        self.__total_amount = total_amount
        self.__discount= discount


    def __calculate_final(self):
        return self.__total_amount - self.__discount

    def _get_admin_view(self):
        return {
            "Customer" : self.customer_name,
            "items" : self.items,
            "Total Amount" : f"{self.__total_amount}",
            "Discount" : f"{self.__discount}",
            "Final Amount" : f"{self.__calculate_final()}"
        }

    
    def get_customer_view(self):
        return {
            "Customer" : self.customer_name,
            "items" : self.items,
            "Total Amount" : self.__total_amount,
            "Final Amount" : self.__calculate_final()
        }

class AdminPortal:
    def show_order(self , order):
        return order._get_admin_view()

class CustomerApp:
    def show_order(self , order):
        return order.get_customer_view()


order = order ("Middhun" , ["Dosa" , "Poori"] , 400 , 120)

admin = AdminPortal()
customer = CustomerApp()


print("Admin View")
print(admin.show_order(order))

print("Customer View")
print(customer.show_order(order))