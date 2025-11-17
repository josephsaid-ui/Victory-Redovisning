# 🚀 Nivå 5: Expert - AI-driven OSINT, Cloud Security & Modern DevSecOps

> **"The future belongs to those who learn more skills and combine them in creative ways." - Robert Greene**
>
> 📚 Läsningstid: 90-120 min | 🎯 Övningar: 8 + ENTERPRISE PROJEKT | 💡 Svårighetsgrad: Expert

---

## 🗺️ Navigation
**[⬅️ Tillbaka till Nivå 4](OSINT_ZAP_Guide_Niva_4.md)** | **[🏠 Översikt](OSINT_ZAP_Guide_README.md)**

---

## 🎯 Vad du lär dig i denna nivå

Efter att ha läst Nivå 5 kommer du att:
- ✅ Använda AI och Machine Learning för OSINT-automation
- ✅ Integrera säkerhetstestning i CI/CD-pipelines (DevSecOps)
- ✅ Testa och säkra molnmiljöer (AWS, Azure, GCP)
- ✅ Genomföra Container Security Testing (Docker, Kubernetes)
- ✅ Automatisera hela pentesting-arbetsflöden
- ✅ Använda moderna API security testing tekniker (GraphQL, REST, gRPC)
- ✅ Implementera Threat Intelligence feeds
- ✅ Bygga egna säkerhetsverktyg med Python
- ✅ Genomföra Red Team operations
- ✅ Arbeta med Bug Bounty programs professionellt

---

## 🤖 Del 1: AI-Driven OSINT och Automation

### 🎯 AI i OSINT - Nästa Generation

**Varför AI i OSINT?**
- 📊 **Data Overload** - Mänsklig analys är för långsam
- 🎯 **Pattern Recognition** - AI hittar mönster vi missar
- ⚡ **Speed** - Analysera miljontals datapunkter på sekunder
- 🔮 **Predictive** - Förutsäga framtida hot

### 🧠 Machine Learning för Threat Intelligence

#### 1. Social Media Analysis med Natural Language Processing

**Installation:**
```bash
pip install tweepy nltk spacy tensorflow transformers
python -m spacy download en_core_web_sm
```

**Advanced Twitter OSINT Bot:**
```python
#!/usr/bin/env python3
"""
AI-Powered Twitter OSINT Tool
Uses NLP for sentiment analysis and entity extraction
"""

import tweepy
import spacy
from transformers import pipeline
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

class AITwitterOSINT:
    def __init__(self, api_key, api_secret, access_token, access_secret):
        """Initialize Twitter API and NLP models"""

        # Twitter API
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)

        # Load NLP models
        self.nlp = spacy.load("en_core_web_sm")
        self.sentiment_analyzer = pipeline("sentiment-analysis")

        print("[+] AI Twitter OSINT initialized")

    def analyze_user(self, username, tweet_count=200):
        """Deep analysis of a Twitter user"""

        print(f"[*] Analyzing @{username}...")

        # Get user info
        user = self.api.get_user(screen_name=username)

        # Get tweets
        tweets = self.api.user_timeline(
            screen_name=username,
            count=tweet_count,
            tweet_mode='extended'
        )

        analysis = {
            'user_info': {
                'name': user.name,
                'username': username,
                'followers': user.followers_count,
                'following': user.friends_count,
                'tweets': user.statuses_count,
                'created': user.created_at,
                'verified': user.verified,
                'location': user.location,
                'bio': user.description,
            },
            'tweets_analyzed': len(tweets),
            'entities': self._extract_entities(tweets),
            'sentiment': self._analyze_sentiment(tweets),
            'topics': self._extract_topics(tweets),
            'activity_pattern': self._analyze_activity(tweets),
            'network': self._analyze_network(tweets)
        }

        return analysis

    def _extract_entities(self, tweets):
        """Extract named entities using spaCy"""

        entities = {
            'PERSON': set(),
            'ORG': set(),
            'GPE': set(),  # Geopolitical entities (countries, cities)
            'PRODUCT': set(),
            'EVENT': set(),
            'URL': set(),
            'HASHTAG': set(),
            'MENTION': set()
        }

        for tweet in tweets:
            text = tweet.full_text

            # Extract hashtags and mentions
            entities['HASHTAG'].update(tweet.entities.get('hashtags', []))
            entities['MENTION'].update([m['screen_name'] for m in tweet.entities.get('user_mentions', [])])
            entities['URL'].update([u['expanded_url'] for u in tweet.entities.get('urls', [])])

            # NLP entity extraction
            doc = self.nlp(text)
            for ent in doc.ents:
                if ent.label_ in entities:
                    entities[ent.label_].add(ent.text)

        # Convert sets to sorted lists
        return {k: sorted(list(v)) for k, v in entities.items()}

    def _analyze_sentiment(self, tweets):
        """Sentiment analysis using transformers"""

        sentiments = []

        for tweet in tweets:
            try:
                result = self.sentiment_analyzer(tweet.full_text[:512])[0]
                sentiments.append({
                    'label': result['label'],
                    'score': result['score'],
                    'date': tweet.created_at
                })
            except:
                pass

        # Calculate statistics
        positive = sum(1 for s in sentiments if s['label'] == 'POSITIVE')
        negative = sum(1 for s in sentiments if s['label'] == 'NEGATIVE')

        return {
            'positive_count': positive,
            'negative_count': negative,
            'positive_percent': (positive / len(sentiments)) * 100 if sentiments else 0,
            'negative_percent': (negative / len(sentiments)) * 100 if sentiments else 0,
            'timeline': sentiments
        }

    def _extract_topics(self, tweets):
        """Extract common topics using keyword extraction"""

        from collections import Counter

        words = []

        for tweet in tweets:
            doc = self.nlp(tweet.full_text.lower())
            # Extract nouns and proper nouns
            words.extend([token.text for token in doc
                         if token.pos_ in ['NOUN', 'PROPN']
                         and len(token.text) > 3
                         and not token.is_stop])

        # Get top 20 topics
        return dict(Counter(words).most_common(20))

    def _analyze_activity(self, tweets):
        """Analyze posting patterns"""

        hours = [tweet.created_at.hour for tweet in tweets]
        days = [tweet.created_at.strftime('%A') for tweet in tweets]

        from collections import Counter

        return {
            'most_active_hours': dict(Counter(hours).most_common(5)),
            'most_active_days': dict(Counter(days).most_common(7)),
            'avg_tweets_per_day': len(tweets) / 30  # Approximate
        }

    def _analyze_network(self, tweets):
        """Analyze social network connections"""

        mentioned_users = []
        replied_to = []
        retweeted = []

        for tweet in tweets:
            # Mentions
            mentioned_users.extend([m['screen_name'] for m in tweet.entities.get('user_mentions', [])])

            # Replies
            if tweet.in_reply_to_screen_name:
                replied_to.append(tweet.in_reply_to_screen_name)

            # Retweets
            if hasattr(tweet, 'retweeted_status'):
                retweeted.append(tweet.retweeted_status.user.screen_name)

        from collections import Counter

        return {
            'top_mentioned': dict(Counter(mentioned_users).most_common(10)),
            'top_replied': dict(Counter(replied_to).most_common(10)),
            'top_retweeted': dict(Counter(retweeted).most_common(10))
        }

    def generate_report(self, analysis, output_file='osint_report.html'):
        """Generate HTML report from analysis"""

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>OSINT Report - @{analysis['user_info']['username']}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .section {{ margin: 20px 0; padding: 15px; border: 1px solid #ddd; }}
                .positive {{ color: green; }}
                .negative {{ color: red; }}
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #4CAF50; color: white; }}
            </style>
        </head>
        <body>
            <h1>🔍 OSINT Report: @{analysis['user_info']['username']}</h1>

            <div class="section">
                <h2>👤 User Information</h2>
                <p><strong>Name:</strong> {analysis['user_info']['name']}</p>
                <p><strong>Username:</strong> @{analysis['user_info']['username']}</p>
                <p><strong>Followers:</strong> {analysis['user_info']['followers']:,}</p>
                <p><strong>Following:</strong> {analysis['user_info']['following']:,}</p>
                <p><strong>Location:</strong> {analysis['user_info']['location']}</p>
                <p><strong>Bio:</strong> {analysis['user_info']['bio']}</p>
                <p><strong>Verified:</strong> {'✓' if analysis['user_info']['verified'] else '✗'}</p>
            </div>

            <div class="section">
                <h2>😊 Sentiment Analysis</h2>
                <p class="positive">Positive: {analysis['sentiment']['positive_percent']:.1f}%</p>
                <p class="negative">Negative: {analysis['sentiment']['negative_percent']:.1f}%</p>
            </div>

            <div class="section">
                <h2>🏷️ Extracted Entities</h2>
                <h3>Organizations</h3>
                <p>{', '.join(analysis['entities']['ORG'][:10])}</p>
                <h3>People</h3>
                <p>{', '.join(analysis['entities']['PERSON'][:10])}</p>
                <h3>Locations</h3>
                <p>{', '.join(analysis['entities']['GPE'][:10])}</p>
            </div>

            <div class="section">
                <h2>📊 Top Topics</h2>
                <table>
                    <tr><th>Topic</th><th>Frequency</th></tr>
                    {"".join([f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in list(analysis['topics'].items())[:10]])}
                </table>
            </div>

            <div class="section">
                <h2>🔗 Network Analysis</h2>
                <h3>Top Mentioned Users</h3>
                <table>
                    <tr><th>User</th><th>Count</th></tr>
                    {"".join([f"<tr><td>@{k}</td><td>{v}</td></tr>" for k, v in list(analysis['network']['top_mentioned'].items())[:10]])}
                </table>
            </div>

            <p><small>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</small></p>
        </body>
        </html>
        """

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"[+] Report saved to {output_file}")

# Usage example
if __name__ == "__main__":
    # Twitter API credentials (get from developer.twitter.com)
    API_KEY = "YOUR_API_KEY"
    API_SECRET = "YOUR_API_SECRET"
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
    ACCESS_SECRET = "YOUR_ACCESS_SECRET"

    # Initialize
    osint = AITwitterOSINT(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

    # Analyze user
    target_user = "elonmusk"  # Example
    analysis = osint.analyze_user(target_user, tweet_count=200)

    # Generate report
    osint.generate_report(analysis, f"osint_{target_user}.html")

    print(f"\n[+] Analysis complete!")
    print(f"  Positive sentiment: {analysis['sentiment']['positive_percent']:.1f}%")
    print(f"  Organizations mentioned: {len(analysis['entities']['ORG'])}")
    print(f"  Top mentioned users: {list(analysis['network']['top_mentioned'].keys())[:5]}")
```

### 🔍 Image Recognition OSINT

**Använd AI för att analysera bilder:**

```python
#!/usr/bin/env python3
"""
Image OSINT using Computer Vision
- Face detection
- Object recognition
- Text extraction (OCR)
- Reverse image search
- EXIF data extraction
"""

from PIL import Image
import pytesseract
from PIL.ExifTags import TAGS
import face_recognition
import cv2
import numpy as np
from transformers import pipeline
import requests
from io import BytesIO

class ImageOSINT:
    def __init__(self):
        """Initialize image analysis tools"""
        self.image_classifier = pipeline("image-classification")
        print("[+] Image OSINT initialized")

    def analyze_image(self, image_path):
        """Complete image analysis"""

        print(f"[*] Analyzing {image_path}...")

        analysis = {
            'exif': self.extract_exif(image_path),
            'faces': self.detect_faces(image_path),
            'text': self.extract_text(image_path),
            'objects': self.classify_image(image_path),
            'metadata': self.get_metadata(image_path)
        }

        return analysis

    def extract_exif(self, image_path):
        """Extract EXIF metadata"""

        image = Image.open(image_path)
        exif_data = {}

        try:
            exif = image._getexif()
            if exif:
                for tag_id, value in exif.items():
                    tag = TAGS.get(tag_id, tag_id)
                    exif_data[tag] = str(value)
        except:
            pass

        # Extract important fields
        result = {
            'GPS': exif_data.get('GPSInfo', 'Not available'),
            'DateTime': exif_data.get('DateTime', 'Not available'),
            'Make': exif_data.get('Make', 'Not available'),
            'Model': exif_data.get('Model', 'Not available'),
            'Software': exif_data.get('Software', 'Not available'),
            'all_data': exif_data
        }

        return result

    def detect_faces(self, image_path):
        """Detect faces in image"""

        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        return {
            'face_count': len(face_locations),
            'locations': face_locations,
            'encodings': [encoding.tolist() for encoding in face_encodings]
        }

    def extract_text(self, image_path):
        """OCR - Extract text from image"""

        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)

        return {
            'text': text.strip(),
            'length': len(text.strip())
        }

    def classify_image(self, image_path):
        """Classify image content using AI"""

        image = Image.open(image_path)
        classifications = self.image_classifier(image)

        return classifications[:5]  # Top 5 classifications

    def get_metadata(self, image_path):
        """Get file metadata"""

        import os
        from datetime import datetime

        stats = os.stat(image_path)

        return {
            'file_size': stats.st_size,
            'created': datetime.fromtimestamp(stats.st_ctime).isoformat(),
            'modified': datetime.fromtimestamp(stats.st_mtime).isoformat(),
        }

    def reverse_image_search_url(self, image_path):
        """Generate reverse image search URLs"""

        # Note: Actual reverse image search requires uploading
        # These are the URLs you would visit manually

        return {
            'google': 'https://images.google.com/searchbyimage',
            'yandex': 'https://yandex.com/images/search?rpt=imageview',
            'tineye': 'https://tineye.com/',
            'bing': 'https://www.bing.com/images/search?view=detailv2&iss=sbi'
        }

    def generate_report(self, analysis, output_file='image_osint.txt'):
        """Generate text report"""

        report = f"""
╔══════════════════════════════════════════════════════════════╗
║              IMAGE OSINT ANALYSIS REPORT                     ║
╚══════════════════════════════════════════════════════════════╝

📸 METADATA
─────────────────────────────────────────────────────────────
File Size: {analysis['metadata']['file_size']:,} bytes
Created: {analysis['metadata']['created']}
Modified: {analysis['metadata']['modified']}

📷 EXIF DATA
─────────────────────────────────────────────────────────────
GPS: {analysis['exif']['GPS']}
DateTime: {analysis['exif']['DateTime']}
Camera Make: {analysis['exif']['Make']}
Camera Model: {analysis['exif']['Model']}
Software: {analysis['exif']['Software']}

👥 FACE DETECTION
─────────────────────────────────────────────────────────────
Faces Detected: {analysis['faces']['face_count']}
Locations: {analysis['faces']['locations']}

📝 TEXT EXTRACTION (OCR)
─────────────────────────────────────────────────────────────
{analysis['text']['text']}

🏷️ IMAGE CLASSIFICATION
─────────────────────────────────────────────────────────────
"""
        for idx, obj in enumerate(analysis['objects'], 1):
            report += f"{idx}. {obj['label']}: {obj['score']*100:.1f}%\n"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)

        print(f"[+] Report saved to {output_file}")
        return report

# Usage
if __name__ == "__main__":
    osint = ImageOSINT()

    # Analyze image
    analysis = osint.analyze_image("target_image.jpg")

    # Generate report
    report = osint.generate_report(analysis)
    print(report)

    # Print reverse search URLs
    print("\n🔍 Reverse Image Search:")
    urls = osint.reverse_image_search_url("target_image.jpg")
    for engine, url in urls.items():
        print(f"  {engine}: {url}")
```

---

## ☁️ Del 2: Cloud Security Testing

### 🎯 AWS Security Assessment

#### AWS CLI Setup och Reconnaissance

```bash
# Installation
pip install awscli boto3

# Konfigurera (kräver AWS credentials)
aws configure

# Basic reconnaissance
aws sts get-caller-identity  # Vem är jag?
aws iam list-users            # Lista användare
aws ec2 describe-instances    # Lista EC2 instances
aws s3 ls                     # Lista S3 buckets
aws lambda list-functions     # Lista Lambda functions
```

#### ScoutSuite - AWS Security Audit Tool

```bash
# Installation
pip install scoutsuite

# Kör full AWS audit
scout aws

# Output: HTML-rapport med alla misconfigurations!
# Öppna: scoutsuite-report/aws.html

# Exempel findings:
# - Public S3 buckets
# - Overly permissive IAM policies
# - Security groups allowing 0.0.0.0/0
# - Unencrypted EBS volumes
# - Missing MFA on root account
```

#### Prowler - AWS CIS Benchmark

```bash
# Installation
git clone https://github.com/prowler-cloud/prowler
cd prowler

# Kör full assessment
./prowler -M html

# Output: Detailed compliance report

# Custom checks
./prowler -c check21  # S3 bucket encryption
./prowler -c check22  # RDS encryption
./prowler -g group1   # Identity and Access Management
```

#### Python Script: AWS S3 Bucket Enumeration

```python
#!/usr/bin/env python3
"""
AWS S3 Bucket Security Scanner
Finds public buckets and checks permissions
"""

import boto3
from botocore.exceptions import ClientError
import concurrent.futures

class S3SecurityScanner:
    def __init__(self):
        self.s3_client = boto3.client('s3')
        self.s3_resource = boto3.resource('s3')

    def list_all_buckets(self):
        """List all S3 buckets in account"""
        response = self.s3_client.list_buckets()
        return [bucket['Name'] for bucket in response['Buckets']]

    def check_bucket_public_access(self, bucket_name):
        """Check if bucket is publicly accessible"""

        try:
            # Check bucket ACL
            acl = self.s3_client.get_bucket_acl(Bucket=bucket_name)

            is_public = False
            for grant in acl['Grants']:
                grantee = grant.get('Grantee', {})
                if grantee.get('Type') == 'Group':
                    uri = grantee.get('URI', '')
                    if 'AllUsers' in uri or 'AuthenticatedUsers' in uri:
                        is_public = True
                        break

            # Check bucket policy
            try:
                policy = self.s3_client.get_bucket_policy(Bucket=bucket_name)
                # Simplified check - real implementation would parse JSON
                if '"Principal":"*"' in policy['Policy'] or '"Principal":{"AWS":"*"}' in policy['Policy']:
                    is_public = True
            except ClientError as e:
                if e.response['Error']['Code'] != 'NoSuchBucketPolicy':
                    raise

            # Check public access block
            try:
                block = self.s3_client.get_public_access_block(Bucket=bucket_name)
                config = block['PublicAccessBlockConfiguration']

                all_blocked = (
                    config['BlockPublicAcls'] and
                    config['IgnorePublicAcls'] and
                    config['BlockPublicPolicy'] and
                    config['RestrictPublicBuckets']
                )

                if all_blocked:
                    is_public = False
            except ClientError:
                pass

            return is_public

        except ClientError as e:
            print(f"[!] Error checking {bucket_name}: {e}")
            return False

    def check_bucket_encryption(self, bucket_name):
        """Check if bucket has encryption enabled"""

        try:
            encryption = self.s3_client.get_bucket_encryption(Bucket=bucket_name)
            return True
        except ClientError as e:
            if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
                return False
            raise

    def check_bucket_versioning(self, bucket_name):
        """Check if versioning is enabled"""

        try:
            versioning = self.s3_client.get_bucket_versioning(Bucket=bucket_name)
            return versioning.get('Status') == 'Enabled'
        except ClientError:
            return False

    def check_bucket_logging(self, bucket_name):
        """Check if logging is enabled"""

        try:
            logging = self.s3_client.get_bucket_logging(Bucket=bucket_name)
            return 'LoggingEnabled' in logging
        except ClientError:
            return False

    def scan_bucket(self, bucket_name):
        """Complete security scan of a bucket"""

        print(f"[*] Scanning {bucket_name}...")

        return {
            'name': bucket_name,
            'is_public': self.check_bucket_public_access(bucket_name),
            'encrypted': self.check_bucket_encryption(bucket_name),
            'versioning': self.check_bucket_versioning(bucket_name),
            'logging': self.check_bucket_logging(bucket_name)
        }

    def scan_all_buckets(self):
        """Scan all buckets in parallel"""

        buckets = self.list_all_buckets()
        print(f"[*] Found {len(buckets)} buckets")

        results = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            future_to_bucket = {executor.submit(self.scan_bucket, bucket): bucket for bucket in buckets}

            for future in concurrent.futures.as_completed(future_to_bucket):
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    print(f"[!] Error: {e}")

        return results

    def generate_report(self, results):
        """Generate security report"""

        print("\n" + "="*70)
        print(" "*20 + "S3 SECURITY SCAN REPORT")
        print("="*70)

        public_buckets = [r for r in results if r['is_public']]
        unencrypted = [r for r in results if not r['encrypted']]
        no_versioning = [r for r in results if not r['versioning']]
        no_logging = [r for r in results if not r['logging']]

        print(f"\n📊 SUMMARY")
        print(f"─" * 70)
        print(f"Total buckets: {len(results)}")
        print(f"🔴 Public buckets: {len(public_buckets)}")
        print(f"🟡 Unencrypted buckets: {len(unencrypted)}")
        print(f"🟡 No versioning: {len(no_versioning)}")
        print(f"🟡 No logging: {len(no_logging)}")

        if public_buckets:
            print(f"\n🚨 PUBLIC BUCKETS (HIGH RISK!)")
            print(f"─" * 70)
            for bucket in public_buckets:
                print(f"  - {bucket['name']}")

        if unencrypted:
            print(f"\n⚠️  UNENCRYPTED BUCKETS")
            print(f"─" * 70)
            for bucket in unencrypted:
                print(f"  - {bucket['name']}")

        print(f"\n✅ RECOMMENDATIONS")
        print(f"─" * 70)
        print("1. Enable encryption on all buckets")
        print("2. Block public access unless explicitly required")
        print("3. Enable versioning for data protection")
        print("4. Enable logging for audit trails")
        print("5. Implement least-privilege IAM policies")

# Usage
if __name__ == "__main__":
    scanner = S3SecurityScanner()
    results = scanner.scan_all_buckets()
    scanner.generate_report(results)
```

### ☁️ Azure Security Testing

```python
#!/usr/bin/env python3
"""
Azure Security Scanner
"""

from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
import os

class AzureSecurityScanner:
    def __init__(self, subscription_id):
        self.subscription_id = subscription_id
        self.credential = DefaultAzureCredential()

        self.storage_client = StorageManagementClient(self.credential, subscription_id)
        self.compute_client = ComputeManagementClient(self.credential, subscription_id)
        self.network_client = NetworkManagementClient(self.credential, subscription_id)

    def check_storage_accounts(self):
        """Check storage account security"""

        findings = []

        for account in self.storage_client.storage_accounts.list():
            issues = []

            # Check HTTPS only
            if not account.enable_https_traffic_only:
                issues.append("HTTPS not enforced")

            # Check encryption
            if not account.encryption.services.blob.enabled:
                issues.append("Blob encryption disabled")

            # Check public access
            if account.allow_blob_public_access:
                issues.append("Public blob access allowed")

            if issues:
                findings.append({
                    'resource': account.name,
                    'type': 'Storage Account',
                    'issues': issues
                })

        return findings

    def check_network_security_groups(self):
        """Check NSG rules for overly permissive access"""

        findings = []

        for nsg in self.network_client.network_security_groups.list_all():
            for rule in nsg.security_rules:
                # Check for 0.0.0.0/0 or * in source
                if rule.source_address_prefix in ['*', '0.0.0.0/0', 'Internet']:
                    if rule.access == 'Allow':
                        findings.append({
                            'resource': nsg.name,
                            'type': 'NSG',
                            'issues': [f"Rule '{rule.name}' allows traffic from Internet on port {rule.destination_port_range}"]
                        })

        return findings

    def check_virtual_machines(self):
        """Check VM security configurations"""

        findings = []

        for vm in self.compute_client.virtual_machines.list_all():
            issues = []

            # Check if managed disks are encrypted
            if vm.storage_profile.os_disk.encryption_settings is None:
                issues.append("OS disk not encrypted")

            if issues:
                findings.append({
                    'resource': vm.name,
                    'type': 'Virtual Machine',
                    'issues': issues
                })

        return findings

# Usage
# scanner = AzureSecurityScanner("your-subscription-id")
# findings = scanner.check_storage_accounts()
```

---

## 🐳 Del 3: Container Security (Docker & Kubernetes)

### 🔍 Docker Security Scanning

#### Trivy - Container Vulnerability Scanner

```bash
# Installation
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo "deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/trivy.list
sudo apt update
sudo apt install trivy

# Scan Docker image
trivy image nginx:latest

# Output:
# ┌──────────────────┬────────────────┬──────────┬───────────────────┬
# │     Library      │ Vulnerability  │ Severity │  Installed Ver.   │
# ├──────────────────┼────────────────┼──────────┼───────────────────┼
# │ openssl          │ CVE-2021-3711  │ HIGH     │ 1.1.1k-1          │
# │ curl             │ CVE-2021-22947 │ MEDIUM   │ 7.74.0-1          │
# └──────────────────┴────────────────┴──────────┴───────────────────┴

# Scan local filesystem
trivy fs /path/to/project

# CI/CD integration
trivy image --exit-code 1 --severity HIGH,CRITICAL myimage:tag
# Exit code 1 if HIGH or CRITICAL vulns found
```

#### Docker Bench Security

```bash
# Installation
git clone https://github.com/docker/docker-bench-security.git
cd docker-bench-security

# Run
sudo sh docker-bench-security.sh

# Output: CIS Docker Benchmark compliance report
# [PASS] 1.1.1 Ensure a separate partition for containers
# [WARN] 1.2.1 Ensure Docker daemon is audited
# [FAIL] 4.1 Ensure a user for the container has been created
```

#### Custom Docker Security Scanner

```python
#!/usr/bin/env python3
"""
Docker Security Scanner
Checks running containers for security issues
"""

import docker
import json

class DockerSecurityScanner:
    def __init__(self):
        self.client = docker.from_env()

    def scan_container(self, container):
        """Security scan of a container"""

        issues = []

        # Check if running as root
        if container.attrs['Config']['User'] == '' or container.attrs['Config']['User'] == 'root':
            issues.append("Container running as root")

        # Check for privileged mode
        if container.attrs['HostConfig']['Privileged']:
            issues.append("Container running in privileged mode (CRITICAL!)")

        # Check for host network mode
        if container.attrs['HostConfig']['NetworkMode'] == 'host':
            issues.append("Container using host network mode")

        # Check for volume mounts
        mounts = container.attrs['Mounts']
        for mount in mounts:
            if mount['Type'] == 'bind':
                if mount['Source'] == '/' or mount['Source'].startswith('/etc'):
                    issues.append(f"Dangerous bind mount: {mount['Source']}")

        # Check capabilities
        cap_add = container.attrs['HostConfig'].get('CapAdd', [])
        dangerous_caps = ['SYS_ADMIN', 'NET_ADMIN', 'SYS_MODULE']
        for cap in cap_add:
            if cap in dangerous_caps:
                issues.append(f"Dangerous capability: {cap}")

        return {
            'name': container.name,
            'image': container.image.tags[0] if container.image.tags else 'unknown',
            'id': container.short_id,
            'status': container.status,
            'issues': issues,
            'risk_level': self._calculate_risk(issues)
        }

    def _calculate_risk(self, issues):
        """Calculate risk level based on issues"""
        if any('privileged' in issue.lower() or 'CRITICAL' in issue for issue in issues):
            return 'CRITICAL'
        elif len(issues) >= 3:
            return 'HIGH'
        elif len(issues) > 0:
            return 'MEDIUM'
        else:
            return 'LOW'

    def scan_all_containers(self):
        """Scan all running containers"""

        containers = self.client.containers.list()
        results = []

        for container in containers:
            result = self.scan_container(container)
            results.append(result)

        return results

    def generate_report(self, results):
        """Generate security report"""

        print("\n" + "="*70)
        print(" "*15 + "DOCKER SECURITY SCAN REPORT")
        print("="*70)

        # Group by risk level
        critical = [r for r in results if r['risk_level'] == 'CRITICAL']
        high = [r for r in results if r['risk_level'] == 'HIGH']
        medium = [r for r in results if r['risk_level'] == 'MEDIUM']
        low = [r for r in results if r['risk_level'] == 'LOW']

        print(f"\n📊 SUMMARY")
        print(f"─" * 70)
        print(f"Total containers scanned: {len(results)}")
        print(f"🔴 Critical: {len(critical)}")
        print(f"🟠 High: {len(high)}")
        print(f"🟡 Medium: {len(medium)}")
        print(f"🟢 Low: {len(low)}")

        for result in results:
            if result['issues']:
                print(f"\n{'🔴' if result['risk_level'] == 'CRITICAL' else '🟡'} {result['name']} ({result['image']})")
                print(f"  Risk Level: {result['risk_level']}")
                print(f"  Issues:")
                for issue in result['issues']:
                    print(f"    - {issue}")

# Usage
if __name__ == "__main__":
    scanner = DockerSecurityScanner()
    results = scanner.scan_all_containers()
    scanner.generate_report(results)
```

### ☸️ Kubernetes Security

#### kube-bench - K8s CIS Benchmark

```bash
# Installation
kubectl apply -f https://raw.githubusercontent.com/aquasecurity/kube-bench/main/job.yaml

# View results
kubectl logs -f job/kube-bench

# Manual installation
curl -L https://github.com/aquasecurity/kube-bench/releases/download/v0.6.8/kube-bench_0.6.8_linux_amd64.tar.gz -o kube-bench.tar.gz
tar -xvf kube-bench.tar.gz
sudo mv kube-bench /usr/local/bin/

# Run
kube-bench run --targets master,node
```

#### kubesec - K8s Security Risk Analysis

```bash
# Installation
wget https://github.com/controlplaneio/kubesec/releases/download/v2.11.0/kubesec_linux_amd64.tar.gz
tar -xvf kubesec_linux_amd64.tar.gz
sudo mv kubesec /usr/local/bin/

# Scan Kubernetes manifest
kubesec scan pod.yaml

# Example output:
{
  "score": -30,
  "scoring": {
    "critical": [
      {
        "selector": "containers[] .securityContext .privileged == true",
        "reason": "Privileged container"
      }
    ],
    "advise": [
      {
        "selector": ".spec .serviceAccountName",
        "reason": "Service account not specified"
      }
    ]
  }
}
```

---

## 🔄 Del 4: DevSecOps - CI/CD Security Integration

### 🎯 ZAP i CI/CD Pipeline

#### GitHub Actions Workflow

```yaml
# .github/workflows/security-scan.yml
name: Security Scan

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '0 2 * * 1'  # Varje måndag kl 02:00

jobs:
  zap-scan:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Start application
        run: |
          docker-compose up -d
          sleep 30  # Vänta på att appen startar

      - name: ZAP Baseline Scan
        uses: zaproxy/action-baseline@v0.7.0
        with:
          target: 'http://localhost:3000'
          rules_file_name: '.zap/rules.tsv'
          cmd_options: '-a'

      - name: ZAP Full Scan
        uses: zaproxy/action-full-scan@v0.4.0
        with:
          target: 'http://localhost:3000'
          allow_issue_writing: true
          issue_title: 'ZAP Full Scan Report'
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Upload ZAP Report
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: zap-report
          path: |
            zap_report.html
            zap_report.md

      - name: Fail on HIGH vulnerabilities
        run: |
          if grep -q "High" zap_report.md; then
            echo "HIGH severity vulnerabilities found!"
            exit 1
          fi

  dependency-check:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Run OWASP Dependency Check
        uses: dependency-check/Dependency-Check_Action@main
        with:
          project: 'my-project'
          path: '.'
          format: 'HTML'

      - name: Upload Dependency Check report
        uses: actions/upload-artifact@v3
        with:
          name: dependency-check-report
          path: reports

  container-scan:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Build Docker image
        run: docker build -t myapp:${{ github.sha }} .

      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: 'myapp:${{ github.sha }}'
          format: 'sarif'
          output: 'trivy-results.sarif'
          severity: 'CRITICAL,HIGH'

      - name: Upload Trivy results to GitHub Security
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'trivy-results.sarif'

  sast-scan:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Run Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: >-
            p/owasp-top-ten
            p/security-audit

      - name: Run Bandit (Python)
        run: |
          pip install bandit
          bandit -r . -f json -o bandit-report.json
        continue-on-error: true

      - name: Upload SAST reports
        uses: actions/upload-artifact@v3
        with:
          name: sast-reports
          path: |
            bandit-report.json
```

#### GitLab CI/CD Pipeline

```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - security
  - deploy

build:
  stage: build
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

sast:
  stage: security
  image: returntocorp/semgrep
  script:
    - semgrep --config=auto --json -o semgrep-report.json .
  artifacts:
    reports:
      sast: semgrep-report.json

dependency_scanning:
  stage: security
  image: owasp/dependency-check
  script:
    - /usr/share/dependency-check/bin/dependency-check.sh
      --scan .
      --format JSON
      --out dependency-check-report.json
  artifacts:
    paths:
      - dependency-check-report.json

container_scanning:
  stage: security
  image: aquasec/trivy
  script:
    - trivy image --exit-code 0 --no-progress --format json -o container-scan.json $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  artifacts:
    paths:
      - container-scan.json

zap_scan:
  stage: security
  image: owasp/zap2docker-stable
  script:
    - mkdir /zap/wrk
    - /zap/zap-baseline.py -t https://staging.myapp.com -r zap-report.html
  artifacts:
    paths:
      - zap-report.html
  allow_failure: true

deploy:
  stage: deploy
  script:
    - kubectl set image deployment/myapp myapp=$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  only:
    - main
```

### 🐍 Custom Security Scanner Integration

```python
#!/usr/bin/env python3
"""
Custom CI/CD Security Scanner
Integrates multiple security tools
"""

import subprocess
import json
import sys
from pathlib import Path

class CICDSecurityScanner:
    def __init__(self, project_path='.'):
        self.project_path = Path(project_path)
        self.results = {
            'sast': [],
            'dependency': [],
            'container': [],
            'secrets': [],
            'dast': []
        }

    def run_bandit(self):
        """Python SAST with Bandit"""
        print("[*] Running Bandit (Python SAST)...")

        try:
            result = subprocess.run(
                ['bandit', '-r', str(self.project_path), '-f', 'json'],
                capture_output=True,
                text=True
            )

            if result.stdout:
                data = json.loads(result.stdout)
                self.results['sast'].extend(data.get('results', []))
                print(f"  Found {len(data.get('results', []))} issues")
        except Exception as e:
            print(f"  [!] Error: {e}")

    def run_semgrep(self):
        """Multi-language SAST with Semgrep"""
        print("[*] Running Semgrep...")

        try:
            result = subprocess.run(
                ['semgrep', '--config=auto', '--json', str(self.project_path)],
                capture_output=True,
                text=True
            )

            if result.stdout:
                data = json.loads(result.stdout)
                self.results['sast'].extend(data.get('results', []))
                print(f"  Found {len(data.get('results', []))} issues")
        except Exception as e:
            print(f"  [!] Error: {e}")

    def run_safety(self):
        """Python dependency check with Safety"""
        print("[*] Running Safety (Python dependencies)...")

        try:
            result = subprocess.run(
                ['safety', 'check', '--json'],
                capture_output=True,
                text=True
            )

            if result.stdout:
                data = json.loads(result.stdout)
                self.results['dependency'].extend(data)
                print(f"  Found {len(data)} vulnerable dependencies")
        except Exception as e:
            print(f"  [!] Error: {e}")

    def run_trivy_fs(self):
        """Filesystem vulnerability scan with Trivy"""
        print("[*] Running Trivy (filesystem scan)...")

        try:
            result = subprocess.run(
                ['trivy', 'fs', '--format', 'json', str(self.project_path)],
                capture_output=True,
                text=True
            )

            if result.stdout:
                data = json.loads(result.stdout)
                if 'Results' in data:
                    for res in data['Results']:
                        self.results['dependency'].extend(res.get('Vulnerabilities', []))
                print(f"  Scan complete")
        except Exception as e:
            print(f"  [!] Error: {e}")

    def run_gitleaks(self):
        """Secret scanning with Gitleaks"""
        print("[*] Running Gitleaks (secret detection)...")

        try:
            result = subprocess.run(
                ['gitleaks', 'detect', '--report-format', 'json', '--report-path', 'gitleaks-report.json'],
                capture_output=True,
                text=True,
                cwd=str(self.project_path)
            )

            try:
                with open(self.project_path / 'gitleaks-report.json') as f:
                    data = json.load(f)
                    self.results['secrets'].extend(data)
                    print(f"  Found {len(data)} potential secrets")
            except:
                print(f"  No secrets found")
        except Exception as e:
            print(f"  [!] Error: {e}")

    def run_zap_baseline(self, target_url):
        """DAST with ZAP baseline scan"""
        print(f"[*] Running ZAP baseline scan on {target_url}...")

        try:
            result = subprocess.run(
                ['docker', 'run', '--rm',
                 '-v', f'{Path.cwd()}:/zap/wrk:rw',
                 'owasp/zap2docker-stable',
                 'zap-baseline.py',
                 '-t', target_url,
                 '-J', 'zap-report.json'],
                capture_output=True,
                text=True
            )

            try:
                with open('zap-report.json') as f:
                    data = json.load(f)
                    self.results['dast'] = data.get('site', [{}])[0].get('alerts', [])
                    print(f"  Found {len(self.results['dast'])} issues")
            except:
                print(f"  Scan complete (check zap-report.json)")
        except Exception as e:
            print(f"  [!] Error: {e}")

    def generate_report(self):
        """Generate comprehensive security report"""

        print("\n" + "="*70)
        print(" "*15 + "CI/CD SECURITY SCAN REPORT")
        print("="*70)

        total_issues = (
            len(self.results['sast']) +
            len(self.results['dependency']) +
            len(self.results['secrets']) +
            len(self.results['dast'])
        )

        print(f"\n📊 SUMMARY")
        print(f"─" * 70)
        print(f"Total issues found: {total_issues}")
        print(f"  SAST (Code): {len(self.results['sast'])}")
        print(f"  Dependencies: {len(self.results['dependency'])}")
        print(f"  Secrets: {len(self.results['secrets'])}")
        print(f"  DAST (Runtime): {len(self.results['dast'])}")

        # Critical/High issues
        critical_count = 0
        high_count = 0

        # Count SAST severity
        for issue in self.results['sast']:
            severity = issue.get('issue_severity', issue.get('extra', {}).get('severity', '')).upper()
            if severity in ['CRITICAL', 'ERROR']:
                critical_count += 1
            elif severity == 'HIGH':
                high_count += 1

        # Count dependency severity
        for issue in self.results['dependency']:
            severity = issue.get('Severity', '').upper()
            if severity == 'CRITICAL':
                critical_count += 1
            elif severity == 'HIGH':
                high_count += 1

        # Count DAST severity
        for issue in self.results['dast']:
            risk = issue.get('riskdesc', '').upper()
            if 'HIGH' in risk:
                high_count += 1

        print(f"\n🚨 SEVERITY BREAKDOWN")
        print(f"─" * 70)
        print(f"🔴 Critical: {critical_count}")
        print(f"🟠 High: {high_count}")

        if critical_count > 0:
            print(f"\n❌ BUILD FAILED - Critical vulnerabilities found!")
            return 1
        elif high_count > 5:
            print(f"\n⚠️  BUILD WARNING - Multiple high severity issues")
            return 0  # Or 1 if you want to fail
        else:
            print(f"\n✅ BUILD PASSED - No critical issues")
            return 0

    def run_all_scans(self, target_url=None):
        """Run all security scans"""

        print("\n🔒 Starting CI/CD Security Scan Pipeline...")
        print("="*70 + "\n")

        # SAST
        self.run_bandit()
        self.run_semgrep()

        # Dependency scanning
        self.run_safety()
        self.run_trivy_fs()

        # Secret detection
        self.run_gitleaks()

        # DAST (if target provided)
        if target_url:
            self.run_zap_baseline(target_url)

        # Generate report and return exit code
        return self.generate_report()

# Usage
if __name__ == "__main__":
    scanner = CICDSecurityScanner('.')

    # Optional: DAST target URL
    target_url = sys.argv[1] if len(sys.argv) > 1 else None

    exit_code = scanner.run_all_scans(target_url)
    sys.exit(exit_code)
```

---

## 🎯 Del 5: Modern API Security Testing

### GraphQL Security Testing

```python
#!/usr/bin/env python3
"""
GraphQL Security Scanner
Tests for common GraphQL vulnerabilities
"""

import requests
import json

class GraphQLSecurityScanner:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.findings = []

    def check_introspection(self):
        """Check if introspection is enabled (info disclosure)"""

        query = """
        {
            __schema {
                types {
                    name
                    fields {
                        name
                    }
                }
            }
        }
        """

        try:
            response = requests.post(
                self.endpoint,
                json={'query': query},
                headers={'Content-Type': 'application/json'}
            )

            if response.status_code == 200 and '__schema' in response.text:
                self.findings.append({
                    'severity': 'MEDIUM',
                    'title': 'Introspection Enabled',
                    'description': 'GraphQL introspection is enabled, exposing entire schema',
                    'recommendation': 'Disable introspection in production'
                })
                return True
        except Exception as e:
            print(f"[!] Error: {e}")

        return False

    def check_depth_limit(self):
        """Test for query depth limit (DoS protection)"""

        # Create deeply nested query
        query = "{ "
        for i in range(50):
            query += "user { friends { "
        query += "name "
        for i in range(50):
            query += "} } "
        query += "}"

        try:
            response = requests.post(
                self.endpoint,
                json={'query': query},
                timeout=10
            )

            if response.status_code == 200:
                self.findings.append({
                    'severity': 'HIGH',
                    'title': 'No Query Depth Limit',
                    'description': 'Server accepts deeply nested queries, vulnerable to DoS',
                    'recommendation': 'Implement query depth limiting'
                })
        except requests.Timeout:
            self.findings.append({
                'severity': 'HIGH',
                'title': 'Query Timeout on Deep Nesting',
                'description': 'Deep query caused timeout, potential DoS vector',
                'recommendation': 'Implement query depth limiting'
            })
        except Exception as e:
            pass

    def check_batch_limit(self):
        """Test for batch query limit"""

        # Try to send 100 queries at once
        batch = [{'query': '{ __typename }'} for _ in range(100)]

        try:
            response = requests.post(
                self.endpoint,
                json=batch,
                timeout=10
            )

            if response.status_code == 200:
                self.findings.append({
                    'severity': 'MEDIUM',
                    'title': 'No Batch Query Limit',
                    'description': 'Server accepts large batch queries, potential DoS',
                    'recommendation': 'Implement batch query limiting'
                })
        except Exception as e:
            pass

    def check_field_suggestions(self):
        """Check if error messages reveal field suggestions"""

        query = "{ nonExistentField }"

        try:
            response = requests.post(
                self.endpoint,
                json={'query': query}
            )

            if 'did you mean' in response.text.lower():
                self.findings.append({
                    'severity': 'LOW',
                    'title': 'Field Suggestions in Errors',
                    'description': 'Error messages suggest valid field names',
                    'recommendation': 'Disable field suggestions in production'
                })
        except Exception as e:
            pass

    def test_injection(self):
        """Test for injection vulnerabilities"""

        payloads = [
            "' OR '1'='1",
            "'; DROP TABLE users--",
            "<script>alert('XSS')</script>",
            "${7*7}",
            "{{7*7}}"
        ]

        query_template = """
        {
            user(id: "%s") {
                name
            }
        }
        """

        for payload in payloads:
            try:
                query = query_template % payload
                response = requests.post(
                    self.endpoint,
                    json={'query': query}
                )

                # Check for signs of injection
                if '49' in response.text or 'error' not in response.text.lower():
                    self.findings.append({
                        'severity': 'CRITICAL',
                        'title': 'Potential Injection Vulnerability',
                        'description': f'Payload "{payload}" may have been executed',
                        'recommendation': 'Implement proper input validation and parameterization'
                    })
            except Exception as e:
                pass

    def generate_report(self):
        """Generate security report"""

        print("\n" + "="*70)
        print(" "*15 + "GRAPHQL SECURITY SCAN REPORT")
        print("="*70)

        if not self.findings:
            print("\n✅ No vulnerabilities found!")
            return

        # Group by severity
        critical = [f for f in self.findings if f['severity'] == 'CRITICAL']
        high = [f for f in self.findings if f['severity'] == 'HIGH']
        medium = [f for f in self.findings if f['severity'] == 'MEDIUM']
        low = [f for f in self.findings if f['severity'] == 'LOW']

        print(f"\n📊 SUMMARY")
        print(f"─" * 70)
        print(f"🔴 Critical: {len(critical)}")
        print(f"🟠 High: {len(high)}")
        print(f"🟡 Medium: {len(medium)}")
        print(f"🟢 Low: {len(low)}")

        print(f"\n🔍 FINDINGS")
        print(f"─" * 70)

        for finding in self.findings:
            emoji = {'CRITICAL': '🔴', 'HIGH': '🟠', 'MEDIUM': '🟡', 'LOW': '🟢'}
            print(f"\n{emoji[finding['severity']]} {finding['title']}")
            print(f"  Severity: {finding['severity']}")
            print(f"  Description: {finding['description']}")
            print(f"  Recommendation: {finding['recommendation']}")

    def run_all_tests(self):
        """Run all security tests"""

        print(f"[*] Scanning GraphQL endpoint: {self.endpoint}")

        self.check_introspection()
        self.check_depth_limit()
        self.check_batch_limit()
        self.check_field_suggestions()
        self.test_injection()

        self.generate_report()

# Usage
if __name__ == "__main__":
    scanner = GraphQLSecurityScanner("https://api.example.com/graphql")
    scanner.run_all_tests()
```

### REST API Security Fuzzer

```python
#!/usr/bin/env python3
"""
Advanced REST API Security Fuzzer
"""

import requests
import json
from urllib.parse import urljoin

class APISecurityFuzzer:
    def __init__(self, base_url):
        self.base_url = base_url
        self.findings = []

    def fuzz_authentication(self, endpoint):
        """Test authentication bypass"""

        headers_list = [
            {},
            {'X-Forwarded-For': '127.0.0.1'},
            {'X-Original-URL': '/admin'},
            {'X-Rewrite-URL': '/admin'},
            {'Authorization': 'Bearer null'},
            {'Authorization': 'Bearer admin'},
            {'Cookie': 'admin=true'},
        ]

        for headers in headers_list:
            try:
                response = requests.get(urljoin(self.base_url, endpoint), headers=headers)

                if response.status_code == 200:
                    self.findings.append({
                        'severity': 'CRITICAL',
                        'title': 'Authentication Bypass',
                        'endpoint': endpoint,
                        'headers': headers,
                        'description': f'Endpoint accessible with headers: {headers}'
                    })
            except Exception as e:
                pass

    def test_http_methods(self, endpoint):
        """Test for improper HTTP method handling"""

        methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS', 'TRACE']

        results = {}
        for method in methods:
            try:
                response = requests.request(method, urljoin(self.base_url, endpoint))
                results[method] = response.status_code
            except Exception as e:
                results[method] = 'Error'

        # Check for unusual allowed methods
        if results.get('TRACE') == 200:
            self.findings.append({
                'severity': 'MEDIUM',
                'title': 'HTTP TRACE Method Enabled',
                'endpoint': endpoint,
                'description': 'TRACE method is enabled, potential XSS vector'
            })

        if results.get('DELETE') == 200 and 'DELETE' not in endpoint.upper():
            self.findings.append({
                'severity': 'HIGH',
                'title': 'DELETE Method Allowed',
                'endpoint': endpoint,
                'description': 'DELETE method may allow unauthorized data deletion'
            })

    def fuzz_idor(self, endpoint):
        """Test for Insecure Direct Object References"""

        # Try sequential IDs
        for user_id in range(1, 20):
            test_endpoint = endpoint.replace('{id}', str(user_id))

            try:
                response = requests.get(urljoin(self.base_url, test_endpoint))

                if response.status_code == 200:
                    # Check if we can access other users' data
                    if user_id > 1:  # Assuming ID 1 is our user
                        self.findings.append({
                            'severity': 'HIGH',
                            'title': 'Insecure Direct Object Reference (IDOR)',
                            'endpoint': test_endpoint,
                            'description': f'Can access user ID {user_id} without authorization'
                        })
                        break  # Found one, no need to continue
            except Exception as e:
                pass

    def test_rate_limiting(self, endpoint):
        """Test for rate limiting"""

        try:
            # Send 100 requests quickly
            for i in range(100):
                response = requests.get(urljoin(self.base_url, endpoint))

                if i == 99 and response.status_code != 429:
                    self.findings.append({
                        'severity': 'MEDIUM',
                        'title': 'No Rate Limiting',
                        'endpoint': endpoint,
                        'description': 'Endpoint accepts 100+ requests without rate limiting'
                    })
        except Exception as e:
            pass

    def test_mass_assignment(self, endpoint):
        """Test for mass assignment vulnerability"""

        payloads = [
            {'isAdmin': True},
            {'role': 'admin'},
            {'admin': 1},
            {'is_admin': True},
            {'user_role': 'admin'},
        ]

        for payload in payloads:
            try:
                response = requests.post(
                    urljoin(self.base_url, endpoint),
                    json=payload
                )

                if response.status_code in [200, 201]:
                    # Check if admin field was set
                    if 'admin' in response.text.lower() and 'true' in response.text.lower():
                        self.findings.append({
                            'severity': 'CRITICAL',
                            'title': 'Mass Assignment Vulnerability',
                            'endpoint': endpoint,
                            'payload': payload,
                            'description': 'Can set privileged fields through mass assignment'
                        })
            except Exception as e:
                pass

# Usage
# fuzzer = APISecurityFuzzer("https://api.example.com")
# fuzzer.fuzz_authentication("/api/admin")
# fuzzer.test_http_methods("/api/users")
```

---

## 📊 Del 6: Threat Intelligence Integration

### MISP Integration

```python
#!/usr/bin/env python3
"""
MISP (Malware Information Sharing Platform) Integration
Query threat intelligence feeds
"""

from pymisp import PyMISP
import requests

class ThreatIntelligence:
    def __init__(self, misp_url, misp_key):
        self.misp = PyMISP(misp_url, misp_key, False)

    def search_ioc(self, ioc, ioc_type='ip-dst'):
        """Search for Indicator of Compromise"""

        results = self.misp.search(
            controller='attributes',
            type_attribute=ioc_type,
            value=ioc
        )

        return results

    def check_ip_reputation(self, ip_address):
        """Check IP reputation across multiple sources"""

        reputation = {
            'ip': ip_address,
            'misp': self.search_ioc(ip_address, 'ip-dst'),
            'abuseipdb': self._check_abuseipdb(ip_address),
            'virustotal': self._check_virustotal_ip(ip_address)
        }

        return reputation

    def _check_abuseipdb(self, ip):
        """Check AbuseIPDB"""
        # Requires API key
        pass

    def _check_virustotal_ip(self, ip):
        """Check VirusTotal"""
        # Requires API key
        pass
```

---

## 🎯 Övningar - Nivå 5

### Övning 5.1: AI Twitter OSINT 🤖

**Mål:** Använd AI för att analysera en Twitter-användare

```
Target: @elonmusk (eller annan publik profil)

Uppgifter:
1. Kör AI Twitter OSINT-scriptet
2. Analysera sentiment över tid
3. Identifiera top topics
4. Kartlägg nätverk (vem interagerar de med?)
5. Extrahera entities (personer, organisationer, platser)

Dokumentera:
- Dominant sentiment: _______________________
- Top 5 topics: ____________________________
- Top 5 mentioned users: ___________________
- Intressanta patterns: ____________________
```

### Övning 5.2: AWS Security Audit ☁️

**Mål:** Audita AWS-miljö för säkerhetsbrister

```bash
# 1. Installera och kör ScoutSuite
scout aws

# 2. Kör S3 Security Scanner
python3 s3_scanner.py

# 3. Kör Prowler
./prowler -M html

Dokumentera:
─────────────────────────────────────────────
Publika S3 buckets: _______
Okrypterade buckets: _______
IAM-användare utan MFA: _______
Security groups med 0.0.0.0/0: _______
Okrypterade EBS volumes: _______

Kritiska fynd:
1. ________________________________________
2. ________________________________________
3. ________________________________________
```

### Övning 5.3: Docker Security Scan 🐳

**Mål:** Säkerhetsskanna Docker-containers

```bash
# 1. Skanna image med Trivy
trivy image nginx:latest

# 2. Kör Docker Bench Security
sh docker-bench-security.sh

# 3. Kör custom Python scanner
python3 docker_scanner.py

Resultat:
─────────────────────────────────────────────
Sårbarheter funna: _______
Containers som root: _______
Privileged containers: _______
Dangerous mounts: _______

Åtgärder:
1. ________________________________________
2. ________________________________________
```

### Övning 5.4: CI/CD Security Pipeline 🔄

**Mål:** Implementera security scanning i CI/CD

```yaml
Uppgift: Skapa GitHub Actions workflow som:
1. Kör SAST (Semgrep + Bandit)
2. Scannar dependencies (Safety + Trivy)
3. Letar efter secrets (Gitleaks)
4. Kör DAST (ZAP baseline)
5. Genererar säkerhetsrapport

Implementera .github/workflows/security-scan.yml

Testkör och dokumentera:
─────────────────────────────────────────────
SAST issues: _______
Vulnerable dependencies: _______
Secrets found: _______
DAST findings: _______

Build status: PASS / FAIL
```

### Övning 5.5: GraphQL Security Test 🎯

**Mål:** Testa GraphQL API för sårbarheter

```python
# Använd GraphQL Security Scanner

Target: https://api.example.com/graphql

Tester:
□ Introspection enabled?
□ Query depth limit?
□ Batch query limit?
□ Injection vulnerabilities?
□ Field suggestions in errors?

Dokumentera fynd:
─────────────────────────────────────────────
Severity: CRITICAL / HIGH / MEDIUM / LOW
Vulnerabilities:
1. ________________________________________
2. ________________________________________
3. ________________________________________

Recommendations:
________________________________________
________________________________________
```

---

## 🚀 EXPERT-PROJEKT: Full Enterprise Security Assessment

### Scenario

Du har anlitats för att genomföra en komplett säkerhetsbedömning av ett företag:

**Target:** TechCorp AB
- Webbapplikation: https://app.techcorp.se
- API: https://api.techcorp.se
- AWS-infrastruktur
- Docker Kubernetes i produktion
- GitHub repository

### Fas 1: OSINT (2-3 timmar)

```
□ DNS enumeration (alla subdomains)
□ Employee enumeration (LinkedIn, emails)
□ Technology stack discovery
□ Shodan reconnaissance
□ GitHub intelligence
□ SSL certificate transparency
□ AI-driven social media analysis
```

### Fas 2: Infrastructure Assessment (2-3 timmar)

```
□ AWS security audit (ScoutSuite + Prowler)
□ Cloud misconfigurations
□ S3 bucket permissions
□ IAM policy review
□ Network security groups
□ Container security scan
□ Kubernetes CIS benchmark
```

### Fas 3: Application Security (3-4 timmar)

```
□ ZAP spider + active scan
□ GraphQL/REST API testing
□ Authentication testing
□ Authorization bypass attempts
□ OWASP Top 10 testing
□ Business logic testing
```

### Fas 4: Code Security (1-2 timmar)

```
□ SAST (Semgrep, Bandit)
□ Dependency scanning
□ Secret detection
□ Container image scanning
```

### Fas 5: Reporting (2-3 timmar)

Skapa professionell penetration testing rapport:

```markdown
# PENETRATION TESTING REPORT
## TechCorp AB Security Assessment

### EXECUTIVE SUMMARY
[Översikt för ledning - icke-teknisk]

### SCOPE
- Targets tested
- Testing methodology
- Testing dates

### FINDINGS SUMMARY
┌─────────────────────────────────────┐
│ Critical: X                         │
│ High: X                             │
│ Medium: X                           │
│ Low: X                              │
│ Informational: X                    │
└─────────────────────────────────────┘

### DETAILED FINDINGS

#### 1. [CRITICAL] SQL Injection in Login Form
**Severity:** Critical
**CVSS Score:** 9.8
**Affected Component:** https://app.techcorp.se/login

**Description:**
The login form is vulnerable to SQL injection...

**Proof of Concept:**
```sql
username: admin' OR '1'='1'--
password: anything
```

**Impact:**
- Complete database compromise
- User data theft
- Privilege escalation

**Recommendation:**
- Use prepared statements
- Implement input validation
- Apply least privilege to database user

**References:**
- OWASP Top 10: A03:2021 - Injection
- CWE-89: SQL Injection

---

[... Fortsätt för alla vulnerabilities ...]

### CONCLUSION
### RECOMMENDATIONS
### APPENDIX
```

---

## 🎓 Sammanfattning Nivå 5

### Du har nu lärt dig:

✅ **AI-Driven OSINT** - NLP, sentiment analysis, image recognition
✅ **Cloud Security** - AWS, Azure, GCP security testing
✅ **Container Security** - Docker & Kubernetes hardening
✅ **DevSecOps** - CI/CD security integration
✅ **Modern API Security** - GraphQL, REST, gRPC testing
✅ **Threat Intelligence** - MISP, IOC hunting
✅ **Enterprise Assessment** - Full professional pentesting
✅ **Professional Reporting** - Industry-standard documentation

### Du behärskar nu:

🔧 ScoutSuite, Prowler (AWS/Cloud)
🔧 Trivy, Docker Bench (Container)
🔧 Semgrep, Bandit (SAST)
🔧 Custom Python automation tools
🔧 GitHub Actions, GitLab CI security
🔧 GraphQL/API security testing
🔧 AI/ML för OSINT

### Din Expert Toolkit:

```
OSINT EXPERT WORKFLOW
═══════════════════════════════════════════
1. AI-powered social media analysis
2. Automated subdomain enumeration
3. Cloud asset discovery
4. Threat intelligence correlation
5. Comprehensive reporting

DEVSECOPS WORKFLOW
═══════════════════════════════════════════
1. Pre-commit: Secret scanning
2. Build: SAST + dependency check
3. Test: Unit + integration tests
4. Security: DAST + container scan
5. Deploy: Runtime protection
6. Monitor: Threat detection

CLOUD SECURITY WORKFLOW
═══════════════════════════════════════════
1. Asset inventory
2. Configuration audit
3. Permission review
4. Network topology mapping
5. Compliance checking
6. Remediation planning
```

---

## 🏆 Du är nu en Expert!

**Grattis!** Du har genomfört hela Nivå 5 och är nu:

🎖️ **Expert i OSINT** - Kan genomföra avancerad OSINT med AI
🎖️ **Cloud Security Specialist** - Kan audita AWS/Azure/GCP
🎖️ **DevSecOps Engineer** - Kan bygga säkra CI/CD-pipelines
🎖️ **Penetration Tester** - Kan genomföra professionella pentests
🎖️ **Security Automation** - Kan bygga egna säkerhetsverktyg

### Nästa Steg i Din Karriär:

🎯 **Bug Bounty Programs**
- HackerOne: https://hackerone.com
- Bugcrowd: https://bugcrowd.com
- Intigriti: https://intigriti.com

🎯 **Certifieringar**
- OSCP (Offensive Security Certified Professional)
- OSWE (Offensive Security Web Expert)
- CEH (Certified Ethical Hacker)
- GCIH (GIAC Certified Incident Handler)
- AWS Certified Security Specialty

🎯 **Community**
- OWASP Local Chapters
- DEF CON Groups
- Security meetups
- CTF competitions

🎯 **Fortsatt Lärande**
- TryHackMe Advanced Rooms
- HackTheBox Pro Labs
- PortSwigger Web Security Academy
- PentesterLab Pro

---

## 🔐 Final Security Reminder

Du har nu extremt kraftfulla färdigheter. Använd dem **ALLTID** etiskt:

✅ **Authorized Testing Only** - Skriftligt tillstånd
✅ **Responsible Disclosure** - Rapportera sårbarheter ansvarsfull
✅ **Protect Data** - Respektera privacy
✅ **Continuous Learning** - Säkerhet utvecklas ständigt
✅ **Give Back** - Dela kunskap, hjälp andra lära

---

**🎉 GRATULATIONER - DU HAR KLARAT NIVÅ 5! 🎉**

**[⬅️ Tillbaka till Nivå 4](OSINT_ZAP_Guide_Niva_4.md)** | **[🏠 Tillbaka till Översikt](OSINT_ZAP_Guide_README.md)**

---

*Nivå 5 Komplett! Du är nu en Expert inom OSINT, Pentesting och DevSecOps!* ✨
*Fortsätt lära, fortsätt hacka (etiskt!), och fortsätt bygga en säkrare digital värld.* 🌍🔒
