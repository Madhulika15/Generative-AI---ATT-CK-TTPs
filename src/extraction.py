# Extract IOCs (IP addresses, domains, and emails)
def extract_iocs(text):
    # IP Address Pattern (IPv4)
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ips = re.findall(ip_pattern, text)

    # Domain Pattern (matches domains but not IP addresses)
    domain_pattern = r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b'
    domains = re.findall(domain_pattern, text)

    # Email Pattern
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)

    # Remove domains that are part of extracted emails to avoid duplication
    domains = [d for d in domains if d not in emails]

    return ips, domains, emails

# Sample Threat Report with IOCs
sample_report_with_iocs = """
The attacker used spear-phishing to gain initial access.
They connected to 203.0.113.45 and downloaded a malicious payload from badactor.org.
Phishing emails were sent from attacker@evilcorp.com.
"""

# Extract IOCs
ips, domains, emails = extract_iocs(sample_report_with_iocs)
