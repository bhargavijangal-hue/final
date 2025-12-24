import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Banking FAQ Chatbot",
    page_icon="🏦",
    layout="centered"
)

# ---------------- CUSTOM CSS (BANKING DARK THEME) ----------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0a192f, #102a43, #1c3d5a);
        font-family: Arial, sans-serif;
        color: #e0e0e0;
    }

    h1 {
        text-align: center;
        color: #64ffda;
    }

    .footer {
        text-align: center;
        font-size: 13px;
        color: #b0bec5;
        margin-top: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- BANKING FAQ DATA ----------------
faq = {
    ("account", "open"): "You can open a bank account by submitting KYC documents such as Aadhaar, PAN, and a photo at a bank branch or online.",
    ("balance", "check"): "You can check your account balance using net banking, mobile banking app, ATM, or SMS service.",
    ("atm", "withdraw"): "ATM withdrawal allows you to withdraw cash using your debit card. Daily limits may apply.",
    ("loan", "personal loan"): "A personal loan is an unsecured loan offered based on your income and credit score.",
    ("interest rate", "interest"): "Interest rates depend on the bank and type of account or loan.",
    ("credit card",): "A credit card allows you to borrow money up to a limit and repay later with possible interest.",
    ("debit card",): "A debit card lets you spend money directly from your bank account.",
    ("net banking", "online banking"): "Net banking allows you to access your account online for transfers, bill payments, and statements.",
    ("upi",): "UPI allows instant money transfers using a mobile number or UPI ID.",
    ("fixed deposit", "fd"): "Fixed Deposits offer higher interest when you deposit money for a fixed period.",
    ("kyc",): "KYC is a verification process required to comply with banking regulations."
}

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- UI ----------------
st.title("🏦 AI Banking FAQ Chatbot")
st.write("Ask common banking-related questions")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- USER INPUT ----------------
user_input = st.chat_input("Ask a banking question...")

if user_input:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    response = None
    user_text = user_input.lower()

    for keywords, answer in faq.items():
        if any(word in user_text for word in keywords):
            response = answer
            break

    if not response:
        response = (
            "Sorry, I can help only with basic banking FAQs.\n\n"
            "Please visit your bank branch or official website for more details."
        )

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.markdown(response)

# ---------------- FOOTER ----------------
st.markdown(
    "<div class='footer'>ℹ️ This chatbot provides general banking information only.</div>",
    unsafe_allow_html=True
)
