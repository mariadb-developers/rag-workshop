import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_mariadb import MariaDBStore

GEMINI_KEY = os.environ["GEMINI_API_KEY"]

# Use Google Generative AI for embeddings
embedder = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", # Model name for embeddings (use the same embedding model as in ingest_embeddings.py)
    google_api_key=GEMINI_KEY # Ensure you set this environment variable
)

# Create a vector store for embeddings
vectorStore = MariaDBStore(
    datasource="mariadb+mariadbconnector://root:RootPassword123!@mariadb-server:3306/demo",
    embeddings=embedder,
    embedding_length=768,
    collection_name="products_desc_gemini001"
)

# Perform a similarity search
results = vectorStore.similarity_search("YOUR QUERY HERE", k=10) # TODO: replace with a real query

# Print the results
for i, (doc) in enumerate(results, 1):
    print(f"{i}. {doc.metadata['name']} - {doc.page_content}")
