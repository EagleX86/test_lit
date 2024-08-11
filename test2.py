import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Mock product data
products = {
    'Product A': {'quantity': 50, 'shipping_date': datetime.now() + timedelta(days=5), 'expiry_date': datetime.now() + timedelta(days=30)},
    'Product B': {'quantity': 20, 'shipping_date': datetime.now() + timedelta(days=3), 'expiry_date': datetime.now() + timedelta(days=15)},
    'Product C': {'quantity': 100, 'shipping_date': datetime.now() + timedelta(days=7), 'expiry_date': datetime.now() + timedelta(days=45)},
}

# Mock user data
user_data = {'username': 'user', 'password': 'pass'}

# Sign in page
def sign_in():
    st.title("Sign In")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Sign In"):
        if username == user_data['username'] and password == user_data['password']:
            st.success("Signed in successfully!")
            st.session_state['logged_in'] = True
        else:
            st.error("Invalid username or password")

# Product page
def product_page():
    st.title("Products")
    product_name = st.selectbox("Select Product", list(products.keys()))
    st.write(f"Product Name: {product_name}")
    
    if st.button("Track My Order"):
        track_order(product_name)
    
    if st.button("Browse Items"):
        browse_items(product_name)

    if st.button("Check Expiry"):
        check_expiry(product_name)

# Track order page
def track_order(product_name):
    st.title("Track My Order")
    product = products[product_name]
    st.write(f"Order Date: {datetime.now().strftime('%Y-%m-%d')}")
    st.write(f"Shipping Status: {'Shipped' if datetime.now() > product['shipping_date'] else 'Pending'}")
    st.progress((datetime.now() - (product['shipping_date'] - timedelta(days=5))).days / 5 * 100)
    
# Browse items page
def browse_items(product_name):
    st.title("Browse Items")
    product = products[product_name]
    st.write(f"Product Name: {product_name}")
    st.write(f"Quantity in Warehouse: {product['quantity']}")
    
    quantity_to_order = st.number_input("Enter Quantity to Order", min_value=1, max_value=product['quantity'])
    if st.button("Place Order"):
        place_order(product_name, quantity_to_order)

# Place order page
def place_order(product_name, quantity_to_order):
    st.title("Order Placement")
    st.write(f"Order placed for {quantity_to_order} units of {product_name} successfully!")

# Check expiry page
def check_expiry(product_name):
    st.title("Check Expiry")
    product = products[product_name]
    if datetime.now() > product['expiry_date']:
        st.error("Product has expired!")
        if st.button("Cancel Order"):
            st.write("Order cancelled successfully!")
    else:
        st.write(f"Product will expire on {product['expiry_date'].strftime('%Y-%m-%d')}")

# Main function
def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        sign_in()
    else:
        st.sidebar.title("Menu")
        menu = ["Products", "Logout"]
        choice = st.sidebar.selectbox("Choose Option", menu)

        if choice == "Products":
            product_page()
        elif choice == "Logout":
            st.session_state['logged_in'] = False
            st.write("Logged out successfully!")

if __name__ == "__main__":
    main()
