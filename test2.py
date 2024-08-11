import streamlit as st
from datetime import datetime

# Mock data for products, orders, and warehouse inventory
products = {
    "Product A": {"quantity": 50, "expiry": "2024-09-10"},
    "Product B": {"quantity": 30, "expiry": "2024-11-15"},
    "Product C": {"quantity": 20, "expiry": "2024-08-25"},
}

orders = [
    {"product": "Product A", "date": "2024-08-01", "shipping_date": "2024-08-05", "location": "Warehouse 1", "quantity": 10, "status": "Shipped"},
    {"product": "Product B", "date": "2024-07-20", "shipping_date": "2024-07-25", "location": "Warehouse 2", "quantity": 5, "status": "Delivered"},
]

# Sign-In / Sign-Up
def sign_in_page():
    st.title("Logistics App - Sign In")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.session_state['logged_in'] = True
        st.session_state['user'] = email
        st.success(f"Logged in as {email}")
        st.experimental_rerun()

# Main Menu
def main_menu():
    st.title("Main Menu")
    option = st.selectbox("Choose an action", ["Track My Order", "Browse Items", "Place Order", "Check Expiry", "Cancel Order"])

    if option == "Track My Order":
        track_order_page()
    elif option == "Browse Items":
        browse_items_page()
    elif option == "Place Order":
        place_order_page()
    elif option == "Check Expiry":
        check_expiry_page()
    elif option == "Cancel Order":
        cancel_order_page()

# Track My Order Page
def track_order_page():
    st.title("Track My Order")
    order_id = st.selectbox("Select Order", range(len(orders)))
    order = orders[order_id]
    st.write(f"**Product:** {order['product']}")
    st.write(f"**Order Date:** {order['date']}")
    st.write(f"**Shipping Location:** {order['location']}")
    st.write(f"**Shipping Date:** {order['shipping_date']}")
    st.write(f"**Quantity:** {order['quantity']}")
    st.write(f"**Status:** {order['status']}")

# Browse Items Page
def browse_items_page():
    st.title("Browse Items in Warehouse")
    product = st.selectbox("Select Product", list(products.keys()))
    st.write(f"**Product:** {product}")
    st.write(f"**Quantity Available:** {products[product]['quantity']}")
    if st.button("Order This Item"):
        place_order_page(product)

# Place Order Page
def place_order_page(selected_product=None):
    st.title("Place an Order")
    product = st.selectbox("Select Product", list(products.keys()), index=list(products.keys()).index(selected_product) if selected_product else 0)
    quantity = st.number_input("Select Quantity", min_value=1, max_value=products[product]['quantity'])
    if st.button("Place Order"):
        orders.append({"product": product, "date": str(datetime.today().date()), "shipping_date": "2024-08-20", "location": "Warehouse 1", "quantity": quantity, "status": "Processing"})
        products[product]['quantity'] -= quantity
        st.success(f"Order placed for {quantity} of {product}")

# Check Expiry Page
def check_expiry_page():
    st.title("Check Product Expiry")
    product = st.selectbox("Select Product", list(products.keys()))
    expiry_date = datetime.strptime(products[product]['expiry'], "%Y-%m-%d").date()
    st.write(f"**Product:** {product}")
    st.write(f"**Expiry Date:** {expiry_date}")
    if expiry_date < datetime.today().date():
        st.warning("This product has expired!")
        if st.button("Cancel Expired Orders"):
            orders[:] = [order for order in orders if order['product'] != product]
            st.success(f"Cancelled all orders for {product}")

# Cancel Order Page
def cancel_order_page():
    st.title("Cancel an Order")
    order_id = st.selectbox("Select Order to Cancel", range(len(orders)))
    order = orders[order_id]
    st.write(f"**Product:** {order['product']}")
    st.write(f"**Order Date:** {order['date']}")
    st.write(f"**Shipping Location:** {order['location']}")
    st.write(f"**Shipping Date:** {order['shipping_date']}")
    st.write(f"**Quantity:** {order['quantity']}")
    if st.button("Cancel Order"):
        orders.pop(order_id)
        st.success("Order cancelled")

# Main App
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    sign_in_page()
else:
    main_menu()
