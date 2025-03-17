class Product:
    # Class variable to store all products
    product_list = []

    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def create_product(self, product_id, name, price, stock):

        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        Product.product_list.append((self.product_id, self.name, self.price, self.stock))
        print(f"Product {self.name} with ID {self.product_id} created successfully.")

    @classmethod
    def read_product(cls):
        """Read all products in the product list."""
        return cls.product_list

    @classmethod
    def update_product(cls, product_id, name=None, price=None, stock=None):
        """Update the details of an existing product."""
        for i, product in enumerate(cls.product_list):
            if product[0] == product_id:
                updated_product = list(product)
                if name:
                    updated_product[1] = name
                if price:
                    updated_product[2] = price
                if stock:
                    updated_product[3] = stock
                cls.product_list[i] = tuple(updated_product)  # Replace the old product with the updated one
                print(f"Product {product_id} updated successfully.")
                return True
        print(f"Product with ID {product_id} not found.")
        return False

    @classmethod
    def delete_product(cls, product_id):
        """Delete a product from the list."""
        for i, product in enumerate(cls.product_list):
            if product[0] == product_id:
                del cls.product_list[i]
                print(f"Product {product_id} deleted successfully.")
                return True
        print(f"Product with ID {product_id} not found.")
        return False

    @classmethod
    def search(cls,name):
        c=[]
        for i,p in enumerate(cls.product_list):
            if p[1]==name:
                c.append(p[0])


        return c

    @classmethod
    def product_availability(cls):
        stocks=[]
        for i,s in enumerate(cls.product_list):
            if s[3]>0:
                stocks.append(s[1])
            else:
                print("Out of stock")

        return stocks

    @classmethod
    def sort_products(cls):
        sorted_products= sorted(cls.product_list)
        return sorted_products


# Testing the Product Management System

# Creating instances of the Product class
product1 = Product(101, "Laptop", 999.99, 50)

product2 = Product(102, "Smartphone", 499.99, 100)
product3 = Product(103, "Headphones", 79.99, 200)
product4 = Product(101, "Laptop", 999.99, 50)

# Create products and add them to the product list
product1.create_product(101, "Laptop", 999.99, 50)
product2.create_product(102, "Smartphone", 499.99, 100)
product3.create_product(103, "Headphones", 79.99, 200)
product4.create_product(101, "Laptop", 999.99, 50)

print("\nsearchedproducts are:")
print(Product.search("Laptop"))

print(f"Available stocks with product name :", ','.join(Product.product_availability()))

print("sorted_products",Product.sort_products())
print("\nAll Products:")
for product in Product.read_product():
    print(product)


print("\nUpdating Product 102 (Smartphone) stock to 120 and price to 550.00:")
Product.update_product(102, stock=1777720, price=550.00)


print("\nAll Products after Update:")
for product in Product.read_product():
    print(product)


print("\nDeleting Product 103 (Headphones):")
Product.delete_product(103)

# Read all products again after delete
print("\nAll Products after Deletion:")
for product in Product.read_product():
    print(product)
