# % %
import os 
from dotenv import load_dotenv
from pprint import pprint
from page_render import render_page, plot_pdf_with_boxes

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

file_path = (
    "../Protegrity 9.1.0.5.8 Documentation/Master Index Document 9.1.0.5.pdf"
)

file_path2 = (
    "../Protegrity 9.1.0.5.8 Documentation/Other Guides/Installation Guide 9.1.0.5.pdf"
)

# Analyzing layout and text extraction from images
"""
If you require a more granular segmentation of text (e.g., into distinct paragraphs, titles, tables, or other structures) or 
require extraction of text from images, the method below is appropriate. It will return a list of Document objects, where each 
object represents a structure on the page. The Document's metadata stores the page number and other information related to the 
object (e.g., it might store table rows and columns in the case of a table object).

Here, unstructured: https://platform.unstructured.io/app/start is used with langchain-unstructured under the hood. Here, there are 2 
strategies that can be set `fast` or `hi-res`. hi-res option provides support for document layout analysis and OCR.

"""


UNSTRUCTURED_API_KEY = os.getenv("UNSTRUCTURED_API_KEY")

from langchain_unstructured import UnstructuredLoader

loader = UnstructuredLoader(
    api_key=UNSTRUCTURED_API_KEY,
    file_path=file_path,
    strategy="hi_res",
    partition_via_api=True,
    coordinates=True,
)

def load_docs():
    docs = []
    for doc in loader.lazy_load():
        docs.append(doc)

    # with open("Splits/Docs_List/hi_res_docslist_master_index_document1.md", mode="a") as file:
    #     file.write(f"{docs}")
    
    return docs

docs = load_docs()

# for doc in docs:
#     with open("Splits/Split Text/hi_res_master_index_document1.md", mode="a") as file:
#         file.write("------------------------------------------------")
#         file.write("------------------------------------------------\n")
#         file.write(f"{doc}\n")
#         file.write("------------------------------------------------")
#         file.write("------------------------------------------------\n")


first_page_docs = [doc for doc in docs if doc.metadata.get("page_number") == 13]

for doc in first_page_docs:
    print(doc.page_content)

# Convert the following line below to #%% if you want to run the render_page as a single line and see output like in .ipynb but you 
# need to convert other lines also as cells. Just convert the whole lines as cells before and after this line to do that. 
# % % 
render_page(doc_list=docs, file_path=file_path, page_number=8)

# More information on extracting the text from images, extract text from a specific section of a pdf, etc. on how to do it is present 
# in this link: https://python.langchain.com/docs/how_to/document_loader_pdf/ and below that implementation is also added


# Extracting text from specific sections
render_page(doc_list=docs, file_path=file_path, page_number=5, print_text=False)  # Here, we are extracting text present in 
# "Sections contained in this Guide". This works by identifying the category and then exact name of the title text (page_content)
# then element_id of that title is extracted and all the documents with this parent_id is the text you want.

sections = []
parent_id = -1
for doc in docs:
    if doc.metadata["category"] == "Title" and "1.1 Sections contained in this Guide" in doc.page_content:
        parent_id = doc.metadata["element_id"]
    if doc.metadata.get("parent_id") == parent_id:
        sections.append(doc)

for doc in sections:
    print(doc.page_content)



# Extracting Text from images (Since there are no images in the document not customizing it, here is the code as it is as found in the 
# langchain documentation link)
render_page(docs, 11)




