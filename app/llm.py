import os
import openai
import sys

from llama_index.core import (
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)
from llama_index.readers.web import TrafilaturaWebReader

from dotenv import load_dotenv, find_dotenv

sys.path.append('../..')
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']
source_url = os.environ['SOURCE_URL']

# check if storage already exists
PERSIST_DIR = "./data"
if not os.path.exists(PERSIST_DIR):
    loader = TrafilaturaWebReader()
    documents = loader.load_data(urls=[source_url])
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

# Either way we can now query the index
query_engine = index.as_query_engine()

def query(question):
    response = query_engine.query(question)
    return response

    


