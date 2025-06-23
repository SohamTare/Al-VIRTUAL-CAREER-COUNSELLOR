import streamlit as st

def main():
    st.set_page_config(page_title="AI Virtual Career Counsellor", page_icon="🎓")
    st.title("🎓 AI Virtual Career Counsellor")

    st.markdown("Tell me what you’re interested in, and I’ll recommend career options.")

    # Input Field
    interests = st.text_input("What are your interests? (e.g., I like coding and finance)")

    if st.button("Suggest Career"):
        if interests:
            st.success(f"You seem to be interested in: {interests}\n\n(We'll recommend careers in the next step!)")
        else:
            st.warning("Please enter at least one interest.")

# 🧠 This line is crucial — it runs your main function
if __name__ == "__main__":
    main()
