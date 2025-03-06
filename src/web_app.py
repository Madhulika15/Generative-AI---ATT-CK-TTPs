# Gradio Prediction Function
def analyze_with_ui(input_text):
    # Run TTP and IOC extraction
    detected_ttps = extract_ttps(input_text, merged_df)
    ips, domains, emails = extract_iocs(input_text)

    # Format output
    output = "Analysis Results:\n"

    # Add TTPs to the output
    if detected_ttps:
        output += "Detected TTPs:\n"
        for technique, tactic in detected_ttps:
            output += f"- Technique: {technique} | Tactic: {tactic}\n"
    else:
        output += "**No TTPs detected.**\n"

    # Add IOCs to the output
    output += "\nDetected IOCs:\n"
    output += f"- IP Addresses: {', '.join(ips) if ips else 'None'}\n"
    output += f"- Domains: {', '.join(domains) if domains else 'None'}\n"
    output += f"- Emails: {', '.join(emails) if emails else 'None'}\n"

    return output

# Launch Gradio Interface
iface = gr.Interface(fn=analyze_with_ui, inputs="text", outputs="text", title="ATT&CK TTP & IOC Extractor")
iface.launch()

