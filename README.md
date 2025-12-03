# 🛡️ AntiPhishing Browser Extension

**AntiPhishing Extension** is a security-focused browser extension developed to detect and prevent malicious URL attacks in real-time. Built using **Chrome Manifest V3**, it analyzes links before navigation occurs, protecting users from social engineering attacks, typosquatting, and deceptive redirects.

This project was developed for the *Cybersecurity* course (Master’s Degree in Engineering in Computer Science) at the **University of Messina**.

---

## 🚨 The Problem
Phishing attacks rely on social engineering rather than technical exploits. Common vectors include:
*   **Typosquatting:** `g00gle.com` instead of `google.com`.
*   **URL Shorteners:** Hiding malicious payloads behind `bit.ly` links.
*   **Homograph Attacks:** Visually similar domains.
*   **Protocol Downgrade:** Forcing HTTP over HTTPS.

## ✨ Key Features

The extension implements a multi-layered detection algorithm (`content.js`) that runs entirely client-side:

*   **🔍 Typosquatting Detection**: Uses the **Levenshtein Distance Algorithm** (Dynamic Programming) to calculate the edit distance between the visited domain and a list of trusted brands (e.g., Google, PayPal, Amazon).
*   **🔗 Shortener Expansion Warning**: Flags known URL shorteners commonly used to obfuscate phishing sites.
*   **⚠️ Suspicious Keyword Analysis**: Detects urgent or security-related terms (e.g., "login", "verify", "update") in non-trusted domains.
*   **🔢 Direct IP & Protocol Checks**: Warns users if they are navigating to a direct IP address or an insecure HTTP connection.
*   **📏 Heuristic Analysis**: Flags abnormally long URLs often used to hide parameters.
*   **🛑 Interactive Warning System**: Displays a modal overlay preventing accidental navigation, giving the user the choice to proceed or go back.

## 🛠️ Tech Stack

*   **Core**: JavaScript (ES6+), HTML5, CSS3.
*   **Architecture**: Chrome Extensions API (**Manifest V3**).
*   **Algorithm**: Levenshtein Distance (Time Complexity: $O(m \times n)$).
*   **Privacy**: Zero-knowledge architecture (no data is sent to external servers; all analysis is local).

## 🚀 Installation & Usage

Since this is a developer build, you need to load it manually in Chrome (or Edge/Brave).

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Francesco-Mon/cybersecurity.git
    ```

2.  **Open Extension Management**:
    *   Open Chrome and navigate to `chrome://extensions/`.
    *   Toggle **Developer mode** (top right switch).

3.  **Load the Extension**:
    *   Click **Load unpacked**.
    *   Select the folder where you cloned the repository.

4.  **Test the Protection**:
    *   Open the included `test.html` file in your browser.
    *   Click on the simulated phishing links to see the detection algorithm in action.

## 🧠 Algorithmic Implementation

The core logic relies on the Levenshtein Distance to identify brand impersonation. Here is a high-level overview of the implementation:

```javascript
// Dynamic Programming approach to find edit distance
function levenshtein(a, b) {
    // Matrix initialization and calculation...
    // Returns the minimum number of single-character edits 
    // (insertions, deletions or substitutions) required to change 'a' into 'b'.
}

// If distance is > 0 and <= 2, it is flagged as a potential typosquatting attack.
```

## 🔒 Privacy & Security
* **Client-Side Only**: No browsing history or URLs are transmitted to any external server.
* **Minimal Permissions**: The extension requests only the necessary permissions defined in manifest.json.
* **Safe Injection**: Uses content scripts securely to monitor DOM interactions without compromising page integrity.
<p align="center">
Developed by <a href="https://github.com/Francesco-Mon">Francesco Montecucco</a> - University of Messina
</p>
