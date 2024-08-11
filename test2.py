import streamlit as st
import pandas as pd
import datetime

# Sample Data
products = {
    "Product 1": {"quantity": 100, "expiry_date": "2024-12-31"},
    "Product 2": {"quantity": 50, "expiry_date": "2024-08-15"},
    "Product 3": {"quantity": 200, "expiry_date": "2025-01-10"},
}

orders = []

# Function to check expiry
def check_expiry(date_str):
    today = datetime.date.today()
    expiry_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    return expiry_date < today

# Sign In Page
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Sign In")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password":  # Dummy credentials
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials")

if st.session_state.logged_in:
    # Main Menu
    st.title("Logistics App")

    # Product Name
    st.header("Products")
    product_name = st.selectbox("Select a Product", list(products.keys()))

    if product_name:
        st.write(f"Quantity in Warehouse: {products[product_name]['quantity']}")

        # Track My Order
        st.subheader("Track My Order")
        order_date = st.date_input("Date of Order")
        shipping_location = st.text_input("Shipping Location")
        shipping_date = st.date_input("Shipping Date")

        if st.button("Track Order"):
            st.write(f"Order Date: {order_date}")
            st.write(f"Shipping Location: {shipping_location}")
            st.write(f"Shipping Date: {shipping_date}")
            st.success("Order tracked successfully!")

        # Check Expiry
        st.subheader("Check Expiry")
        expiry_status = check_expiry(products[product_name]['expiry_date'])
        if expiry_status:
            st.warning("The product has expired!")
            if st.button("Cancel Order"):
                st.success("Order cancelled successfully!")
        else:
            st.write(f"Expiry Date: {products[product_name]['expiry_date']}")

        # Browse Items and Order
        st.subheader("Browse Items and Order")
        order_quantity = st.number_input("Select Quantity", min_value=1, max_value=products[product_name]['quantity'])

        if st.button("Place Order"):
            if order_quantity <= products[product_name]['quantity']:
                products[product_name]['quantity'] -= order_quantity
                orders.append({"product": product_name, "quantity": order_quantity, "date": datetime.date.today()})
                st.success(f"Order placed successfully for {order_quantity} units of {product_name}!")
            else:
                st.error("Insufficient quantity in warehouse")

    # Show All Orders
    st.subheader("All Orders")
    if orders:
        orders_df = pd.DataFrame(orders)
        st.dataframe(orders_df)
    else:
        st.write("No orders placed yet.")

