import streamlit as st
import emoji

# Title of the app
st.title("Calculator by Abdullah Khalid")

# Display and Clear button row
display_col, clear_col = st.columns([5, 1])
display = display_col.empty()

# Clear input
def clear_input():
    st.session_state.clear_clicks += 1
    if st.session_state.clear_clicks == 1:
        st.session_state.input_value = ""
        display.markdown("<div style='font-size: 40px; color: white;'>0</div>", unsafe_allow_html=True)

# Clear button in right column
if clear_col.button("C"):
    clear_input()

# Initialize session state variables
if "input_value" not in st.session_state:
    st.session_state.input_value = ""
if "operation" not in st.session_state:
    st.session_state.operation = None
if "stored_value" not in st.session_state:
    st.session_state.stored_value = ""
if "clear_clicks" not in st.session_state:
    st.session_state.clear_clicks = 0

# Function to format result (remove .0 if not needed)
def format_result(result):
    return str(int(result)) if result == int(result) else str(result)

# Update display
def update_display(value):
    st.session_state.input_value += value
    display.markdown(f"<div style='font-size: 40px; color: white;'>{st.session_state.input_value}</div>", unsafe_allow_html=True)

# Set operation and show operator on display
def set_operation(op):
    if st.session_state.input_value:
        st.session_state.stored_value = st.session_state.input_value
        st.session_state.input_value = ""
    st.session_state.operation = op
    operator_symbol = {
        "Addition": "+",
        "Subtraction": "-",
        "Multiplication": "×",
        "Division": "÷"
    }.get(op, "?")
    display.markdown(f"<div style='font-size: 40px; color: white;'>{operator_symbol}</div>", unsafe_allow_html=True)

# Calculate and display result
def calculate_result():
    if st.session_state.operation and st.session_state.input_value:
        try:
            num1 = float(st.session_state.stored_value)
            num2 = float(st.session_state.input_value)
            if st.session_state.operation == "Addition":
                result = num1 + num2
            elif st.session_state.operation == "Subtraction":
                result = num1 - num2
            elif st.session_state.operation == "Multiplication":
                result = num1 * num2
            elif st.session_state.operation == "Division":
                result = num1 / num2 if num2 != 0 else "Error"
            result_str = format_result(result) if result != "Error" else result
        except:
            result_str = "Error"
        st.session_state.input_value = result_str
        st.session_state.operation = None
        st.session_state.stored_value = ""
        display.markdown(f"<div style='font-size: 40px; color: white;'>{result_str}</div>", unsafe_allow_html=True)

# Display current input or 0 at start
if st.session_state.input_value:
    display.markdown(f"<div style='font-size: 40px; color: white;'>{st.session_state.input_value}</div>", unsafe_allow_html=True)
else:
    display.markdown("<div style='font-size: 40px; color: white;'>0</div>", unsafe_allow_html=True)

# Styling buttons
button_style = """
<style>
.stButton>button {
    font-size: 30px;
    padding: 10px;
    width: 100%;
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    color: #333;
}
.stButton>button:hover {
    background-color: #ddd;
    border: 1px solid #bbb;
}
</style>
"""
st.markdown(button_style, unsafe_allow_html=True)

# Layout
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7"):
        update_display("7")
    if st.button("4"):
        update_display("4")
    if st.button("1"):
        update_display("1")
    if st.button("0"):
        update_display("0")

with col2:
    if st.button("8"):
        update_display("8")
    if st.button("5"):
        update_display("5")
    if st.button("2"):
        update_display("2")
    if st.button("."):
        update_display(".")

with col3:
    if st.button("9"):
        update_display("9")
    if st.button("6"):
        update_display("6")
    if st.button("3"):
        update_display("3")
    if st.button("="):
        calculate_result()

with col4:
    if st.button(emoji.emojize(":heavy_plus_sign:")):
        set_operation("Addition")
    if st.button(emoji.emojize(":heavy_minus_sign:")):
        set_operation("Subtraction")
    if st.button(emoji.emojize(":heavy_multiplication_x:")):
        set_operation("Multiplication")
    if st.button(emoji.emojize(":heavy_division_sign:")):
        set_operation("Division")
