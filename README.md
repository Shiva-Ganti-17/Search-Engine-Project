Project Title: Enhancing Search Engine Relevance for Video Subtitles
Background:
In today's rapidly evolving digital landscape, efficient search engines are essential for connecting users with relevant information. This project focuses on enhancing the search relevance for video subtitles, aiming to improve the accessibility of video content. By leveraging natural language processing and machine learning techniques, the goal is to provide a seamless and accurate search experience for users.

Objective:
The main objective of this project is to develop an advanced search engine algorithm that efficiently retrieves subtitles based on user queries, with a specific emphasis on the content of the subtitles. By moving beyond simple keyword matching, the aim is to understand the deeper meaning and context of user queries and documents, thereby enhancing the relevance and accuracy of search results.

Core Logic:
The core logic of the search engine algorithm involves several key steps:

Data Preprocessing:
Read and decode the subtitle data from the provided database.
Apply appropriate cleaning steps to the subtitle documents, such as removing timestamps.
Experiment with text vectorization techniques, including Bag-of-Words (BOW), TF-IDF, and BERT-based SentenceTransformers, to generate representations of subtitle documents.
Document Chunking:
Divide large subtitle documents into smaller, manageable chunks to prevent information loss.
Address the challenge of embedding large documents by splitting them into smaller chunks.
Implement overlapping windows to ensure continuity and context preservation between chunks.
Store the generated embeddings in a ChromaDB database for efficient retrieval.
Retrieving Documents:
Take the user's search query and preprocess it if necessary.
Create an embedding for the user query.
Calculate the cosine similarity between the embeddings of documents and the user query embedding.
Use the cosine similarity scores to return the most relevant candidate documents as per the user’s search query.
Step-by-Step Process:
Part 1: Ingesting Documents
Read and decode the subtitle data from the provided database, considering resource limitations.
Apply cleaning steps to preprocess subtitle documents.
Experiment with text vectorization techniques to generate representations of subtitle documents.
Implement document chunking to handle large documents effectively.
Store the generated embeddings in a ChromaDB database for future retrieval.
Part 2: Retrieving Documents
Take the user's search query and preprocess it if necessary.
Create an embedding for the user query.
Calculate the cosine similarity between document embeddings and the user query embedding.
Return the most relevant candidate documents based on cosine similarity scores.
