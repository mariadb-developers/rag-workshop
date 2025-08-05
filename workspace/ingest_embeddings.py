import os
import mariadb
from sqlalchemy.engine.url import make_url
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_mariadb import MariaDBStore

# Create embeddings using Google Generative AI
embedder = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", # Model name for embeddings
    google_api_key=os.environ["GEMINI_API_KEY"] # Ensure you set this environment variable
)

# MariaDB Data Source Name (host: mariadb-server, port: 3306, database: demo, user: root, password: RootPassword123!)
DSN = "mariadb+mariadbconnector://root:RootPassword123!@mariadb-server:3306/demo"

# Create a MariaDB store for embeddings (LangChain integration)
store = MariaDBStore(
    embeddings=embedder,
    embedding_length=768,
    datasource=DSN,
    collection_name="products_desc_gemini001"
)

# Connect to MariaDB
url = make_url(DSN)
conn = mariadb.connect(
    user=url.username,
    password=url.password,
    host=url.host,
    port=url.port,
    database=url.database,
)

# Get all products
cur = conn.cursor()
cur.execute("SELECT id, name, description FROM products")

# Ingest product descriptions into the embeddings store
for id, name, desc in cur:
    doc = Document(page_content=desc, metadata={"id": id, "name" : name})
    store.add_documents([doc])
    print(f"[ingested] id={id}", flush=True)

conn.close()
