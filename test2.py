import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# In-memory storage for users and orders (simulating a database)
if 'users' not in st.session_state:
    st.session_state['users'] = {}

if 'orders' not in st.session_state:
    st.session_state['orders'] = []

# Helper function to hash passwords (simplified)
def hash_password(password):
    return password[::-1]

# Sign up page
def sign_up():
    st.title("Sign Up")
    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')
    
    if st.button("Sign Up"):
        if username in st.session_state['users']:
            st.error("Username already exists. Please choose another one.")
        elif password != confirm_password:
            st.error("Passwords do not match.")
        else:
            st.session_state['users'][username] = hash_password(password)
            st.success("Sign-up successful! You can now log in.")
            st.session_state['signed_up'] = True

# Login page
def login():
    st.title("Log In")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Log In"):
        if username in st.session_state['users'] and st.session_state['users'][username] == hash_password(password):
            st.success("Logged in successfully!")
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
        else:
            st.error("Invalid username or password")

# Main menu page
def main_menu():
    st.sidebar.title(f"Welcome, {st.session_state['username']}")
    menu = ["Place Order", "Track Order", "Inventory", "Log Out"]
    choice = st.sidebar.selectbox("Select an Option", menu)

    if choice == "Place Order":
        place_order()
    elif choice == "Track Order":
        track_order()
    elif choice == "Inventory":
        inventory()
    elif choice == "Log Out":
        st.session_state['logged_in'] = False
        st.sidebar.empty()

# Place order page
def place_order():
    st.title("Place Order")
    product_name = st.selectbox("Select Product", ["Product A", "Product B", "Product C"])
    quantity = st.number_input("Enter Quantity", min_value=1)
    
    if st.button("Place Order"):
        order = {
            'username': st.session_state['username'],
            'product': product_name,
            'quantity': quantity,
            'order_date': datetime.now(),
            'shipping_date': datetime.now() + timedelta(days=5),
            'status': 'Processing'
        }
        st.session_state['orders'].append(order)
        st.success("Order placed successfully!")

# Track order page
def track_order():
    st.title("Track My Order")
    if len(st.session_state['orders']) == 0:
        st.write("No orders to track.")
        return
    
    for order in st.session_state['orders']:
        if order['username'] == st.session_state['username']:
            st.write(f"Order for {order['product']} ({order['quantity']} units)")
            st.write(f"Order Date: {order['order_date'].strftime('%Y-%m-%d')}")
            st.write(f"Shipping Date: {order['shipping_date'].strftime('%Y-%m-%d')}")
            st.write(f"Status: {order['status']}")
            if datetime.now() > order['shipping_date']:
                order['status'] = 'Shipped'
            st.progress((datetime.now() - order['order_date']).days / 5 * 100)

# Inventory page
def inventory():
    st.title("Inventory")
    inventory_data = {
        "Product A": {"Quantity": 50, "Location": "Warehouse 1"},
        "Product B": {"Quantity": 30, "Location": "Warehouse 2"},
        "Product C": {"Quantity": 20, "Location": "Warehouse 3"},
    }
    
    df = pd.DataFrame.from_dict(inventory_data, orient='index')
    st.table(df)

# Main function
def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if 'signed_up' not in st.session_state:
        st.session_state['signed_up'] = False

    if not st.session_state['logged_in']:
        if not st.session_state['signed_up']:
            sign_up()
        else:
            login()
    else:
        main_menu()

if __name__ == "__main__":
    main()
