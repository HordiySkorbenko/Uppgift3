import csv
import os
import locale
from bcolors import bcolors

def format_currency(value):
    return locale.currency(value,grouping=True)


def load_data(filename): 
    products = []           #lista
    with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products

def save_product(filepath, products): 
    print(f"sparar produkter ...")
    
    try :
        with open(filepath, mode = "w", newline='')  as file:
            writer = csv.DictWriter(file, fieldnames = ["id", "name", "desc", "price", "quantity"]) 
            writer.writeheader()
            writer.writerows(products)  
            print("OK")
    except Exception as error_code:
        print("Fel")
        
        if isinstance (error_code, OSError) and error_code.errno == 13:
            return ("Filen är skriv skyddad")
        else:
            return (f"Felet är {error_code}")

def add_product(products, name, desc, price, quantity):
    last_id = max(products, key = lambda x : x['id'])["id"]
    
    products.append(
        {
            "id": last_id + 1,
            "name": name,
            "desc": desc,
            "price": price,
            "quantity": quantity
        }
    )
        
        
    return products

def change_product(products, idx, name, price, desc, quantity ):
    for product in products:
        if product['id'] == idx:
                product['name'] = name
                product['price'] = price
                product['desc'] = desc
                product['quantity'] = quantity
            
    return products
            

def list_products(products):
    for idx, product in enumerate(products, 1): print(bcolors.YELLOW + f"{idx}. {product['name']} - {format_currency(product['price'])} - {product['quantity']} st")

def view_product(products, idx):
    for product in products:
        if product['id'] == idx - 1:
            return product['name'], product["price"]

def product_remove(products, id):
    for product in products:
        if product['id'] == idx - 1:
            products.remove(product)
            return product
    return None

def count_stats(products):
    total_value = 0
    for product in products:
        total_value += product['price'] * product['quantity']
        print (f"{product["name"]} --> {product["price"]} * {product['quantity']} = {product["price"] * product['quantity']}")
        print(f"den totala prisen nu är {total_value}")
    return total_value

os.system('cls')

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

products = load_data('db_products.csv')


while True:
    list_products(products)
    choice = int(input(bcolors.CYAN + bcolors.BOLD + """Välj vad du vill göra:
1 : Hitta en produkt
2 : Skriv ut alla produkter
3 : Lägg till produkt
4 : Ta bort produkt
5 : Ändra produkt
6 : Se statistik
> """))
    if choice == 1 :
        list_products(products)
        idx = int(input("välj produkt: "))
        product = view_product(products,idx)
        print(f"the product is {product[0]} and costs {product[1]}")
        
    elif choice == 2 :    
        list_products(products)
    
    elif choice == 3 :
        namn = input("skriv namn på produkten du vill lägga till ")
        desc = input("skriv beskrivning på produkten du vill lägga till ")
        price = float(input("skriv priset på produkten du vill lägga till "))
        quantity = int(input("skriv mängden av produkten det finns/ska finnas "))
        add_product(products, namn, desc, price, quantity )
        save_product('db_products.csv', products)
    
    elif choice == 4 :
        idx = int(input("Välj produkt att ta bort: "))
        removed = product_remove(products, idx)
        if removed:
            print(f"Du tog bort {removed['name']} från listan.")
            save_product('db_products.csv', products)
        else:
            print("Ingen produkt med det ID:t hittades.")
            
        
        
    elif choice == 5 :
        idx = int(input("välj produkt att ändra "))
        namn = input("skriv namn på produkten du vill ändra annars skriv - ")
        desc = input("skriv beskrivning på produkten du vill ändra annars skriv - ")
        price = float(input("skriv priset på produkten du vill ändra annars skriv - "))
        quantity = int(input("skriv mängden av ändrad produkt det finns/ska finnas annars skriv - "))
        change_product(products, idx, namn, price, desc, quantity )
        list_products(products)
        save_product('db_products.csv', products)
        
    elif choice == 6:
        print(f"Den totala prisen av alla produkter i lagern är {count_stats(products)}")
        