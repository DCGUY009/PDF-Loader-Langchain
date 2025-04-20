# Parsing Locally requires the installation of additional dependencies (the following steps are also written in Setup.md file):
# Poppler -  Installation for windows is download the latest version from here: https://github.com/oschwartz10612/poppler-windows
# and Extract the file someplace, go and find bin inside the extracted files and then go to edit system environment variables from
# search and in System Variables find path and edit it, and add a new one and enter the bin path of the poppler library you just 
# downloaded. If done open the cmd and check if it is installed correctly by entering the command `pdftotext -v` and if the version
# is returned it is downloaded correctly and added to the path
# Tesseract - Installation for windows is through a .exe file downloadable from: 
# https://github.com/UB-Mannheim/tesseract/wiki#tesseract-installer-for-windows. Once the .exe file is downloaded follow the installation
# menu and install the tesseract OCR library 

#% %
import os 
from dotenv import load_dotenv
from pprint import pprint
from langchain_unstructured import UnstructuredLoader
import asyncio
from page_render import render_page

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

file_path = (
    "../Protegrity 9.1.0.5.8 Documentation/Master Index Document 9.1.0.5.pdf"
)

file_path2 = (
    "../Protegrity 9.1.0.5.8 Documentation/Other Guides/Installation Guide 9.1.0.5.pdf"
)


loader_local = UnstructuredLoader(
    file_path=file_path,
    strategy="hi_res",
)

# async def docs_loader():
docs_local = []

for doc in loader_local.lazy_load():
    docs_local.append(doc)

with open("Splits/Docs List/hi_res_docslist_master_index_document.md", mode="a") as file:
    file.write(f"{docs_local}")

    # return docs_local

for doc in docs_local:
    with open("Splits/Split/hi_res_master_index_document.md", mode="a") as file:
        file.write("------------------------------------------------")
        file.write("------------------------------------------------\n")
        file.write(f"{doc}\n")
        file.write("------------------------------------------------")
        file.write("------------------------------------------------\n")


thirteenth_page_docs = [doc for doc in docs_local if doc.metadata.get("page_number") == 13]

for doc in thirteenth_page_docs:
    print(doc.page_content)

#% %
render_page(doc_list=docs_local, file_path=file_path, page_number=8)


