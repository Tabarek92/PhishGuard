# PhishGuard

AI-powered email threat detection tool built for university students. Paste any suspicious email and get an instant, detailed analysis powered by Claude.

## Features

- **Threat classification** — Detects Phishing, Fraud, Spam, Spear Phishing, and Legitimate emails
- **Threat score** — 0–100 risk score with a visual bar
- **Evidence highlighting** — Quotes the specific text from the email that triggered each red flag
- **Educational insights** — Explains the social engineering technique used so you can recognize it in the future
- **Sample emails** — Six realistic examples (phishing, fraud, spam, legitimate, spear phish) loaded in one click
- **Ask anything** — Chat mode for general questions about phishing tactics and defenses

## Getting Started

### Requirements

- Python 3.x
- An [Anthropic API key](https://console.anthropic.com/)

### Run locally

```bash
git clone git@github.com:Tabarek92/PhishGuard.git
cd PhishGuard
python3 server.py
```

Then open **http://localhost:8080** in your browser.

The server proxies requests to the Anthropic API — your key is never stored, only used for the current session.

## Usage

1. Enter your Anthropic API key in the input at the top
2. Paste a suspicious email into the **Paste Email** tab and click **ANALYZE THREAT**
3. Or switch to **Ask Question** to ask anything about email security

## Project Structure

```
PhishGuard/
├── index.html   # Frontend — UI, formatting logic, API integration
└── server.py    # Lightweight Python server + Anthropic API proxy
```
