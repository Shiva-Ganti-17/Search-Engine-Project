import streamlit as st
import sqlite3
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load SentenceTransformer model
model_name = 'all-MiniLM-L6-v2'
model = SentenceTransformer(model_name, device='cpu')

# Function to encode the preprocessed query using the model
def encode_query(query):
    query_embedding = model.encode(query)
    return query_embedding

# Function to fetch all document content from the 'embedding_fulltext_search_content' table
def fetch_document_data():
    conn = sqlite3.connect('C:/Users/shiva/OneDrive/Desktop/search engine/webapp/chromadb/chroma.sqlite3')
    c = conn.cursor()
    c.execute("SELECT * FROM embedding_fulltext_search_content")
    document_data = c.fetchall()
    conn.close()
    return document_data

# Function to calculate cosine similarity between query and document embeddings
def calculate_similarity(query_embedding, document_embedding):
    similarity = cosine_similarity([query_embedding], [document_embedding])[0][0]
    return similarity

# Main function to display search results
def main():
    st.title("Search Engine")
    
    # Streamlit UI for document search
    search_query = st.text_input('Enter your search query:')
    if st.button('Search'):
        # Encode the query
        query_embedding = encode_query(search_query)
        
        # Fetch all document data from the 'embedding_fulltext_search_content' table
        document_data = fetch_document_data()
        
        # Calculate similarity between query and each document
        similarities = []
        for doc_data in document_data:
            document_embedding = model.encode(doc_data[1])  # Assuming content is in the second column
            similarity = calculate_similarity(query_embedding, document_embedding)
            similarities.append((doc_data[1], similarity))  # Store content and similarity
        
        # Sort documents based on similarity scores
        sorted_documents = sorted(similarities, key=lambda x: x[1], reverse=True)
        
        # Display top 10 search results with subtitles
        st.subheader('Top 10 Related Subtitles:')
        for i, (content, _) in enumerate(sorted_documents[:10], 1):  # Display only the top 10 documents
            st.write(f"Subtitle {i}: \"{content}\"")

if __name__ == "__main__":
    main()
