import streamlit as st
from verify_pass import verify

st.set_page_config(page_title="Bus Pass Verification", page_icon="🚌")

st.title("🚌 QR Code–Based Bus Pass Verification System")

pass_id = st.text_input("Enter Pass ID")

if st.button("Verify Pass"):
    if pass_id:
        result = verify(pass_id)
        if "VALID" in result:
            st.success(result)
        else:
            st.error(result)
    else:
        st.warning("Please enter Pass ID")


