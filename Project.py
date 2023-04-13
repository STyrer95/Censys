import censys.certificates
import csv

# Set up Censys API credentials
CENSYS_API_ID = "your_api_id_here"
CENSYS_API_SECRET = "your_api_secret_here"
censys_certificates = censys.certificates.CensysCertificates(api_id=CENSYS_API_ID, api_secret=CENSYS_API_SECRET)

# Set up search query parameters
query = 'parsed.names: censys.io AND tags: trusted'
fields = ['parsed.fingerprint_sha256', 'parsed.validity.start', 'parsed.validity.end']

# Get search results and write to CSV
with open('censys_certificates.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['SHA256 Fingerprint', 'Validity Start', 'Validity End'])
    for result in censys_certificates.search(query, fields):
        if result['parsed.validity.end'] >= censys.certificates.CensysCertificates.get_current_time():
            writer.writerow([result['parsed.fingerprint_sha256'], result['parsed.validity.start'], result['parsed.validity.end']])
