# DNS Tool (CLI)

A comprehensive Python Command Line Interface (CLI) utility for performing various DNS operations, diagnostics, and domain lookup services.

---

## 🚀 Features

The tool provides an interactive CLI menu with the following capabilities:

1. **DNS Lookup**:
   - Query common DNS records for any domain name.
   - Supported record types: `A`, `AAAA`, `MX`, `NS`, `TXT`, `CNAME`, `SOA`, `CAA`, `PTR`, and `SRV`.

2. **Reverse DNS Lookup**:
   - Resolve an IP address back to its associated hostname (PTR record lookup).

3. **DNS Response Time**:
   - Measure the exact time (in milliseconds) taken to query a specific DNS record for a domain.

4. **WHOIS Lookup**:
   - Retrieve registration details for a domain, including:
     - Registrar
     - Creation, expiration, and last updated dates
     - Name servers
     - Domain status and administrative emails

5. **DNSSEC Check**:
   - Check if Domain Name System Security Extensions (DNSSEC) is enabled and configured for a domain.
   - Queries and returns `DNSKEY`, `DS`, and `RRSIG` records.

6. **JSON Export Utility**:
   - Underlying logic in `modules/export_json.py` supports exporting results directly into the `output/` directory as JSON files.

---

## 📁 Project Structure

```text
dns_lookup/
│
├── main.py                 # Application entrypoint & CLI interactive menu
├── config.py               # Config parameters (timeout settings, DNS servers)
├── requirements.txt        # Third-party library dependencies
│
├── modules/                # Core implementation logic
│   ├── dns_lookup.py       # Standard DNS records query module
│   ├── reverse_lookup.py   # IP-to-hostname reverse resolver
│   ├── response_time.py    # Query response latency measuring module
│   ├── whois_lookup.py     # WHOIS domain registration details lookup
│   ├── dnssec.py           # DNSSEC configuration checking module
│   └── export_json.py      # Results exporting utility
│
├── output/                 # Directory where export results are saved
└── worldlists/             # Directory for wordlists (if any)
```

---

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.6+
- pip (Python package installer)

### Step 1: Install Dependencies
Install all required libraries using `requirements.txt`:
```bash
pip install -r requirements.txt
```

*Libraries installed:*
* `dnspython`: For performing DNS resolutions.
* `python-whois`: For fetching WHOIS information.
* `rich`: For rich text formatting in terminals.

### Step 2: Run the Application
Start the interactive CLI menu:
```bash
python main.py
```

---

## ⚙️ Configuration

You can customize global settings in [config.py](file:///d:/AI%20Study/python/dns_lookup/config.py):
* `DEFAULT_TIMEOUT`: Timeout duration in seconds for requests (default: `5`).
* `DEFAULT_DNS_SERVER`: Specific DNS resolver server to query (default: `None` - uses system default resolver).
