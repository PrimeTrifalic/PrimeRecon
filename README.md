```
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║              🔍 PRIMERECON - Web Reconnaissance Toolkit 🔍               ║
║                                                                           ║
║            Advanced Banner Grabbing & Port Scanning Suite                ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

# 🎯 PrimeRecon

> **Scan fast, look gorgeous** — A powerful Python-based reconnaissance toolkit for security professionals and ethical hackers.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Banner Grabber](#banner-grabber)
  - [Open Ports Scanner](#open-ports-scanner)
- [Author](#author)
- [License](#license)

---

## 🌟 Overview

**PrimeRecon** is a comprehensive web reconnaissance toolkit designed for penetration testers and security researchers. It provides fast, efficient tools for:

- **Banner Grabbing** — Extract HTTP headers and server information
- **Port Scanning** — Identify open ports with multi-threaded scanning
- **Colorized Output** — Beautiful, decorative terminal output for enhanced visibility

Perfect for initial reconnaissance phases of security assessments.

---

## ✨ Features

### 🎨 **Decorative & Colorful**
- Rainbow gradient ANSI color support
- Fancy Unicode box borders
- Multi-threaded performance indicators
- Terminal-aware responsive design

### 🔧 **Banner Grabber** (`bannerGrabber.py`)
- Connect to target hosts via HTTP
- Extract server headers and banner information
- Save results to custom directories/files
- Configurable timeout settings
- Error handling & graceful fallbacks

### 🚀 **Port Scanner** (`openPortsScanner.py`)
- Fast, multi-threaded port scanning
- Customizable port range scanning
- Identify open/closed ports in real-time
- Export results to files
- Timeout control per connection attempt

### 📦 **Banner Module** (`banner.py`)
- Enhanced ASCII art banners using figlet
- Per-character color cycling with 256-color palette
- Subtitle and timestamp support
- Box drawing with Unicode borders
- Automatic terminal width detection

---

## 📁 Project Structure

```
webRecon/
├── main.py                    # Main entry point (future)
├── README.md                  # This file
├── requirements.txt           # Python dependencies
│
└── components/
    ├── __init__.py            # Package initialization
    ├── banner.py              # 🎨 Decorative banner system
    ├── bannerGrabber.py       # 🌐 HTTP banner extraction
    ├── openPortsScanner.py    # 🔍 Multi-threaded port scanner
    └── results.txt            # Sample output file
```

---

## 🛠️ Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PrimeTrifalic/PrimeRecon.git
   cd webRecon
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Or manually install required packages:
   ```bash
   pip install pyfiglet colorama
   ```

---

## 🚀 Usage

### 🎨 Banner Grabber

Extract HTTP headers and server information from a target host.

#### **Basic Usage:**
```bash
python3 components/bannerGrabber.py -t <target> -p <port>
```

#### **Full Options:**
```bash
python3 components/bannerGrabber.py \
  -t example.com              # Target host/IP (required)
  -p 80                       # Target port (default: 80)
  -w 2                        # Timeout in seconds (default: 2)
  -d ./results                # Output directory (optional)
  -f banner.txt               # Output filename (optional)
```

#### **Examples:**
```bash
# Grab banner from example.com on port 80
python3 components/bannerGrabber.py -t example.com

# Custom port with timeout
python3 components/bannerGrabber.py -t 192.168.1.1 -p 8080 -w 5

# Save results to file
python3 components/bannerGrabber.py -t example.com -d ./output -f banner.txt
```

---

### 🔍 Open Ports Scanner

Scan a target host for open ports using multi-threaded connections.

#### **Basic Usage:**
```bash
python3 components/openPortsScanner.py -t <target> -i <start> -f <end>
```

#### **Full Options:**
```bash
python3 components/openPortsScanner.py \
  -t example.com              # Target host/IP (required)
  -i 1                        # Starting port (required)
  -f 1000                     # Ending port (required)
  -w 2                        # Timeout in seconds (default: 2)
  -d ./results                # Output directory (optional)
  -o ports.txt                # Output filename (optional)
```

#### **Examples:**
```bash
# Scan common ports 1-1000
python3 components/openPortsScanner.py -t example.com -i 1 -f 1000

# Scan web service ports with custom timeout
python3 components/openPortsScanner.py -t 192.168.1.1 -i 80 -f 443 -w 3

# Save results to file
python3 components/openPortsScanner.py -t example.com -i 1 -f 65535 -d ./scans -o open_ports.txt
```

---

## 🎭 Banner Display

The custom banner module displays a decorative, colorful header before each scan:

```bash
python3 -c "from components.banner import print_banner; print_banner('PrimeRecon', subtitle='v1.0')"
```

**Features:**
- Full-width rainbow gradient colors
- Unicode box borders
- Embedded timestamp
- Custom subtitles
- Terminal auto-sizing

---

## 👤 Author

**PrimeTrifalic**

- 🐙 GitHub: [PrimeTrifalic](https://github.com/PrimeTrifalic)
- 📧 Repository: [PrimeRecon](https://github.com/PrimeTrifalic/PrimeRecon)

---

## ⚠️ Disclaimer

**Legal Notice:** This toolkit is designed for authorized security testing and educational purposes only. Unauthorized access to computer systems is illegal. Always obtain written permission before performing any security assessments. The author is not responsible for misuse or illegal activities.

---

## 📜 License

This project is provided as-is for educational and authorized security testing purposes.

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues, fork the repository, and create pull requests.

---

## 📞 Support

For issues, questions, or feature requests, please open an issue on the [GitHub repository](https://github.com/PrimeTrifalic/PrimeRecon/issues).

---

**Made by PrimeTrifalic**