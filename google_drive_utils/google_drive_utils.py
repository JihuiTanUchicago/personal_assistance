from google.oauth2 import service_account
from googleapiclient.discovery import build

# Mental Departments Document ID
EXECUTOR = "1EPBmlVCro3rEDfnAZCeFhAlOvZc0Z7p6aYUtjez7IzM"

# Load credentials
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build the Docs API client
docs_service = build('docs', 'v1', credentials=credentials)

# Retrieve document content
def get_doc(document_id):
    # Retrieve document content
    doc = docs_service.documents().get(documentId=document_id).execute()

    return doc

def get_table_below_heading(doc, heading_text):
    content = doc.get('body', {}).get('content', [])
    found_heading = False

    for i, element in enumerate(content):
        # Look for heading with styled name (e.g., TITLE, HEADING_1)
        if 'paragraph' in element:
            style = element['paragraph'].get('paragraphStyle', {})
            text_elems = element['paragraph'].get('elements', [])

            full_text = ''.join(
                el.get('textRun', {}).get('content', '').strip() for el in text_elems
            )

            if full_text == heading_text and style.get('namedStyleType', '').startswith('HEADING') or style.get('namedStyleType') == 'TITLE':
                found_heading = True
                continue  # move to next element

        # Once heading is found, find the first table right after
        if found_heading and 'table' in element:
            table = element['table']
            rows = []
            for row in table['tableRows']:
                row_cells = []
                for cell in row['tableCells']:
                    cell_text = ''
                    for cell_elem in cell['content']:
                        if 'paragraph' in cell_elem:
                            for run in cell_elem['paragraph']['elements']:
                                cell_text += run.get('textRun', {}).get('content', '')
                    row_cells.append(cell_text.strip())
                rows.append(row_cells)
            return rows

    return []

# print(read_text(document_id))
document = get_doc(EXECUTOR)
table = get_table_below_heading(document, 'Current Goals')
print(table)
