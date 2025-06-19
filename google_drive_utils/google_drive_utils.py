from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load credentials
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build the Docs API client
docs_service = build('docs', 'v1', credentials=credentials)

# Replace with your actual Google Doc ID (from its URL)
DOCUMENT_ID = '17AKsmdddNJ3CCO2BPwBak3Tl2jjn93kWYfD8mpwlt8I'

# Retrieve document content
doc = docs_service.documents().get(documentId=DOCUMENT_ID).execute()

# Extract and print plain text
def read_text(doc):
    text = ''
    for element in doc.get('body', {}).get('content', []):
        if 'paragraph' in element:
            for run in element['paragraph']['elements']:
                text += run.get('textRun', {}).get('content', '')
    return text

print(read_text(doc))
