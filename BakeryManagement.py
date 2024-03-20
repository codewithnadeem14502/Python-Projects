import json

filename = "orders.txt"


def load_all_order():
    try:
        # open file in read format and return json as load file
        with open(filename,'r') as file:
         return json.load(file)
    except FileNotFoundError:
        return []
    

def save_order(orders):
    with open(filename,'w') as file:
        json.dump(orders,file)

def list_all_orders(orders):
    print('*'*80)
    print('*'*80)
    print("\t \t List of Orders")
    print('*'*80)
    print('*'*80)
    # print("orders type : ",type(orders))
    print('\n')
    ordersSize = len(orders)
    if ordersSize == 0 : 
        print("NO DATA IS THERE")

    for index, order in enumerate(orders, start=1):
     print(f"{index}) orderID : {order['orderID']} || Customer_Name : {order['customer_name']} || Item : {order['item']} || Quantity : {order['Quantity']}")
   
    print('\n')
    print('*'*80)   

def  create_order(orders):
    orderID = input("Enter OrderID : ")
    Customer_Name = input("Enter Customer_Name : ")
    Item = input("Enter Item : ")
    Quantity = input("Enter Quatity : ")

    orders.append({"orderID" :orderID,"customer_name" :Customer_Name ,'item':Item ,"Quantity":Quantity})

    save_order(orders)
def  update_order(orders):
    list_all_orders(orders)

    index = int(input("Enter Index of the order : "))

    if index >= 1 and index <=  len(orders):
        new_orderID = input("Enter new OrderID : ")
        new_Customer_Name = input("Enter new Customer_Name : ")
        new_Item = input("Enter new Item : ")
        new_Quantity = input("Enter new Quatity : ")
    

        print("Your Order Details Updated Successfully")
        print('*'*80)
        print(orders[index-1])
        print('*'*80)
        orders[index-1] ={"orderID" :new_orderID,"customer_name" :new_Customer_Name ,'item':new_Item ,"Quantity":new_Quantity}

        save_order(orders)

    else : 
        print('*'*80)   
        print('\n')
        print("\t \t Invalid Index ")
        print('\n')
        print('*'*80)   

def  delete_order(orders):
    list_all_orders(orders)
    index = int(input("Enter the Index : "))

    if index >= 1 and index <= len(orders):
        print("Your Order Deleted  Successfully")
        print('*'*80)
        print(orders[index-1])
        print('*'*80)
        del orders[index-1]
        save_order(orders)
    else :
        print('*'*80)   
        print('\n')
        print("\t \t Invalid Index ")
        print('\n')
        print('*'*80)   

def main():
    orders=load_all_order()
    # orders = []
    print("Hello Nadeem")
    while(True):
        print('\n')
        print('*'*80)   
        print("\t \t Bakery Manager System ")
        print('*'*80)   
        print('\n')
        print("\t  1) List all orders")
        print("\t  2) Create new order")
        print("\t  3) Update a order")
        print("\t  4) Delete a order")
        print("\t  5) Exit the app")
        print('\n')
        print('*'*80)   
        choice = input("Enter your option :")

        match choice:
            case '1':
                 list_all_orders(orders)
            case '2':
               create_order(orders)
            case '3':
                update_order(orders)
            case '4':
                delete_order(orders)
            case '5':
                break
            case _:
                print("\n Invalid choice, please try again") 




if __name__ == "__main__" :
    main()
