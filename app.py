import os
import re
import subprocess
import streamlit as st

st.set_page_config(
    page_title="Swastik's Dashboard", 
    page_icon="⚡", 
    layout="centered"
)

st.title("⚡ Welcome to the Workspace")
st.subheader("Developer Profile: **Swastik**")
st.write("This application serves as an interactive Python engineering playground.")
st.divider()

# Tool 1: Resistor Calculator
st.header("🎛️ 4-Band Resistor Value Decoder")
color_multipliers = {
    "Black": 1,
    "Brown": 10,
    "Red": 100,
    "Orange": 1000,
    "Yellow": 10000,
    "Green": 100000,
    "Blue": 1000000,
}
digit_colors = ["Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue"]

col1, col2, col3 = st.columns(3)
with col1:
    b1 = st.selectbox("Band 1 (Digit)", digit_colors, index=2)
with col2:
    b2 = st.selectbox("Band 2 (Digit)", digit_colors, index=0)
with col3:
    b3 = st.selectbox("Band 3 (Multiplier)", list(color_multipliers.keys()), index=2)

digit_1 = digit_colors.index(b1)
digit_2 = digit_colors.index(b2)
multiplier = color_multipliers[b3]

final_ohms = ((digit_1 * 10) + digit_2) * multiplier
k_ohms = final_ohms / 1000

st.metric(
    label="Calculated Resistance Value",
    value=f"{k_ohms:.2f} kΩ" if k_ohms >= 1 else f"{final_ohms} Ω",
)

st.divider()

# Tool 2: Live Network Engine Check
st.header("🌐 Quick Infrastructure Ping Utility")
target_host = st.text_input("Enter target domain or IP address:", "8.8.8.8")

if st.button("Execute Network Ping"):
    if not re.match(r"^[a-zA-Z0-9.-]+$", target_host):
        st.error("Invalid characters detected in host format.")
    else:
        st.info(f"Pinging {target_host} directly from host environment...")
        param = "-n" if os.name == "nt" else "-c"
        command = ["ping", param, "2", target_host]
        try:
            output = subprocess.run(command, capture_output=True, text=True, timeout=5)
            if output.returncode == 0:
                st.success("Target Host is reachable!")
                st.code(output.stdout, language="text")
            else:
                st.error("Ping request timed out or host is down.")
                st.code(output.stderr, language="text")
        except Exception as e:
            st.error(f"Execution system fault: {e}")
