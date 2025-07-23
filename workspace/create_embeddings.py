import os
import mariadb
from sqlalchemy.engine.url import make_url
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_mariadb import MariaDBStore

embedder = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.environ["GEMINI_API_KEY"]
)

DSN = "mariadb+mariadbconnector://root:RootPassword123!@mariadb-server:3306/rag_demo"

store = MariaDBStore(
    embeddings=embedder,
    embedding_length=768,
    datasource=DSN,
    collection_name="products_desc_gemini001"
)

url = make_url(DSN)
conn = mariadb.connect(
    user=url.username,
    password=url.password,
    host=url.host,
    port=url.port,
    database=url.database,
)
cur = conn.cursor()
cur.execute("SELECT id, description FROM products")

for pid, desc in cur:
    doc = Document(page_content=desc, metadata={"product_id": pid})
    store.add_documents([doc])
    print(f"[ingested] product_id={pid}", flush=True)

conn.close()
