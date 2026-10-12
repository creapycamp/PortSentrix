# PortSentrix 🔍
### Python-Based TCP Port Scanner for Ethical Cybersecurity

**PortSentrix** is a lightweight Python-based network reconnaissance tool designed to identify open TCP ports on one or multiple authorized target systems. It helps cybersecurity enthusiasts understand network exposure, discover accessible services, and practice fundamental port-scanning techniques.

---

## 📌 Project Overview

Ports are communication endpoints that allow applications and services to exchange data over a network. Identifying open ports is an important step in network reconnaissance and security assessment.

PortSentrix automates basic TCP port scanning by attempting to establish connections to ports within a user-defined range. It supports scanning a single target or multiple targets in one execution.

## ✨ Features

- **TCP Port Scanning:** Checks TCP ports by attempting socket connections.
- **Multiple Target Support:** Accepts multiple target IP addresses or hostnames separated by commas.
- **Custom Port Range:** Allows users to specify the upper limit of the port scan.
- **Open Port Detection:** Displays ports where TCP connections succeed.
- **Colored Terminal Output:** Uses `termcolor` to highlight multiple-target scanning status.
- **Lightweight Implementation:** Built with Python's standard `socket` library and a minimal external dependency.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| `socket` | Establishes TCP connections to target ports |
| `termcolor` | Adds color to terminal output |
| PyCharm | Development environment |
| Git and GitHub | Version control and project hosting |

## ⚙️ How It Works

1. The user enters one target or multiple comma-separated targets.
2. The user specifies the number of ports to scan.
3. PortSentrix iterates through port numbers starting at port 1.
4. It attempts a TCP connection to each port.
5. If a connection succeeds, the port is displayed as open.
6. Connection failures are silently ignored.

**Note:** The scanner currently checks ports from `1` up to, but not including, the number entered by the user.

For example, entering `1000` checks ports **1–999**, not port 1000.

## 📥 Installation

### Prerequisites

- Python 3 installed on your computer.
- Git (optional, for cloning the repository).
- Network access to authorized targets.

### 1. Clone the Repository

```bash
git clone https://github.com/creapycamp/PortSentrix.git
```

### 2. Navigate to the Project Directory

```bash
cd PortSentrix
```

### 3. Install the Dependency

```bash
python -m pip install termcolor
```

The `socket` module is included with Python and does not require separate installation.

## ▶️ Usage

Run the Python script containing the scanner code. If the file is named `main.py`, use:

```bash
python main.py
```

Replace `main.py` with your actual Python filename if it is different.

### Example 1: Scan a Single Target

```text
Enter Targets to Scan (Split them by ',' ): 192.168.1.1
Enter how many Ports You want to Scan: 100
```

The scanner attempts TCP connections to ports 1–99 on the specified target.

### Example 2: Scan Multiple Targets

```text
Enter Targets to Scan (Split them by ',' ): 192.168.1.1,192.168.1.10
Enter how many Ports You want to Scan: 100
```

PortSentrix scans ports 1–99 on each target sequentially.

### Example Output

```text
Starting Scan For 192.168.1.1
[+] Port Open 22
[+] Port Open 80

Starting Scan For 192.168.1.10
[+] Port Open 443
```

*Illustrative output only. Actual results depend on the target, network conditions, and firewall rules.*

## 🔐 Ethical Use and Disclaimer

PortSentrix is intended for educational purposes, authorized network reconnaissance, and cybersecurity learning.

- Scan only systems you own or have explicit permission to test.
- Respect organizational security policies and applicable laws.
- Do not use the tool to access, disrupt, or compromise unauthorized systems.
- Open ports do not automatically indicate vulnerabilities; further authorized assessment is required.

The author is not responsible for misuse of this software.

## 🚀 Future Improvements

Potential enhancements for future versions include:

- Add connection timeouts to prevent slow scans.
- Report closed, filtered, and unreachable ports where they can be reliably distinguished.
- Add configurable starting and ending port numbers.
- Add multithreading or asynchronous scanning to improve performance.
- Export scan results to CSV or text reports.
- Add input validation and exception-specific error handling.
- Generate summaries comparing the number of open ports across targets.
- Add progress indicators and scan duration reporting.

## 👨‍💻 Author

**creapycamp**

GitHub: [https://github.com/creapycamp](https://github.com/creapycamp)


**PortSentrix — Discover Open Ports. Understand Network Exposure. Practice Ethical Security.**
