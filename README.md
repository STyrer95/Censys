# Censys

The censys.certificates module provides a Python interface for interacting with the Censys Certificates API, which allows us to search for and retrieve information about X.509 certificates.
The CENSYS_API_ID and CENSYS_API_SECRET variables should be replaced with your own Censys API credentials.
The query variable specifies the search query we want to run. We're looking for X.509 certificates associated with the censys.io domain that are tagged as "trusted".
The fields variable specifies the fields we want to retrieve from each search result. In this case, we want the SHA256 fingerprint of the certificate, as well as its validity start and end dates.
We then open a CSV file for writing ('censys_certificates.csv') and create a csv.writer object to write rows to the file. We also write the header row containing the column names.
We use a for loop to iterate over the search results returned by censys_certificates.search(query, fields). For each result, we check whether the certificate is unexpired by comparing its validity end date to the current time (censys.certificates.CensysCertificates.get_current_time()). If the certificate is unexpired, we write its SHA256 fingerprint, validity start date, and validity end date to the CSV file.
