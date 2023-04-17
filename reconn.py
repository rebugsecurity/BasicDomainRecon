import requests

# Define the target domain
target_domain = "sltbs1.com"

# Performing the DNS lookup.
def dns_lookup(domain):
    try:
        response = requests.get(f"https://dns.google/resolve?name={domain}", timeout=5)
        if response.status_code == 200:
            dns_records = response.json()
            print("DNS Records for", domain)
            print("A Records:")
            for record in dns_records["Answer"]:
                if record["type"] == 1:
                    print(record["data"])
            print("MX Records:")
            for record in dns_records["Answer"]:
                if record["type"] == 15:
                    print(record["data"])
        else:
            print("Failed to perform basic DNS lookup for", domain)
    except requests.exceptions.Timeout:
        print("DNS Lookup timeout for", domain)
    except Exception as e:
        print("Failed to perform DNS lookup for", domain, ":", e)

# Perform a WHOIS Lookup:
def whois_lookup(domain):
    try:
        response = requests.get(f"https://whois.iana.org/whois?query={domain}", timeout=5)
        if response.status_code == 200:
            whois_data = response.text
            print("WHOIS Information for:", domain)
            print(whois_data)
        else:
            print("Failed to perform WHOIS lookup for:", domain)
    except requests.exceptions.Timeout:
        print("WHOIS lookup timeout for", domain)
    except Exception as e:
        print("Failed to perform WHOIS lookup for:", domain, ":", e)


# Perform port scanning
def port_scan(domain, ports):
    try:
        for port in ports:
            response = requests.get(f"https://{domain}:{port}", timeout=5)
            if response.status_code == 200:
                print(f"Port {port} is Open on:", domain)
            else:
                print(f"Port {port} is Closed on:", domain)
    except requests.exceptions.Timeout:
        print(f"Port {port} is FILTERED on:", domain)
    except Exception as e:
        print(f"Failed to perform port scan for port {port} on:", domain, ":", e)

# Now lets call the functions
dns_lookup(target_domain)
whois_lookup(target_domain)
port_scan(target_domain, [21, 22, 53, 80, 443, 8080])