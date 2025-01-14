from sentence_transformers import SentenceTransformer
import faiss
import numpy as np



faqs = [
    {"question": "What is your return policy?", "answer": "You can return items within 30 days."},
    {"question": "How do I reset my password?", "answer": "Click on 'Forgot Password' on the login page."},
    {"question": "What payment methods do you accept?", "answer": "We accept credit cards, debit cards, upis, and more."},
    {"question": "How do I track my order?", "answer": "You can track your order using the tracking link sent to your email."},
    {"question": "Can I cancel my order?", "answer": "Yes, you can cancel your order within 24 hours of placing it."},
    {"question": "Do you offer international shipping?", "answer": "Yes, we ship to selective countries. Please check the shipping options at checkout."},
    {"question": "How long does shipping take?", "answer": "Shipping usually takes 5–7 business days within the country and 10–15 business days for international orders."},
    {"question": "What is your warranty policy?", "answer": "We offer a 1-year warranty on all products. Please contact support for warranty claims."},
    {"question": "How do I contact customer support?", "answer": "You can contact customer support via email, live chat, or phone."},
    {"question": "Can I change the shipping address after placing an order?", "answer": "Yes, you can update your shipping address within 12 hours of placing your order."},
    {"question": "What should I do if I receive a damaged product?", "answer": "Contact our support team immediately with photos of the damaged item to initiate a replacement or refund."},
    {"question": "Do you offer gift wrapping services?", "answer": "Yes, we provide gift wrapping at an additional cost during checkout."},
    {"question": "How can I leave a review for a product?", "answer": "After purchase, you'll receive an email with a link to leave a review on our website."},
    {"question": "What happens if my order gets lost during shipping?", "answer": "If your order is lost, contact us, and we'll assist you with a replacement or refund."},
    {"question": "Do you offer discounts for bulk purchases?", "answer": "Yes, bulk discounts are available. Contact our sales team for details."},
    {"question": "You are a great chatbot", "answer": "Thanks! my developers have worked very hard for it..."}

]



# Load a pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Extract FAQ questions
questions = [faq["question"] for faq in faqs]

# Generate embeddings for the FAQ questions
question_embeddings = model.encode(questions)


#Get the embedding dimension
dimension = question_embeddings.shape[1]

# Create a FAISS index (L2 for Euclidean distance)
index = faiss.IndexFlatL2(dimension)

# Add embeddings to the FAISS index
index.add(np.array(question_embeddings))



def find_best_match(query):
    # Encode the query to get its embedding
    query_embedding = model.encode([query])
    
    # Search the FAISS index
    distances, indices = index.search(query_embedding, k=1)
    
    # Get the best match
    best_match_index = indices[0][0]
    return faqs[best_match_index]
