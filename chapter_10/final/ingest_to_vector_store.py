import toml
from vector_store import VectorStore

secrets = toml.load(".streamlit/secrets.toml")
api_keys = secrets["api_keys"]
index_name = secrets["config"]["VECTOR_STORE_INDEX_NAME"]
model_name = secrets["config"]["EMBEDDING_MODEL_NAME"]
vector_store = VectorStore(api_keys, index_name, model_name)
vector_store.ingest_folder("articles/")
