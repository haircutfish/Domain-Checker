# Domain Checker

The script is used to check the validity of a domain.  It checks the Creation Date, Expiration Date, and when the WHOis record was last updated.  It also checks the following DNS records: A, AAAA, NS, CNAME, PTR, MX, and TXT.  Lastly, it will Curl the website to see what HTTP headers are sent back.

### Requirements
`dc.py` uses python3 along with several modules that you installing in the **Installation** section.

### Installation
Follow these steps to install the the script on your system
```
cd ~
git clone https://github.com/haircutfish/Domain-Checker.git
sudo chmod 755 ~/Domain-Checker/dc.py
python3 -m pip install --user -r ~/Domain-Checker/requirements.txt
sudo ln -s ~/Domain-Checker/dc.py /usr/local/bin/dc.py
```

### Usage:
To use this python script type the following command
```
dc.py {domain.name}
```

### example: 
```
dc.py haircutfish.com
```

### Output:
```
      =================================
           ***Domain Information***    
      ================================= 
       
Creation date   : 2022-12-13 19:29:09+00:00
Expiration date : 2024-12-13 19:29:09+00:00
Updated date    : 2023-09-14 10:26:37+00:00
A Record        : ['185.199.109.153', '185.199.111.153', '185.199.108.153', '185.199.110.153']
AAAA Record     : ['2606:50c0:8000::153', '2606:50c0:8001::153', '2606:50c0:8002::153', '2606:50c0:8003::153']
NS Record       : ['ns3.linode.com.', 'ns5.linode.com.', 'ns4.linode.com.', 'ns1.linode.com.', 'ns2.linode.com.']
CNAME Record    : No Results Found
PTR Record      : No Results Found
MX Record       : No Results Found
TXT Record      : ['"spf=v1 -all"']
Curl            : HTTP/1.1 301 Moved Permanently, HTTP/2 200
```

### Author:
Dan Rearden