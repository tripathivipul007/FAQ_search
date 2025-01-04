
# Albeena FAQ Bot

Albeena FAQ Bot is an AI-powered chatbot designed to respond instantly to frequently asked questions (FAQs). It leverages embeddings and FAISS for semantic search, creating a responsive and user-friendly interface.

## Features

- Provides accurate answers to FAQs based on semantic similarity.
- A chat-like interface with a modern design.
- Input handling via "Ask" button


## Technologies Used

- **Streamlit**: For creating the web-based application.
- **Sentence Embedding Model**: To convert user queries and FAQs into numerical embeddings for semantic similarity.
- **FAISS**: For efficient similarity search across large FAQ datasets.
- **Python**: The core programming language.
- **HTML & CSS**: Custom styling for a better user experience.



## How It Works

- **Input Query**: Users enter their question into the chat interface.

- **Embedding Generation**: The query is transformed into a dense vector using a pre-trained model.

- **Semantic Search**: FAISS retrieves the most relevant FAQ based on similarity to the query embedding.

- **Response Generation**: The bot provides a pre-stored answer from the FAQs or a fallback message for unmatched queries.

## Screenshots

![image](https://github.com/user-attachments/assets/231c0aa2-4c7f-49bf-afa1-70faa1eed5d4)

  **Chat Interface**


![image](https://github.com/user-attachments/assets/11681cd1-844d-4f4f-bb6b-95f7beca9052)



