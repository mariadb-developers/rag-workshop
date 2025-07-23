import os, mariadb, textwrap
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_mariadb import MariaDBStore

GEMINI_KEY = os.environ["GEMINI_API_KEY"]

embedder = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GEMINI_KEY
)

vectorStore = MariaDBStore(
    embeddings=embedder,
    embedding_length=768,
    datasource="mariadb+mariadbconnector://root:RootPassword123!@mariadb-server:3306/rag_demo",
    collection_name="products_desc_gemini001"
)

results = vectorStore.similarity_search("Gear for cold, wet mountain backpacking", k=10)

for i, (doc) in enumerate(results, 1):
    snippet = textwrap.shorten(doc.page_content, width=250, placeholder="…")
    print(f"{i}. {snippet}\n")
