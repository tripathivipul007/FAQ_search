from sentence_transformers import SentenceTransformer
import faiss
import numpy as np



faqs = [
    {"question": "What is your return policy?", "answer": "You can return items within 30 days."},
    {"question": "How do I reset my password?", "answer": "Click on 'Forgot Password' on the login page."},
    {"question": "What payment methods do you accept?", "answer": "We accept credit cards, PayPal, and more."},
    {"question": "How do I track my order?", "answer": "You can track your order using the tracking link sent to your email."},
    {"question": "Can I cancel my order?", "answer": "Yes, you can cancel your order within 24 hours of placing it."}
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
