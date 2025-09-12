import csv
import os
import locale



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

def list_products (products):
    for idx, product in enumerate(products, 1):
        print(f"{idx}. {product['name']} - {format_currency(product['price'])} - {product['quantity']} st")


def view_product(products, idx):
    for product in products:
        if product['id'] == idx - 1:
            return product['name'], product["price"]

def product_remove(products, id):
    for product in products:
        if product['id'] == id:
            products.remove(product)

#TODO: hur gör man så funktionen load_data returnerar products istället?
#TODO: gör så man kan se en numrerad lista som börjar på 1.
#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id
#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id

os.system('cls')

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

products = load_data('db_products.csv')


product_remove(products, 3)

add_product(products, "teslacar", "a transport veichle to move around city", 300000, 5)

while True:
    list_products(products)
    idx = int(input("välj produkt: "))
    
    product = view_product(products,idx)
    print(f"the product is {product[0]} and costs {product[1]}")
    input ("")