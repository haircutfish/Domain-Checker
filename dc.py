#!/usr/bin/env python3
# First step is to import the package
import whois21
import sys
import pydig
import subprocess

if len(sys.argv) == 1:
        print("""
        ======================================================        
        No Domain or IP address was giving.  Please try again.
        ======================================================
              """)
        exit()

query = sys.argv[1]

# Running pydig, then checking to see if any results
# If non found, append variable with No Results Found
a_record = pydig.query(query,'A')
if not a_record:
    a_record = "No Results Found"

aaaa_record = pydig.query(query, 'AAAA')
if not aaaa_record:
    aaaa_recordd = "No Results Found"

ns_record = pydig.query(query, 'NS')
if not ns_record:
    ns_record = "No Results Found"

cname_record = pydig.query(query, 'CNAME')
if not cname_record:
    cname_record = "No Results Found"

ptr_record = pydig.query(query, 'PTR')
if not ptr_record:
    ptr_record = "No Results Found"

mx_record = pydig.query(query, 'MX')
if not mx_record:
    mx_record = "No Results Found"

txt_record = pydig.query(query, 'TXT')
if not txt_record:
    txt_record = "No Results Found"

# Second step is to create an instance of the WHOIS class
whois = whois21.WHOIS(query)

# Third step is to check if the operation was successful
if not whois.success:
    print(whois.error)
    exit()

# Using pycurl to curl the webpage to see what results we get
curl = subprocess.getoutput(f'curl -sIL {query} | grep HTTP | tr -d "\n"')

curl = curl.replace("\n",", ")


print ("""
      =================================
           ***Domain Information***    
      ================================= 
       """)
print(f'Creation date   : {whois.creation_date}')
print(f'Expiration date : {whois.expires_date}')
print(f'Updated date    : {whois.updated_date}')
print(f'A Record        : {a_record}')
print(f'AAAA Record     : {aaaa_record}')
print(f'NS Record       : {ns_record}')
print(f'CNAME Record    : {cname_record}')
print(f'PTR Record      : {ptr_record}')
print(f'MX Record       : {mx_record}')
print(f'TXT Record      : {txt_record}')
print(f'Curl            : {curl}')
exit()