import os
import mariadb
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_mariadb import MariaDBStore

# Create embeddings using Google Generative AI
embedder = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", # Model name for embeddings
    google_api_key=os.environ["GEMINI_API_KEY"] # Ensure you set this environment variable
)

# MariaDB connection details
USER="root"
PASSWORD="RootPassword123!"
HOST="mariadb-server"
PORT=3306
DATABASE="demo"

# Create a MariaDB store for embeddings (LangChain integration)
store = MariaDBStore(
    datasource=f"mariadb+mariadbconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}",
    embeddings=embedder,
    embedding_length=768,
    collection_name="products_desc_gemini001"
)

# Connect to MariaDB
connection = mariadb.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DATABASE)

# Get all products
cursor = connection.cursor()
cursor.execute("SELECT id, name, description FROM products")

# Ingest product descriptions into the embeddings store
for id, name, desc in cursor:
    doc = Document(page_content=desc, metadata={"id": id, "name" : name})
    store.add_documents([doc])
    print(f"[ingested] id={id}", flush=True)

connection.close()
