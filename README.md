# Workshop: Vector Search with LangChain and MariaDB

Learn how to use [MariaDB](https://mariadb.com/) as a vector store ([vector database](https://mariadb.com/database-topics/vector-embedded-search/)) for embeddings using Gemini, Python, and [LangChain](https://github.com/mariadb-corporation/langchain-mariadb).

---
**➡️ Step 1** - Download **Docker version 28** or later and run the following in a terminal window:

```shell
docker --version
```

---
**➡️ Step 2** - Download (click on **Code** -> **Download ZIP**) and extract the project at:

https://github.com/mariadb-developers/vector-search-workshop

**Note:** Alternatively, you can clone the project using Git.

---
**➡️ Step 3** - In a terminal window, move to the project directory, and start the services with:

```shell
docker compose up -d
```

---
**➡️ Step 4** - Watch the logs with:

```shell
docker logs code-server -f
```

---
**➡️ Step 5** - Go to http://localhost:4444/ and create a MariaDB connection (click on _Database icon_ -> **Create Connection** -> **MariaDB**):

* Host: `mariadb-server`
* Port: `3306`
* User: `root`
* Password: `RootPassword123!`

---
**➡️ Step 6** - Click on the **Open Query** button next to **demo** and run this SQL query (replace the search query first!):

```sql
SELECT CONCAT(ROW_NUMBER() OVER(), ". ", name, " - ", description)
FROM products
WHERE MATCH(description) AGAINST ("YOUR_QUERY_HERE")
LIMIT 10;
```

---
**➡️ Step 7** - Click on **Toggle Panel** -> **TERMINAL** and calculate the vectors by running the following commands (replace the API key first!):

```shell
export GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
python ingest_embeddings.py
```

---
**➡️ Step 8** - Find products using vector search by introducing your own search query in the **semantic_search.py** program (use the same search query as before!):

```python
results = vectorStore.similarity_search("YOUR_QUERY_HERE", k=10)
```

... and running:

```shell
python semantic_search.py
```

---
**➡️ Step 9** - Compare results using an LLM (replace the search query and result sets first!):

```
Which result set is better for the search YOUR_QUERY_HERE" and why? (answer in a very short paragraph)

Result set 1:
INSERT_RESULT_SET_1

Result set 2:
INSERT_RESULT_SET_2
```

---
**➡️ (Optional) Step 10** - Stop and delete services and volumes (this deletes all the data!):

```shell
docker compose down -v
```
