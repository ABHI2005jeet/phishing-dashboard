# phishing_checker.py

def get_risk_level(message):
    keywords = {
        "urgent": "⚠️ Urgency tactic",
        "verify": "⚠️ Asking for verification",
        "click here": "⚠️ Clickable link",
        "update": "⚠️ Wants info update",
        "password": "⚠️ Password-related",
        "account": "⚠️ Mentions account",
        "login": "⚠️ Login request",
        "prize": "⚠️ Fake rewards",
        "limited time": "⚠️ Pressure tactic"
    }

    reasons = [v for k, v in keywords.items() if k in message.lower()]
    score = len(reasons)

    if score >= 4:
        level = "🔴 High Risk"
        advice = "❌ Do NOT trust this message."
    elif score >= 2:
        level = "🟠 Medium Risk"
        advice = "⚠️ Be cautious. Don’t click links."
    else:
        level = "🟢 Low Risk"
        advice = "✅ Seems safe."

    return level, reasons, advice

def generate_html(messages):
    rows = ""
    for msg in messages:
        level, reasons, advice = get_risk_level(msg)
        reason_html = "<ul>" + "".join(f"<li>{r}</li>" for r in reasons) + "</ul>" if reasons else "None"
        rows += f"""
        <tr>
            <td>{msg}</td>
            <td>{level}<br><small>{advice}</small></td>
            <td>{reason_html}</td>
        </tr>
        """

    html_content = f"""
    <html>
    <head>
        <title>Phishing Report</title>
        <link rel="stylesheet" href="static/style.css">
    </head>
    <body>
        <h1>🛡️ Phishing Detection Report</h1>
        <p>Below are your scanned results:</p>
        <table>
            <tr>
                <th>Message</th>
                <th>Risk Level</th>
                <th>Reasons</th>
            </tr>
            {rows}
        </table>
        <footer><p style="text-align:center;">Made by Abhijeet 🚀</p></footer>
    </body>
    </html>
    """

    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("✅ report.html generated successfully!")

def read_messages():
    with open("messages.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

generate_html(read_messages())

