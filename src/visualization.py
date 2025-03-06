# Display Extracted IOCs
print("\n Extracted IOCs:")
print("IP Addresses:", ips)
print("Domains:", domains)
print("Emails:", emails)
# Full Analysis Function: Extract both TTPs and IOCs
def analyze_report(report, mapping_df):
    # Extract TTPs
    detected_ttps = extract_ttps(report, mapping_df)

    # Extract IOCs
    ips, domains, emails = extract_iocs(report)

    # Display Results
    print("\n Analysis Results:")

    # Show TTPs
    if detected_ttps:
        print("\nDetected TTPs:")
        for technique, tactic in detected_ttps:
            print(f"Technique: {technique} | Tactic: {tactic}")
    else:
        print("No TTPs detected.")

    # Show IOCs
    print("\nDetected IOCs:")
    print(f"- IP Addresses: {ips if ips else 'None'}")
    print(f"- Domains: {domains if domains else 'None'}")
    print(f"- Emails: {emails if emails else 'None'}")

# Analyze a Sample Report
new_report = """
The attacker used spear-phishing for initial access and employed PowerShell scripts.
They connected to 45.67.89.101 and downloaded a malicious payload from attackerdomain.org.
Phishing emails were sent to victims from hacker@badactor.net.
"""

analyze_report(new_report, merged_df)


# Save detected TTPs to CSV
def save_results_to_csv(detected_ttps, ips, domains, emails, filename="detected_results.csv"):
    # Prepare the data
    results = []
    for technique, tactic in detected_ttps:
        results.append({
            "Technique": technique,
            "Tactic": tactic
        })
    
    for ip in ips:
        results.append({"IP Address": ip})
    
    for domain in domains:
        results.append({"Domain": domain})

    for email in emails:
        results.append({"Email": email})

    # Create and save DataFrame
    results_df = pd.DataFrame(results)
    results_df.to_csv(filename, index=False)
    print(f"\n Results saved to {filename}")

# Example Usage
ips, domains, emails = extract_iocs(new_report)
save_results_to_csv(detected_ttps, ips, domains, emails)

