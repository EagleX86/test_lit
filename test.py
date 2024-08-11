import streamlit as st

# Simple user authentication (for demonstration purposes)
def authenticate(username, password):
    if username == "admin" and password == "password":
        return True
    else:
        return False

# Placeholder data for demonstration
products = {
    "Product A": {
        "quantity": 150,
        "expiry_date": "2025-12-31",
    },
    "Product B": {
        "quantity": 75,
        "expiry_date": "2024-06-30",
    }
}

# Sign In Page
def sign_in():
    st.title("Sign In")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password")

# Main Menu
def main_menu():
    st.title("Main Menu")
    product_name = st.selectbox("Select a product", list(products.keys()))

    option = st.selectbox("Select an action", ["Track My Order", "Check Quantity", "Order Product", "Check Expiry", "Cancel Order"])

    if option == "Track My Order":
        st.write(f"Tracking {product_name}... (This is a placeholder)")
    
    elif option == "Check Quantity":
        quantity = products[product_name]["quantity"]
        st.write(f"The quantity of {product_name} in the warehouse is {quantity} units.")
    
    elif option == "Order Product":
        order_quantity = st.number_input("Enter quantity to order", min_value=1, max_value=100)
        if st.button("Order Now"):
            st.success(f"Ordered {order_quantity} units of {product_name} successfully!")
    
    elif option == "Check Expiry":
        expiry_date = products[product_name]["expiry_date"]
        st.write(f"The expiry date of {product_name} is {expiry_date}.")
    
    elif option == "Cancel Order":
        if st.button("Cancel Order"):
            st.warning(f"The order for {product_name} has been cancelled!")

# Main Application Logic
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    sign_in()
else:
    main_menu()

# Logout Button
if st.session_state.logged_in:
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()
