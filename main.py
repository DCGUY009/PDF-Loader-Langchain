import os 
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

file_path = (
    "./Protegrity 9.1.0.5.8 Documentation/Master Index Document 9.1.0.5.pdf"
)

file_path2 = (
    "./Protegrity 9.1.0.5.8 Documentation/Other Guides/Installation Guide 9.1.0.5.pdf"
)

# Simple and Fast test Extraction
"""
If you are looking for a simple string representation of text that is embedded in a PDF, the method below is appropriate. 
It will return a list of Document objects-- one per page-- containing a single string of the page's text in the Document's 
page_content attribute. It will not parse text in images or scanned PDF pages. Under the hood it uses the pypdf Python library.
"""

from langchain_community.document_loaders import PyPDFLoader
import asyncio

loader = PyPDFLoader(file_path=file_path)  # Installation Guide is of 680 pages and this was able to extract the 
# text with atmost accuracy in very few seconds and the Master Index Document has 24 pages with tables, it was able to extract the 
# content in the tables as well

async def load_pages():
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)
    
    return pages

pages = asyncio.run(load_pages())

# for page in pages:
#     with open("./master_index_document.md", mode="a") as file:
#         file.write("------------------------------------------------")
#         file.write("------------------------------------------------\n")
#         file.write(f"{page}\n")
#         file.write("------------------------------------------------")
#         file.write("------------------------------------------------\n")

# So, the catch here is this parser is able to extract the text alright even from the tables but the problem is it is not formatted in 
# a way which can be understood only by looking at the text.

# pprint(f"Metadata: {pages[3].metadata}\n")
# pprint(f"Content: {pages[3].page_content}")


# Testing this with a vector store
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings

vector_store = InMemoryVectorStore.from_documents(pages, OpenAIEmbeddings(
    api_key=OPENAI_API_KEY
))
docs = vector_store.similarity_search("Protection Methods?", k=5)

for doc in docs:
    pprint(f"Page {doc.metadata["page"]}: {doc.page_content[:300]}\n")



