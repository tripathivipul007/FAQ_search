import streamlit as st
from faqs import model
from faqs import faqs
from faqs import index as faiss_index 

# Title of the app
st.title("Frequently Asked Questions")

# Subtitle
st.subheader("We are here to assist you")

# User input
user_query = st.text_input("Ask a question:")

if st.button("Search"):
    if user_query.strip():  # Ensure the input is not empty
        # Generate embedding for user query
        query_embedding = model.encode([user_query])
        
        # Search FAISS index for the closest match
        distances, indices = faiss_index.search(query_embedding, k=1)
        
        # Display result
        if distances[0][0] < 1.0:  # A threshold to determine a good match
            matched_faq = faqs[indices[0][0]]
            st.success(f"**Question:** {matched_faq['question']}")
            st.info(f"**Answer:** {matched_faq['answer']}")
        else:
            st.warning("Sorry, no matching FAQ was found.")
    else:
        st.error("Please enter a question!")