import streamlit as st

def main():
    st.title("Simple Calculator")

    # Input fields for numbers
    num1 = st.number_input("Enter the first number", value=0.0)
    num2 = st.number_input("Enter the second number", value=0.0)

    # Dropdown for operation selection
    operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

    # Perform calculation based on selected operation
    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"

        st.write(f"The result of {operation.lower()}ing {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()
