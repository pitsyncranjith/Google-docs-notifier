import gdata.docs.service
import getpass

client = gdata.docs.service.DocsService()

email = raw_input('Enter your email :')
password = getpass.getpass('Enter your password :')

client.ClientLogin(email, password)

documents_feed = client.GetDocumentListFeed()

for documents in documents_feed.entry:
	print documents.title.text
