
product_list = []

def add_product(product_name):
    """Add a product to the product list."""
    product_list.append(product_name)
    print(f"Product '{product_name}' added to the list.")

def remove_product(product_name):
    """Remove a product from the product list."""
    if product_name in product_list:
        product_list.remove(product_name)
        print(f"Product '{product_name}' removed from the list.")
    else:
        print(f"Product '{product_name}' not found in the list.")

def update_product(old_name, new_name):
    """Update a product name in the product list."""
    if old_name in product_list:
        index = product_list.index(old_name)
        product_list[index] = new_name
        print(f"Product '{old_name}' updated to '{new_name}'.")
    else:
        print(f"Product '{old_name}' not found in the list.")

product_details = {}

def add_product_details(product_name, quantity, price):
    """Add details for a product."""
    product_details[product_name] = {'quantity': quantity, 'price': price}
    print(f"Details for product '{product_name}' added.")

def update_product_details(product_name, quantity=None, price=None):
    """Update details for a product."""
    if product_name in product_details:
        if quantity is not None:
            product_details[product_name]['quantity'] = quantity
        if price is not None:
            product_details[product_name]['price'] = price
        print(f"Details for product '{product_name}' updated.")
    else:
        print(f"Product '{product_name}' not found.")

def delete_product(product_name):
    """Delete a product from the dictionary."""
    if product_name in product_details:
        del product_details[product_name]
        print(f"Product '{product_name}' deleted.")
    else:
        print(f"Product '{product_name}' not found.")

if __name__ == "__main__":
    # List operations
    add_product('Laptop')
    add_product('Smartphone')
    remove_product('Smartphone')
    update_product('Laptop', 'Gaming Laptop')

    add_product_details('Gaming Laptop', 10, 1500)
    add_product_details('Tablet', 5, 500)
    update_product_details('Gaming Laptop', price=1400)
    delete_product('Tablet')

    print("Product List:", product_list)
    print("Product Details:", product_details)
