delivery_partner = "swiggy"

def hotel():
    item = "Naan"

    def order():
        quantity = 2
        print(f"Order placed for {quantity} {item} from {delivery_partner}")

    order()
hotel()