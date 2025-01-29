import streamlit as st

# Set page configuration (this should be the first Streamlit command)
st.set_page_config(
    page_title="Secure App",
    page_icon="🔒",
    layout="centered"
)

# Security Note: This example uses a hardcoded password for demonstration purposes only.
# In production, use proper password hashing and secure storage solutions.
VALID_PASSWORD = "admin123"  # Change this to your desired password

def check_password():
    """Returns `True` if the user entered the correct password."""
    
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == VALID_PASSWORD:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password
        else:
            st.session_state["password_correct"] = False

    # Show password input if password hasn't been checked yet
    if "password_correct" not in st.session_state:
        st.text_input(
            "Password", 
            type="password", 
            on_change=password_entered, 
            key="password"
        )
        return False
    # Return True if password is correct, otherwise show error + input again
    elif not st.session_state["password_correct"]:
        st.error("Incorrect password. Please try again.")
        st.text_input(
            "Password", 
            type="password", 
            on_change=password_entered, 
            key="password"
        )
        return False
    else:
        # Password correct
        return True

def dashboard():
    """Main dashboard page after successful login"""
    st.title("Secure Dashboard 🔒")
    
    # Example dashboard content
    st.success("Welcome to your secure dashboard!")
    st.write("Here's your confidential data:")
    
    # Sample data visualization
    chart_data = {
        "Category": ["A", "B", "C", "D", "E"],
        "Values": [23, 45, 56, 78, 33]
    }
    st.bar_chart(chart_data, x="Category", y="Values")
    
    # Display some metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Users", "1,234", "+15")
    col2.metric("Revenue", "$23,456", "-3%")
    col3.metric("Active Sessions", "56", "+8")
    
    # Logout button
    st.sidebar.button("Logout", on_click=logout)

def logout():
    """Clear the session state and log out the user"""
    for key in list(st.session_state.keys()):
        del st.session_state[key]

def main():
    """Main app control flow"""
    # Check authentication
    if not check_password():
        return
    
    # If authenticated, show dashboard
    dashboard()

if __name__ == "__main__":
    main()