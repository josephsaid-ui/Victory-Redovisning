# 🌐 OSINT & OWASP ZAP Guide - Nivå 5: Expert-nivå

**Mål:** Behärska AI-driven OSINT, CI/CD-säkerhetsintegration, molnsäkerhetstestning och bli en komplett cybersäkerhetsexpert
**Förkunskaper:** Alla tidigare nivåer (1-4)
**Tidsåtgång:** 3-4 timmar
**Nivå:** Expert

---

## 📚 Innehållsförteckning

1. [AI-driven OSINT och Automation](#1-ai-driven-osint-och-automation)
2. [OWASP ZAP i CI/CD Pipelines](#2-owasp-zap-i-cicd-pipelines)
3. [Molnsäkerhetstestning](#3-molnsäkerhetstestning)
4. [Modern API Security Testing](#4-modern-api-security-testing)
5. [Container & Kubernetes Säkerhet](#5-container--kubernetes-säkerhet)
6. [Dark Web OSINT (Etiskt)](#6-dark-web-osint-etiskt)
7. [Case Studies: Verkliga Undersökningar](#7-case-studies-verkliga-undersökningar)
8. [Övningar (5.1-5.8)](#8-övningar)
9. [Stort Projekt: Enterprise Security Pipeline](#9-stort-projekt-enterprise-security-pipeline)

---

## 1. AI-driven OSINT och Automation

### 🤖 LLM för OSINT-analys

Moderna språkmodeller kan transformera OSINT-arbete genom att:
- Analysera stora mängder text (social media, forum, nyhetskällor)
- Identifiera mönster och anomalier
- Generera sammanfattningar och rapporter
- Automatisera språköversättningar

**Python-exempel med OpenAI API för OSINT-analys:**

```python
import openai
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

class AI_OSINT_Analyzer:
    """AI-driven OSINT analys med LLM"""

    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key
        self.results = []

    def scrape_target_data(self, url):
        """Samla in data från målsida"""
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extrahera relevant text
            text_content = soup.get_text(separator=' ', strip=True)
            return text_content[:4000]  # Begränsa längd
        except Exception as e:
            print(f"❌ Fel vid scraping: {e}")
            return None

    def analyze_with_llm(self, data, analysis_type="security"):
        """Analysera data med LLM"""

        prompts = {
            "security": """Analysera följande webbplatsdata från ett cybersäkerhetsperspektiv:
            - Identifiera potentiella säkerhetsrisker
            - Hitta exponerad känslig information
            - Notera teknologier som används
            - Rekommendera säkerhetsåtgärder

            Data:
            {data}
            """,

            "osint": """Utför OSINT-analys på följande data:
            - Identifiera nyckelinformation (personer, platser, organisationer)
            - Hitta metadata och dolda detaljer
            - Extrahera kontaktuppgifter och kopplingar
            - Sammanfatta viktiga fynd

            Data:
            {data}
            """,

            "threat": """Bedöm hotprofilen baserat på denna data:
            - Identifiera potentiella attackvektorer
            - Bedöm risk-nivå (låg/medel/hög)
            - Föreslå mitigationsstrategier
            - Prioritera åtgärder

            Data:
            {data}
            """
        }

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Du är en expert på cybersäkerhet och OSINT."},
                    {"role": "user", "content": prompts[analysis_type].format(data=data)}
                ],
                temperature=0.3,  # Låg för mer konsistent analys
                max_tokens=1500
            )

            analysis = response.choices[0].message.content
            return analysis

        except Exception as e:
            print(f"❌ LLM-analys misslyckades: {e}")
            return None

    def generate_report(self, target, analyses):
        """Generera komplett OSINT-rapport"""

        report = {
            "target": target,
            "timestamp": datetime.now().isoformat(),
            "analyses": analyses,
            "summary": "",
            "recommendations": []
        }

        # Använd LLM för att generera sammanfattning
        all_findings = "\n\n".join([f"{k}: {v}" for k, v in analyses.items()])

        summary_prompt = f"""Baserat på följande OSINT-fynd, skapa en kortfattad sammanfattning (max 200 ord):

{all_findings}

Inkludera:
1. Huvudsakliga fynd
2. Risk-bedömning
3. Prioriterade rekommendationer
"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Du är en cybersäkerhetsanalytiker."},
                    {"role": "user", "content": summary_prompt}
                ],
                temperature=0.3,
                max_tokens=500
            )

            report["summary"] = response.choices[0].message.content

        except Exception as e:
            print(f"❌ Sammanfattning misslyckades: {e}")

        return report

    def automated_investigation(self, target_url):
        """Komplett automatiserad OSINT-undersökning"""

        print(f"🔍 Startar AI-driven OSINT-undersökning av: {target_url}\n")

        # Steg 1: Samla data
        print("📥 Samlar in data...")
        scraped_data = self.scrape_target_data(target_url)

        if not scraped_data:
            return None

        # Steg 2: Multipelanalyser
        analyses = {}

        print("🤖 Utför säkerhetsanalys...")
        analyses["security"] = self.analyze_with_llm(scraped_data, "security")

        print("🤖 Utför OSINT-analys...")
        analyses["osint"] = self.analyze_with_llm(scraped_data, "osint")

        print("🤖 Utför hotbedömning...")
        analyses["threat"] = self.analyze_with_llm(scraped_data, "threat")

        # Steg 3: Generera rapport
        print("📊 Genererar rapport...\n")
        report = self.generate_report(target_url, analyses)

        return report

    def save_report(self, report, filename="osint_report.json"):
        """Spara rapport till fil"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"✅ Rapport sparad: {filename}")

# Användning
if __name__ == "__main__":
    # OBS: Använd bara på auktoriserade mål!
    analyzer = AI_OSINT_Analyzer(api_key="din-openai-api-nyckel")

    target = "http://testphp.vulnweb.com"  # Testmål
    report = analyzer.automated_investigation(target)

    if report:
        print("\n" + "="*60)
        print("📋 SAMMANFATTNING:")
        print("="*60)
        print(report["summary"])

        analyzer.save_report(report, f"osint_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
```

### 🔄 Machine Learning för Anomali-detektion

```python
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import numpy as np

class ML_SecurityAnalyzer:
    """ML-baserad säkerhetsanalys"""

    def __init__(self):
        self.model = IsolationForest(
            contamination=0.1,  # 10% anses vara anomalier
            random_state=42
        )
        self.scaler = StandardScaler()

    def analyze_zap_results(self, zap_alerts_file):
        """Analysera ZAP-varningar med ML"""

        # Läs in ZAP-resultat (JSON)
        with open(zap_alerts_file, 'r') as f:
            alerts = json.load(f)

        # Skapa features från varningar
        features = []
        for alert in alerts:
            features.append([
                alert.get('risk', 0),        # 0-3 (Info-High)
                alert.get('confidence', 0),  # 0-3
                len(alert.get('url', '')),   # URL-längd
                len(alert.get('description', '')),  # Beskrivningslängd
                alert.get('cweid', 0),       # CWE-ID
                len(alert.get('instances', []))  # Antal instanser
            ])

        # Normalisera data
        X = self.scaler.fit_transform(features)

        # Träna modell och prediktera
        predictions = self.model.fit_predict(X)

        # Identifiera anomalier (predictions == -1)
        anomalies = []
        for i, pred in enumerate(predictions):
            if pred == -1:
                anomalies.append({
                    'alert': alerts[i],
                    'anomaly_score': self.model.score_samples([X[i]])[0]
                })

        return sorted(anomalies, key=lambda x: x['anomaly_score'])

    def prioritize_vulnerabilities(self, vulnerabilities):
        """Prioritera sårbarheter med ML"""

        # Skapa feature-vektor
        features = []
        for vuln in vulnerabilities:
            features.append([
                vuln['cvss_score'],
                vuln['exploit_available'],  # 0 eller 1
                vuln['patch_available'],     # 0 eller 1
                vuln['asset_criticality'],   # 1-5
                vuln['exposure_level']       # 1-3 (internal/dmz/external)
            ])

        X = np.array(features)

        # Beräkna prioritetspoäng
        # Viktade summan av features
        weights = np.array([0.4, 0.2, -0.1, 0.3, 0.2])
        priority_scores = X.dot(weights)

        # Sortera och returnera
        sorted_indices = np.argsort(priority_scores)[::-1]

        prioritized = []
        for i in sorted_indices:
            prioritized.append({
                'vulnerability': vulnerabilities[i],
                'priority_score': priority_scores[i],
                'rank': len(prioritized) + 1
            })

        return prioritized

# Användning
analyzer = ML_SecurityAnalyzer()
anomalies = analyzer.analyze_zap_results('zap_alerts.json')

print("🚨 Upptäckta anomalier:")
for anomaly in anomalies[:5]:  # Top 5
    print(f"- {anomaly['alert']['name']} (score: {anomaly['anomaly_score']:.2f})")
```

---

## 2. OWASP ZAP i CI/CD Pipelines

### 🔧 Jenkins Integration

**Jenkinsfile för automatiserad säkerhetstestning:**

```groovy
pipeline {
    agent any

    environment {
        ZAP_PORT = '8090'
        TARGET_URL = 'https://staging.example.com'
        ZAP_API_KEY = credentials('zap-api-key')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Application') {
            steps {
                sh 'npm install'
                sh 'npm run build'
            }
        }

        stage('Deploy to Staging') {
            steps {
                sh './deploy-staging.sh'
                sleep(time: 30, unit: 'SECONDS')
            }
        }

        stage('ZAP Security Scan') {
            steps {
                script {
                    // Starta ZAP i daemon-läge
                    sh """
                        docker run -d --name zap-container \
                        -p ${ZAP_PORT}:${ZAP_PORT} \
                        -v \$(pwd)/zap-reports:/zap/reports \
                        owasp/zap2docker-stable \
                        zap.sh -daemon -port ${ZAP_PORT} -config api.key=${ZAP_API_KEY}
                    """

                    // Vänta på att ZAP startar
                    sleep(time: 30, unit: 'SECONDS')

                    // Kör Python-skript för scanning
                    sh """
                        python3 << 'EOF'
from zapv2 import ZAPv2
import time
import sys

zap = ZAPv2(
    apikey='${ZAP_API_KEY}',
    proxies={'http': 'http://localhost:${ZAP_PORT}', 'https': 'http://localhost:${ZAP_PORT}'}
)

target = '${TARGET_URL}'

print(f"🔍 Startar Spider på {target}")
scan_id = zap.spider.scan(target)

while int(zap.spider.status(scan_id)) < 100:
    print(f"Spider progress: {zap.spider.status(scan_id)}%")
    time.sleep(5)

print("✅ Spider klar")

print("🔍 Startar Active Scan")
scan_id = zap.ascan.scan(target)

while int(zap.ascan.status(scan_id)) < 100:
    print(f"Active Scan progress: {zap.ascan.status(scan_id)}%")
    time.sleep(10)

print("✅ Active Scan klar")

# Hämta resultat
alerts = zap.core.alerts(baseurl=target)
high_risk = [a for a in alerts if a['risk'] == 'High']
medium_risk = [a for a in alerts if a['risk'] == 'Medium']

print(f"\\n📊 RESULTAT:")
print(f"High Risk: {len(high_risk)}")
print(f"Medium Risk: {len(medium_risk)}")

# Generera rapport
with open('/zap/reports/zap_report.html', 'w') as f:
    f.write(zap.core.htmlreport())

# Fail pipeline om kritiska sårbarheter hittas
if len(high_risk) > 0:
    print("❌ PIPELINE FAILED: High-risk sårbarheter hittade!")
    sys.exit(1)

EOF
                    """
                }
            }

            post {
                always {
                    // Stoppa och ta bort ZAP-container
                    sh 'docker stop zap-container || true'
                    sh 'docker rm zap-container || true'
                }
            }
        }

        stage('Publish Results') {
            steps {
                publishHTML([
                    reportDir: 'zap-reports',
                    reportFiles: 'zap_report.html',
                    reportName: 'ZAP Security Report'
                ])
            }
        }
    }

    post {
        success {
            echo '✅ Säkerhetstester godkända!'
        }
        failure {
            echo '❌ Säkerhetstester misslyckades!'
            emailext(
                subject: "Security Scan Failed: ${env.JOB_NAME}",
                body: "Kritiska sårbarheter hittade. Se rapport: ${env.BUILD_URL}",
                to: 'security-team@example.com'
            )
        }
    }
}
```

### 🦊 GitLab CI/CD Integration

**`.gitlab-ci.yml`:**

```yaml
stages:
  - build
  - test
  - security
  - deploy

variables:
  ZAP_IMAGE: owasp/zap2docker-stable
  TARGET_URL: https://staging.example.com

build:
  stage: build
  script:
    - npm install
    - npm run build
  artifacts:
    paths:
      - dist/

test:
  stage: test
  script:
    - npm run test

zap_baseline_scan:
  stage: security
  image: ${ZAP_IMAGE}
  script:
    - mkdir -p zap-reports
    - |
      zap-baseline.py \
        -t ${TARGET_URL} \
        -r zap_baseline_report.html \
        -J zap_baseline_report.json \
        -w zap_baseline_report.md \
        -z "-config api.key=${ZAP_API_KEY}"
  artifacts:
    when: always
    paths:
      - zap-reports/
    reports:
      junit: zap-reports/zap_baseline_report.xml
  allow_failure: false

zap_full_scan:
  stage: security
  image: ${ZAP_IMAGE}
  script:
    - mkdir -p zap-reports
    - |
      zap-full-scan.py \
        -t ${TARGET_URL} \
        -r zap_full_report.html \
        -J zap_full_report.json \
        -z "-config api.key=${ZAP_API_KEY}"
  artifacts:
    when: always
    paths:
      - zap-reports/
  only:
    - main
    - production

zap_api_scan:
  stage: security
  image: ${ZAP_IMAGE}
  script:
    - mkdir -p zap-reports
    - |
      zap-api-scan.py \
        -t ${TARGET_URL}/api/openapi.json \
        -f openapi \
        -r zap_api_report.html \
        -J zap_api_report.json
  artifacts:
    when: always
    paths:
      - zap-reports/

deploy_production:
  stage: deploy
  script:
    - ./deploy-production.sh
  only:
    - main
  when: manual
```

### 🐙 GitHub Actions Integration

**`.github/workflows/security-scan.yml`:**

```yaml
name: Security Scan with OWASP ZAP

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '0 2 * * 1'  # Varje måndag kl 02:00

jobs:
  zap_scan:
    runs-on: ubuntu-latest
    name: OWASP ZAP Security Scan

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Build application
        run: |
          npm install
          npm run build

      - name: Deploy to staging
        run: |
          # Deploy till staging-miljö
          echo "Deploying to staging..."

      - name: Run ZAP Baseline Scan
        uses: zaproxy/action-baseline@v0.7.0
        with:
          target: 'https://staging.example.com'
          rules_file_name: '.zap/rules.tsv'
          cmd_options: '-a'

      - name: Run ZAP Full Scan
        if: github.ref == 'refs/heads/main'
        uses: zaproxy/action-full-scan@v0.4.0
        with:
          target: 'https://staging.example.com'
          rules_file_name: '.zap/rules.tsv'
          cmd_options: '-a -j'

      - name: Run ZAP API Scan
        uses: zaproxy/action-api-scan@v0.2.0
        with:
          target: 'https://staging.example.com/api/openapi.json'
          format: 'openapi'

      - name: Upload ZAP Reports
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: zap-reports
          path: |
            report_html.html
            report_json.json
            report_md.md

      - name: Create Issue on Failure
        if: failure()
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: '🚨 Security Scan Failed',
              body: 'OWASP ZAP scan detected vulnerabilities. Check the artifacts for details.',
              labels: ['security', 'bug']
            })
```

---

## 3. Molnsäkerhetstestning

### ☁️ AWS Security Testing

**Python-skript för AWS säkerhetsgranskning:**

```python
import boto3
from botocore.exceptions import ClientError
import json
from datetime import datetime

class AWS_SecurityAuditor:
    """AWS säkerhetsgranskning"""

    def __init__(self, profile_name='default', region='eu-north-1'):
        self.session = boto3.Session(profile_name=profile_name, region_name=region)
        self.findings = []

    def audit_s3_buckets(self):
        """Granska S3-buckets för säkerhetsrisker"""

        s3 = self.session.client('s3')

        try:
            buckets = s3.list_buckets()['Buckets']
            print(f"🪣 Granskar {len(buckets)} S3-buckets...\n")

            for bucket in buckets:
                bucket_name = bucket['Name']
                issues = []

                # Kontrollera offentlig access
                try:
                    acl = s3.get_bucket_acl(Bucket=bucket_name)
                    for grant in acl['Grants']:
                        if grant['Grantee'].get('URI') == 'http://acs.amazonaws.com/groups/global/AllUsers':
                            issues.append("❌ KRITISK: Bucket är offentligt tillgänglig!")

                except ClientError as e:
                    issues.append(f"⚠️ Kunde inte läsa ACL: {e}")

                # Kontrollera kryptering
                try:
                    encryption = s3.get_bucket_encryption(Bucket=bucket_name)
                except ClientError:
                    issues.append("⚠️ Kryptering är inte aktiverad!")

                # Kontrollera versioning
                try:
                    versioning = s3.get_bucket_versioning(Bucket=bucket_name)
                    if versioning.get('Status') != 'Enabled':
                        issues.append("⚠️ Versioning är inte aktiverad!")
                except ClientError:
                    issues.append("⚠️ Kunde inte kontrollera versioning")

                # Kontrollera logging
                try:
                    logging = s3.get_bucket_logging(Bucket=bucket_name)
                    if 'LoggingEnabled' not in logging:
                        issues.append("⚠️ Logging är inte aktiverad!")
                except ClientError:
                    issues.append("⚠️ Kunde inte kontrollera logging")

                if issues:
                    self.findings.append({
                        'service': 'S3',
                        'resource': bucket_name,
                        'issues': issues
                    })

                    print(f"Bucket: {bucket_name}")
                    for issue in issues:
                        print(f"  {issue}")
                    print()

        except ClientError as e:
            print(f"❌ Fel vid S3-granskning: {e}")

    def audit_ec2_instances(self):
        """Granska EC2-instanser"""

        ec2 = self.session.client('ec2')

        try:
            instances = ec2.describe_instances()

            for reservation in instances['Reservations']:
                for instance in reservation['Instances']:
                    instance_id = instance['InstanceId']
                    issues = []

                    # Kontrollera om instans har offentlig IP
                    if 'PublicIpAddress' in instance:
                        issues.append(f"⚠️ Instans har offentlig IP: {instance['PublicIpAddress']}")

                    # Kontrollera säkerhetsgrupper
                    for sg in instance['SecurityGroups']:
                        sg_id = sg['GroupId']
                        sg_details = ec2.describe_security_groups(GroupIds=[sg_id])

                        for perm in sg_details['SecurityGroups'][0]['IpPermissions']:
                            # Kontrollera om SSH (22) eller RDP (3389) är öppet för alla
                            if perm.get('FromPort') in [22, 3389]:
                                for ip_range in perm.get('IpRanges', []):
                                    if ip_range.get('CidrIp') == '0.0.0.0/0':
                                        issues.append(f"❌ KRITISK: Port {perm['FromPort']} öppen för alla (0.0.0.0/0)!")

                    # Kontrollera om IMDSv2 är aktiverat
                    if instance.get('MetadataOptions', {}).get('HttpTokens') != 'required':
                        issues.append("⚠️ IMDSv2 är inte påtvingat (metadata-säkerhet)")

                    if issues:
                        self.findings.append({
                            'service': 'EC2',
                            'resource': instance_id,
                            'issues': issues
                        })

        except ClientError as e:
            print(f"❌ Fel vid EC2-granskning: {e}")

    def audit_iam_users(self):
        """Granska IAM-användare"""

        iam = self.session.client('iam')

        try:
            users = iam.list_users()['Users']

            for user in users:
                username = user['UserName']
                issues = []

                # Kontrollera MFA
                mfa_devices = iam.list_mfa_devices(UserName=username)
                if not mfa_devices['MFADevices']:
                    issues.append("⚠️ MFA är inte aktiverat!")

                # Kontrollera ålder på access keys
                access_keys = iam.list_access_keys(UserName=username)
                for key in access_keys['AccessKeyMetadata']:
                    age_days = (datetime.now(key['CreateDate'].tzinfo) - key['CreateDate']).days
                    if age_days > 90:
                        issues.append(f"⚠️ Access key {key['AccessKeyId']} är {age_days} dagar gammal (>90 dagar)")

                # Kontrollera lösenordspolicy
                try:
                    login_profile = iam.get_login_profile(UserName=username)
                    password_age = (datetime.now(login_profile['LoginProfile']['CreateDate'].tzinfo) -
                                  login_profile['LoginProfile']['CreateDate']).days
                    if password_age > 90:
                        issues.append(f"⚠️ Lösenord är {password_age} dagar gammalt (>90 dagar)")
                except ClientError:
                    pass  # Användare har inget lösenord (API-only)

                if issues:
                    self.findings.append({
                        'service': 'IAM',
                        'resource': username,
                        'issues': issues
                    })

        except ClientError as e:
            print(f"❌ Fel vid IAM-granskning: {e}")

    def audit_rds_databases(self):
        """Granska RDS-databaser"""

        rds = self.session.client('rds')

        try:
            databases = rds.describe_db_instances()['DBInstances']

            for db in databases:
                db_id = db['DBInstanceIdentifier']
                issues = []

                # Kontrollera offentlig tillgänglighet
                if db.get('PubliclyAccessible'):
                    issues.append("❌ KRITISK: Databas är offentligt tillgänglig!")

                # Kontrollera kryptering
                if not db.get('StorageEncrypted'):
                    issues.append("⚠️ Storage-kryptering är inte aktiverad!")

                # Kontrollera backups
                if db.get('BackupRetentionPeriod', 0) < 7:
                    issues.append(f"⚠️ Backup retention är endast {db.get('BackupRetentionPeriod')} dagar (rekommenderat: ≥7)")

                # Kontrollera auto minor version upgrade
                if not db.get('AutoMinorVersionUpgrade'):
                    issues.append("⚠️ Automatiska minor version upgrades är inte aktiverade!")

                if issues:
                    self.findings.append({
                        'service': 'RDS',
                        'resource': db_id,
                        'issues': issues
                    })

        except ClientError as e:
            print(f"❌ Fel vid RDS-granskning: {e}")

    def generate_report(self):
        """Generera säkerhetsrapport"""

        report = {
            'timestamp': datetime.now().isoformat(),
            'total_findings': len(self.findings),
            'critical_issues': 0,
            'warnings': 0,
            'findings': self.findings
        }

        # Räkna allvarlighetsgrad
        for finding in self.findings:
            for issue in finding['issues']:
                if 'KRITISK' in issue:
                    report['critical_issues'] += 1
                else:
                    report['warnings'] += 1

        # Spara till fil
        filename = f"aws_security_audit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        print("\n" + "="*60)
        print("📊 AWS SÄKERHETSGRANSKNING - SAMMANFATTNING")
        print("="*60)
        print(f"Totalt antal fynd: {report['total_findings']}")
        print(f"❌ Kritiska problem: {report['critical_issues']}")
        print(f"⚠️  Varningar: {report['warnings']}")
        print(f"\n✅ Rapport sparad: {filename}")

        return report

    def full_audit(self):
        """Kör fullständig säkerhetsgranskning"""

        print("🔍 AWS Säkerhetsgranskning - Startar...\n")

        self.audit_s3_buckets()
        self.audit_ec2_instances()
        self.audit_iam_users()
        self.audit_rds_databases()

        return self.generate_report()

# Användning
if __name__ == "__main__":
    auditor = AWS_SecurityAuditor(profile_name='default', region='eu-north-1')
    report = auditor.full_audit()
```

### 🔵 Azure Security Testing

**PowerShell-skript för Azure säkerhet:**

```powershell
# Azure Security Audit Script

# Kräver Azure PowerShell Module
# Install-Module -Name Az -AllowClobber -Scope CurrentUser

Connect-AzAccount

$findings = @()

# Granska Storage Accounts
Write-Host "🔍 Granskar Storage Accounts..." -ForegroundColor Cyan

$storageAccounts = Get-AzStorageAccount

foreach ($sa in $storageAccounts) {
    $issues = @()

    # Kontrollera HTTPS-only
    if (-not $sa.EnableHttpsTrafficOnly) {
        $issues += "⚠️ HTTPS-only är inte aktiverat!"
    }

    # Kontrollera blob public access
    if ($sa.AllowBlobPublicAccess) {
        $issues += "❌ KRITISK: Public blob access är tillåtet!"
    }

    # Kontrollera TLS version
    if ($sa.MinimumTlsVersion -lt "TLS1_2") {
        $issues += "⚠️ TLS version är lägre än 1.2!"
    }

    if ($issues.Count -gt 0) {
        $findings += @{
            Service = "Storage Account"
            Resource = $sa.StorageAccountName
            Issues = $issues
        }
    }
}

# Granska Virtual Machines
Write-Host "🔍 Granskar Virtual Machines..." -ForegroundColor Cyan

$vms = Get-AzVM

foreach ($vm in $vms) {
    $issues = @()

    # Kontrollera disk encryption
    $diskEncryption = Get-AzVMDiskEncryptionStatus -ResourceGroupName $vm.ResourceGroupName -VMName $vm.Name

    if ($diskEncryption.OsVolumeEncrypted -ne "Encrypted") {
        $issues += "⚠️ OS disk är inte krypterad!"
    }

    # Kontrollera NSG (Network Security Group)
    $nics = $vm.NetworkProfile.NetworkInterfaces
    foreach ($nic in $nics) {
        $nicResource = Get-AzNetworkInterface -ResourceId $nic.Id
        if (-not $nicResource.NetworkSecurityGroup) {
            $issues += "⚠️ Inget NSG kopplat till nätverksgränssnitt!"
        }
    }

    if ($issues.Count -gt 0) {
        $findings += @{
            Service = "Virtual Machine"
            Resource = $vm.Name
            Issues = $issues
        }
    }
}

# Granska Network Security Groups
Write-Host "🔍 Granskar Network Security Groups..." -ForegroundColor Cyan

$nsgs = Get-AzNetworkSecurityGroup

foreach ($nsg in $nsgs) {
    $issues = @()

    foreach ($rule in $nsg.SecurityRules) {
        # Kontrollera öppna farliga portar
        if ($rule.Direction -eq "Inbound" -and
            $rule.Access -eq "Allow" -and
            $rule.SourceAddressPrefix -eq "*") {

            if ($rule.DestinationPortRange -match "22|3389|3306|5432|27017") {
                $issues += "❌ KRITISK: Port $($rule.DestinationPortRange) öppen från Internet!"
            }
        }
    }

    if ($issues.Count -gt 0) {
        $findings += @{
            Service = "Network Security Group"
            Resource = $nsg.Name
            Issues = $issues
        }
    }
}

# Generera rapport
$report = @{
    Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    TotalFindings = $findings.Count
    Findings = $findings
}

$report | ConvertTo-Json -Depth 10 | Out-File "azure_security_audit_$(Get-Date -Format 'yyyyMMdd_HHmmss').json"

Write-Host "`n$('='*60)" -ForegroundColor Yellow
Write-Host "📊 AZURE SÄKERHETSGRANSKNING - SAMMANFATTNING" -ForegroundColor Yellow
Write-Host $('='*60) -ForegroundColor Yellow
Write-Host "Totalt antal fynd: $($findings.Count)" -ForegroundColor White

$criticalCount = ($findings.Issues | Where-Object { $_ -match "KRITISK" }).Count
Write-Host "❌ Kritiska problem: $criticalCount" -ForegroundColor Red
Write-Host "✅ Rapport sparad" -ForegroundColor Green
```

---

## 4. Modern API Security Testing

### 🔌 REST API Testing med ZAP

```python
from zapv2 import ZAPv2
import requests
import json

class API_SecurityTester:
    """REST API säkerhetstestning"""

    def __init__(self, zap_proxy='http://localhost:8090', api_key='your-api-key'):
        self.zap = ZAPv2(apikey=api_key, proxies={
            'http': zap_proxy,
            'https': zap_proxy
        })
        self.results = []

    def test_authentication(self, api_base_url):
        """Testa autentisering"""

        print("🔐 Testar autentisering...\n")

        tests = []

        # Test 1: Utan token
        print("1. Försöker komma åt skyddad endpoint utan token...")
        response = requests.get(f"{api_base_url}/api/protected")
        if response.status_code != 401:
            tests.append({
                'test': 'No auth token',
                'result': '❌ FAIL',
                'issue': f'Fick {response.status_code} istället för 401'
            })
        else:
            tests.append({'test': 'No auth token', 'result': '✅ PASS'})

        # Test 2: Med ogiltig token
        print("2. Försöker med ogiltig token...")
        headers = {'Authorization': 'Bearer invalid_token_12345'}
        response = requests.get(f"{api_base_url}/api/protected", headers=headers)
        if response.status_code != 401:
            tests.append({
                'test': 'Invalid token',
                'result': '❌ FAIL',
                'issue': f'Fick {response.status_code} istället för 401'
            })
        else:
            tests.append({'test': 'Invalid token', 'result': '✅ PASS'})

        # Test 3: Token replay
        print("3. Testar token replay...")
        # Få giltig token
        login_response = requests.post(f"{api_base_url}/api/login", json={
            'username': 'testuser',
            'password': 'testpass'
        })
        if login_response.status_code == 200:
            token = login_response.json()['token']

            # Logga ut
            requests.post(f"{api_base_url}/api/logout", headers={
                'Authorization': f'Bearer {token}'
            })

            # Försök använda samma token igen
            response = requests.get(f"{api_base_url}/api/protected", headers={
                'Authorization': f'Bearer {token}'
            })
            if response.status_code == 200:
                tests.append({
                    'test': 'Token replay after logout',
                    'result': '❌ FAIL',
                    'issue': 'Token fungerar fortfarande efter logout!'
                })
            else:
                tests.append({'test': 'Token replay after logout', 'result': '✅ PASS'})

        self.results.append({'category': 'Authentication', 'tests': tests})
        return tests

    def test_authorization(self, api_base_url, user_token, admin_token):
        """Testa auktorisering (IDOR, Privilege Escalation)"""

        print("\n🔒 Testar auktorisering...\n")

        tests = []

        # Test 1: IDOR - Access other user's data
        print("1. Testar IDOR (Insecure Direct Object Reference)...")

        # Skapa två användare
        user1_id = 1
        user2_id = 2

        headers_user1 = {'Authorization': f'Bearer {user_token}'}

        # Försök komma åt user2's data med user1's token
        response = requests.get(
            f"{api_base_url}/api/users/{user2_id}/profile",
            headers=headers_user1
        )

        if response.status_code == 200:
            tests.append({
                'test': 'IDOR - Access other user data',
                'result': '❌ FAIL',
                'issue': 'Användare kan komma åt annan användares data!'
            })
        elif response.status_code == 403:
            tests.append({'test': 'IDOR - Access other user data', 'result': '✅ PASS'})

        # Test 2: Privilege Escalation
        print("2. Testar privilege escalation...")

        # Försök utföra admin-åtgärd med vanlig användare
        response = requests.delete(
            f"{api_base_url}/api/admin/users/{user2_id}",
            headers=headers_user1
        )

        if response.status_code == 200:
            tests.append({
                'test': 'Privilege escalation',
                'result': '❌ FAIL',
                'issue': 'Vanlig användare kan utföra admin-åtgärder!'
            })
        elif response.status_code == 403:
            tests.append({'test': 'Privilege escalation', 'result': '✅ PASS'})

        # Test 3: Mass Assignment
        print("3. Testar mass assignment...")

        payload = {
            'username': 'testuser',
            'email': 'test@example.com',
            'is_admin': True  # Försök sätta admin-flagga
        }

        response = requests.put(
            f"{api_base_url}/api/users/{user1_id}",
            headers=headers_user1,
            json=payload
        )

        if response.status_code == 200:
            # Kontrollera om is_admin faktiskt uppdaterades
            profile = requests.get(
                f"{api_base_url}/api/users/{user1_id}/profile",
                headers=headers_user1
            ).json()

            if profile.get('is_admin'):
                tests.append({
                    'test': 'Mass assignment',
                    'result': '❌ FAIL',
                    'issue': 'Användare kan sätta admin-flagga via mass assignment!'
                })
            else:
                tests.append({'test': 'Mass assignment', 'result': '✅ PASS'})

        self.results.append({'category': 'Authorization', 'tests': tests})
        return tests

    def test_input_validation(self, api_base_url, auth_token):
        """Testa input-validering"""

        print("\n✅ Testar input-validering...\n")

        tests = []
        headers = {'Authorization': f'Bearer {auth_token}'}

        # Test 1: SQL Injection i query parameter
        print("1. Testar SQL injection i query parameter...")

        sql_payloads = [
            "' OR '1'='1",
            "1' UNION SELECT NULL--",
            "admin'--",
            "1' AND 1=1--"
        ]

        for payload in sql_payloads:
            response = requests.get(
                f"{api_base_url}/api/search?q={payload}",
                headers=headers
            )

            # Kolla efter SQL-fel i response
            if any(error in response.text.lower() for error in
                   ['sql', 'mysql', 'postgresql', 'syntax error', 'database']):
                tests.append({
                    'test': f'SQL Injection: {payload}',
                    'result': '❌ FAIL',
                    'issue': 'SQL-fel exponeras i response!'
                })
                break
        else:
            tests.append({'test': 'SQL Injection in query param', 'result': '✅ PASS'})

        # Test 2: XSS i JSON body
        print("2. Testar XSS i JSON body...")

        xss_payloads = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "';alert('XSS');//"
        ]

        for payload in xss_payloads:
            response = requests.post(
                f"{api_base_url}/api/comments",
                headers=headers,
                json={'comment': payload}
            )

            if response.status_code == 200:
                # Hämta kommentar och kolla om payload finns okodad
                comment_response = requests.get(
                    f"{api_base_url}/api/comments",
                    headers=headers
                )

                if payload in comment_response.text:
                    tests.append({
                        'test': f'XSS: {payload}',
                        'result': '❌ FAIL',
                        'issue': 'XSS-payload sparad och returnerad utan encoding!'
                    })
                    break
        else:
            tests.append({'test': 'XSS in JSON body', 'result': '✅ PASS'})

        # Test 3: Command Injection
        print("3. Testar command injection...")

        cmd_payloads = [
            "; ls -la",
            "| whoami",
            "&& cat /etc/passwd"
        ]

        for payload in cmd_payloads:
            response = requests.post(
                f"{api_base_url}/api/execute",
                headers=headers,
                json={'command': f'ping {payload}'}
            )

            # Kolla om command output finns i response
            if any(indicator in response.text for indicator in
                   ['root:', 'bin:', 'total ', 'drwx']):
                tests.append({
                    'test': f'Command Injection: {payload}',
                    'result': '❌ FAIL',
                    'issue': 'Command injection möjlig!'
                })
                break
        else:
            tests.append({'test': 'Command Injection', 'result': '✅ PASS'})

        self.results.append({'category': 'Input Validation', 'tests': tests})
        return tests

    def test_rate_limiting(self, api_base_url):
        """Testa rate limiting"""

        print("\n⏱️ Testar rate limiting...\n")

        tests = []

        # Skicka många requests snabbt
        print("Skickar 100 requests...")
        blocked_count = 0

        for i in range(100):
            response = requests.get(f"{api_base_url}/api/public")
            if response.status_code == 429:  # Too Many Requests
                blocked_count += 1

        if blocked_count == 0:
            tests.append({
                'test': 'Rate limiting',
                'result': '❌ FAIL',
                'issue': 'Ingen rate limiting implementerad!'
            })
        else:
            tests.append({
                'test': 'Rate limiting',
                'result': '✅ PASS',
                'info': f'{blocked_count}/100 requests blockerades'
            })

        self.results.append({'category': 'Rate Limiting', 'tests': tests})
        return tests

    def generate_report(self):
        """Generera testrapport"""

        total_tests = sum(len(cat['tests']) for cat in self.results)
        failed_tests = sum(
            1 for cat in self.results
            for test in cat['tests']
            if test['result'] == '❌ FAIL'
        )

        print("\n" + "="*60)
        print("📊 API SÄKERHETSTEST - SAMMANFATTNING")
        print("="*60)
        print(f"Totalt antal tester: {total_tests}")
        print(f"✅ Godkända: {total_tests - failed_tests}")
        print(f"❌ Misslyckade: {failed_tests}")
        print("\nDetaljer per kategori:")

        for category in self.results:
            print(f"\n{category['category']}:")
            for test in category['tests']:
                print(f"  {test['result']} {test['test']}")
                if 'issue' in test:
                    print(f"      Issue: {test['issue']}")

        # Spara rapport
        filename = f"api_security_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)

        print(f"\n✅ Rapport sparad: {filename}")

        return self.results

# Användning
if __name__ == "__main__":
    tester = API_SecurityTester()

    api_base = "https://api.example.com"
    user_token = "user_jwt_token_here"
    admin_token = "admin_jwt_token_here"

    tester.test_authentication(api_base)
    tester.test_authorization(api_base, user_token, admin_token)
    tester.test_input_validation(api_base, user_token)
    tester.test_rate_limiting(api_base)

    tester.generate_report()
```

### 🔷 GraphQL Security Testing

```python
import requests
import json

class GraphQL_SecurityTester:
    """GraphQL-specifik säkerhetstestning"""

    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.findings = []

    def test_introspection(self):
        """Testa om introspection är aktiverad (bör vara av i produktion)"""

        print("🔍 Testar GraphQL introspection...\n")

        introspection_query = """
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

        response = requests.post(
            self.endpoint,
            json={'query': introspection_query}
        )

        if response.status_code == 200 and '__schema' in response.text:
            self.findings.append({
                'test': 'Introspection',
                'severity': 'MEDIUM',
                'issue': 'GraphQL introspection är aktiverad i produktion!',
                'recommendation': 'Inaktivera introspection i produktion'
            })
            print("❌ Introspection är aktiverad!")
            return True
        else:
            print("✅ Introspection är inaktiverad")
            return False

    def test_batching_attack(self):
        """Testa batch query attacks (DoS)"""

        print("\n⚡ Testar batch query attack...\n")

        # Skapa en batch med många queries
        batch_query = "{ " + " ".join([f"q{i}: __typename" for i in range(1000)]) + " }"

        response = requests.post(
            self.endpoint,
            json={'query': batch_query}
        )

        if response.status_code == 200:
            self.findings.append({
                'test': 'Batch Query Attack',
                'severity': 'HIGH',
                'issue': 'Servern accepterar stora batch queries (DoS-risk)!',
                'recommendation': 'Implementera query depth/complexity limiting'
            })
            print("❌ Batch attack möjlig!")
            return True
        else:
            print("✅ Batch queries begränsade")
            return False

    def test_depth_limit(self):
        """Testa query depth limiting"""

        print("\n🕳️ Testar query depth limit...\n")

        # Skapa en djup nested query
        deep_query = """
        {
            user {
                posts {
                    comments {
                        author {
                            posts {
                                comments {
                                    author {
                                        posts {
                                            id
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        """

        response = requests.post(
            self.endpoint,
            json={'query': deep_query}
        )

        if response.status_code == 200 and 'errors' not in response.json():
            self.findings.append({
                'test': 'Query Depth Limit',
                'severity': 'MEDIUM',
                'issue': 'Inga depth limits implementerade (DoS-risk)!',
                'recommendation': 'Implementera max query depth (t.ex. 5-7 nivåer)'
            })
            print("❌ Inga depth limits!")
            return True
        else:
            print("✅ Depth limits fungerar")
            return False

    def test_authorization(self):
        """Testa field-level authorization"""

        print("\n🔒 Testar field-level authorization...\n")

        # Försök komma åt känsliga fält utan auth
        sensitive_query = """
        {
            users {
                id
                email
                password
                ssn
                creditCard
            }
        }
        """

        response = requests.post(
            self.endpoint,
            json={'query': sensitive_query}
        )

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and data['data'].get('users'):
                # Kolla vilka känsliga fält som exponeras
                exposed_fields = []
                for field in ['password', 'ssn', 'creditCard']:
                    if field in str(data):
                        exposed_fields.append(field)

                if exposed_fields:
                    self.findings.append({
                        'test': 'Field-Level Authorization',
                        'severity': 'CRITICAL',
                        'issue': f'Känsliga fält exponerade: {", ".join(exposed_fields)}!',
                        'recommendation': 'Implementera field-level authorization'
                    })
                    print(f"❌ Känsliga fält exponerade: {exposed_fields}")
                    return True

        print("✅ Field-level authorization fungerar")
        return False

    def generate_report(self):
        """Generera säkerhetsrapport"""

        print("\n" + "="*60)
        print("📊 GRAPHQL SÄKERHETSTEST - SAMMANFATTNING")
        print("="*60)
        print(f"Totalt antal fynd: {len(self.findings)}\n")

        for finding in self.findings:
            severity_emoji = {
                'CRITICAL': '🔴',
                'HIGH': '🟠',
                'MEDIUM': '🟡',
                'LOW': '🟢'
            }
            print(f"{severity_emoji[finding['severity']]} [{finding['severity']}] {finding['test']}")
            print(f"   Issue: {finding['issue']}")
            print(f"   Fix: {finding['recommendation']}\n")

        return self.findings

# Användning
tester = GraphQL_SecurityTester("https://api.example.com/graphql")
tester.test_introspection()
tester.test_batching_attack()
tester.test_depth_limit()
tester.test_authorization()
tester.generate_report()
```

---

## 5. Container & Kubernetes Säkerhet

### 🐳 Docker Security Scanning

```python
import subprocess
import json

class Docker_SecurityScanner:
    """Docker container säkerhetsscanning"""

    def __init__(self):
        self.vulnerabilities = []

    def scan_image_with_trivy(self, image_name):
        """Scanna Docker-image med Trivy"""

        print(f"🔍 Scannar {image_name} med Trivy...\n")

        # Kör Trivy scan
        result = subprocess.run(
            ['trivy', 'image', '--format', 'json', '--severity', 'HIGH,CRITICAL', image_name],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            scan_data = json.loads(result.stdout)

            for target in scan_data.get('Results', []):
                for vuln in target.get('Vulnerabilities', []):
                    self.vulnerabilities.append({
                        'image': image_name,
                        'cve': vuln.get('VulnerabilityID'),
                        'package': vuln.get('PkgName'),
                        'severity': vuln.get('Severity'),
                        'fixed_version': vuln.get('FixedVersion', 'N/A')
                    })

            print(f"✅ Hittade {len(self.vulnerabilities)} sårbarheter\n")
        else:
            print(f"❌ Fel vid scanning: {result.stderr}")

    def audit_dockerfile(self, dockerfile_path):
        """Granska Dockerfile för best practices"""

        print(f"🔍 Granskar {dockerfile_path}...\n")

        issues = []

        with open(dockerfile_path, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines, 1):
            line = line.strip()

            # Kolla efter root user
            if line.startswith('USER root') or (not any('USER' in l for l in lines)):
                issues.append({
                    'line': i,
                    'issue': 'Container kör som root',
                    'severity': 'HIGH',
                    'recommendation': 'Lägg till: USER nonroot'
                })

            # Kolla efter hårdkodade secrets
            if any(keyword in line.upper() for keyword in ['PASSWORD=', 'API_KEY=', 'SECRET=']):
                issues.append({
                    'line': i,
                    'issue': 'Hårdkodad secret upptäckt',
                    'severity': 'CRITICAL',
                    'recommendation': 'Använd secrets management (Docker secrets, K8s secrets)'
                })

            # Kolla efter latest tag
            if 'FROM' in line and ':latest' in line:
                issues.append({
                    'line': i,
                    'issue': 'Använder :latest tag',
                    'severity': 'MEDIUM',
                    'recommendation': 'Använd specifik version-tag'
                })

            # Kolla efter curl | bash
            if 'curl' in line and '|' in line and 'bash' in line:
                issues.append({
                    'line': i,
                    'issue': 'Osäker curl | bash pattern',
                    'severity': 'HIGH',
                    'recommendation': 'Ladda ner och verifiera innan exekvering'
                })

        print(f"📋 Hittade {len(issues)} problem i Dockerfile:\n")
        for issue in issues:
            print(f"  Rad {issue['line']} [{issue['severity']}]: {issue['issue']}")
            print(f"    Fix: {issue['recommendation']}\n")

        return issues

# Användning
scanner = Docker_SecurityScanner()
scanner.scan_image_with_trivy('myapp:latest')
scanner.audit_dockerfile('./Dockerfile')
```

### ☸️ Kubernetes Security Audit

```python
from kubernetes import client, config
import yaml

class K8s_SecurityAuditor:
    """Kubernetes säkerhetsgranskning"""

    def __init__(self):
        config.load_kube_config()
        self.v1 = client.CoreV1Api()
        self.apps_v1 = client.AppsV1Api()
        self.findings = []

    def audit_pod_security(self):
        """Granska pod säkerhetskonfiguration"""

        print("🔍 Granskar Pods...\n")

        pods = self.v1.list_pod_for_all_namespaces()

        for pod in pods.items:
            pod_issues = []

            # Kolla om pod kör som root
            for container in pod.spec.containers:
                sec_context = container.security_context

                if not sec_context or sec_context.run_as_non_root != True:
                    pod_issues.append({
                        'container': container.name,
                        'issue': 'Kör inte explicit som non-root',
                        'severity': 'HIGH'
                    })

                if not sec_context or sec_context.read_only_root_filesystem != True:
                    pod_issues.append({
                        'container': container.name,
                        'issue': 'Root filesystem är inte read-only',
                        'severity': 'MEDIUM'
                    })

                if not sec_context or sec_context.allow_privilege_escalation != False:
                    pod_issues.append({
                        'container': container.name,
                        'issue': 'Privilege escalation inte explicit disabled',
                        'severity': 'HIGH'
                    })

                # Kolla capabilities
                if sec_context and sec_context.capabilities:
                    if sec_context.capabilities.add:
                        pod_issues.append({
                            'container': container.name,
                            'issue': f'Lägger till capabilities: {sec_context.capabilities.add}',
                            'severity': 'MEDIUM'
                        })

            if pod_issues:
                self.findings.append({
                    'resource_type': 'Pod',
                    'name': pod.metadata.name,
                    'namespace': pod.metadata.namespace,
                    'issues': pod_issues
                })

    def audit_network_policies(self):
        """Granska network policies"""

        print("🔍 Granskar Network Policies...\n")

        networking_v1 = client.NetworkingV1Api()
        policies = networking_v1.list_network_policy_for_all_namespaces()

        # Kolla vilka namespaces som saknar network policies
        namespaces = self.v1.list_namespace()
        namespaces_with_policy = set(p.metadata.namespace for p in policies.items)

        for ns in namespaces.items:
            if ns.metadata.name not in namespaces_with_policy:
                if ns.metadata.name not in ['kube-system', 'kube-public', 'kube-node-lease']:
                    self.findings.append({
                        'resource_type': 'Namespace',
                        'name': ns.metadata.name,
                        'issues': [{
                            'issue': 'Ingen NetworkPolicy definierad',
                            'severity': 'MEDIUM',
                            'recommendation': 'Implementera network segmentation'
                        }]
                    })

    def audit_rbac(self):
        """Granska RBAC-konfiguration"""

        print("🔍 Granskar RBAC...\n")

        rbac_v1 = client.RbacAuthorizationV1Api()

        # Kolla ClusterRoleBindings
        cluster_role_bindings = rbac_v1.list_cluster_role_binding()

        for binding in cluster_role_bindings.items:
            # Kolla om cluster-admin är bundet till för många subjects
            if binding.role_ref.name == 'cluster-admin':
                if binding.subjects:
                    for subject in binding.subjects:
                        if subject.kind == 'ServiceAccount':
                            self.findings.append({
                                'resource_type': 'ClusterRoleBinding',
                                'name': binding.metadata.name,
                                'issues': [{
                                    'issue': f'ServiceAccount {subject.name} har cluster-admin!',
                                    'severity': 'CRITICAL',
                                    'recommendation': 'Använd least-privilege principle'
                                }]
                            })

    def generate_report(self):
        """Generera säkerhetsrapport"""

        print("\n" + "="*60)
        print("📊 KUBERNETES SÄKERHETSGRANSKNING")
        print("="*60)
        print(f"Totalt antal fynd: {len(self.findings)}\n")

        # Gruppera per severity
        critical = sum(1 for f in self.findings for i in f['issues'] if i.get('severity') == 'CRITICAL')
        high = sum(1 for f in self.findings for i in f['issues'] if i.get('severity') == 'HIGH')
        medium = sum(1 for f in self.findings for i in f['issues'] if i.get('severity') == 'MEDIUM')

        print(f"🔴 CRITICAL: {critical}")
        print(f"🟠 HIGH: {high}")
        print(f"🟡 MEDIUM: {medium}\n")

        for finding in self.findings[:10]:  # Visa top 10
            print(f"{finding['resource_type']}: {finding['name']} ({finding.get('namespace', 'N/A')})")
            for issue in finding['issues']:
                print(f"  [{issue.get('severity', 'INFO')}] {issue['issue']}")
            print()

        # Spara full rapport
        with open('k8s_security_audit.json', 'w') as f:
            json.dump(self.findings, f, indent=2)

        print("✅ Full rapport sparad: k8s_security_audit.json")

# Användning
auditor = K8s_SecurityAuditor()
auditor.audit_pod_security()
auditor.audit_network_policies()
auditor.audit_rbac()
auditor.generate_report()
```

---

## 6. Dark Web OSINT (Etiskt)

**⚠️ VARNING:** Dark Web-forskning måste göras etiskt och lagligt. Använd endast för legitim säkerhetsforskning.

### 🧅 Tor-baserad OSINT

```python
import requests
from bs4 import BeautifulSoup
import socks
import socket

class DarkWeb_OSINT:
    """Etisk Dark Web OSINT (endast för forskning!)"""

    def __init__(self, tor_proxy_port=9050):
        # Konfigurera Tor proxy
        socks.set_default_proxy(socks.SOCKS5, "localhost", tor_proxy_port)
        socket.socket = socks.socksocket

        self.session = requests.session()
        self.session.proxies = {
            'http': f'socks5h://localhost:{tor_proxy_port}',
            'https': f'socks5h://localhost:{tor_proxy_port}'
        }

    def check_tor_connection(self):
        """Verifiera Tor-anslutning"""
        try:
            response = self.session.get('https://check.torproject.org/', timeout=10)
            if 'Congratulations' in response.text:
                print("✅ Ansluten till Tor-nätverket")
                return True
            else:
                print("❌ INTE ansluten till Tor!")
                return False
        except Exception as e:
            print(f"❌ Fel: {e}")
            return False

    def search_paste_sites(self, keyword):
        """Sök efter läckta data på paste-sajter (clearnet)"""

        print(f"🔍 Söker efter '{keyword}' på paste-sajter...\n")

        # Använd clearnet paste-aggregerare
        results = []

        # Example: Psbdmp.ws (clearnet paste aggregator)
        try:
            response = self.session.get(
                f'https://psbdmp.ws/api/search/{keyword}',
                timeout=10
            )

            if response.status_code == 200:
                data = response.json()
                results.extend(data.get('data', []))
                print(f"✅ Hittade {len(results)} resultat")

        except Exception as e:
            print(f"❌ Fel: {e}")

        return results

    def check_breach_databases(self, email):
        """Kolla om email finns i kända dataintrång (via HIBP API)"""

        print(f"🔍 Kollar breaches för: {email}\n")

        try:
            # Have I Been Pwned API
            response = requests.get(
                f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}',
                headers={'User-Agent': 'Security-Research-Tool'},
                timeout=10
            )

            if response.status_code == 200:
                breaches = response.json()
                print(f"❌ Email hittad i {len(breaches)} dataintrång:")
                for breach in breaches:
                    print(f"  - {breach['Name']} ({breach['BreachDate']})")
                return breaches

            elif response.status_code == 404:
                print("✅ Email inte hittad i kända breaches")
                return []

        except Exception as e:
            print(f"❌ Fel: {e}")
            return None

    def monitor_dark_web_marketplaces(self, keywords):
        """
        Övervaka dark web marketplaces för företagets data
        OBS: Detta är endast för illustration - verklig implementation
        kräver specifika onion-adresser och access
        """

        print(f"🔍 Övervakar dark web för: {keywords}\n")

        # I verkligheten skulle du använda specifika .onion-adresser
        # och autentisering för olika marketplaces

        print("⚠️  Detta kräver access till specifika dark web-resurser")
        print("⚠️  Använd endast för legitim säkerhetsforskning!")

        # Pseudo-kod för illustration
        findings = []

        # Exempel-struktur (inte faktisk implementation)
        monitored_sites = [
            # '.onion-addresses skulle listas här'
        ]

        return findings

# Användning (endast för legitim säkerhetsforskning!)
if __name__ == "__main__":
    # OBS: Kräver att Tor körs lokalt (Tor Browser eller Tor daemon)

    osint = DarkWeb_OSINT()

    if osint.check_tor_connection():
        # Exempel: Kolla breaches
        osint.check_breach_databases("test@example.com")

        # Exempel: Sök paste-sajter
        osint.search_paste_sites("example.com")
```

---

## 7. Case Studies: Verkliga Undersökningar

### 📰 Case Study 1: Bellingcat MH17-undersökningen

**Bakgrund:**
Malaysia Airlines Flight 17 sköts ner över Ukraina 2014. Bellingcat använde OSINT för att identifiera ansvariga.

**OSINT-tekniker som användes:**

1. **Social Media Analysis**
   - Analyserade tusentals VK (ryska Facebook) inlägg
   - Geolokalisering av foton och videos
   - Tidsstämpling av innehåll

2. **Satellite Imagery**
   - Google Earth historisk imagery
   - Kommersiell satellit-data
   - Korrelering med video-bevis

3. **Vehicle Tracking**
   - Identifierade specifik BUK-missile launcher
   - Spårade transport genom Ryssland och Ukraina
   - Matchade fordon med registreringsnummer

4. **Metadata Analysis**
   - EXIF-data från foton
   - GPS-koordinater
   - Tidszoner och timestamps

**Python-verktyg för liknande analys:**

```python
import exifread
from geopy.geocoders import Nominatim
from datetime import datetime
import json

class MH17_Style_Analysis:
    """OSINT-analys inspirerad av Bellingcat MH17-metodik"""

    def __init__(self):
        self.geolocator = Nominatim(user_agent="osint_training")
        self.evidence = []

    def extract_photo_metadata(self, image_path):
        """Extrahera EXIF-data från foto"""

        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f, details=True)

        metadata = {}

        # Extrahera GPS-data
        if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
            lat = self.convert_to_degrees(tags['GPS GPSLatitude'].values)
            lon = self.convert_to_degrees(tags['GPS GPSLongitude'].values)

            # Konvertera till decimalgrader
            if tags['GPS GPSLatitudeRef'].values[0] == 'S':
                lat = -lat
            if tags['GPS GPSLongitudeRef'].values[0] == 'W':
                lon = -lon

            metadata['gps'] = {'lat': lat, 'lon': lon}

            # Reverse geocoding
            location = self.geolocator.reverse(f"{lat}, {lon}")
            metadata['location'] = location.address

        # Extrahera tidsinformation
        if 'EXIF DateTimeOriginal' in tags:
            metadata['timestamp'] = str(tags['EXIF DateTimeOriginal'])

        # Extrahera kamerainformation
        if 'Image Make' in tags:
            metadata['camera_make'] = str(tags['Image Make'])
        if 'Image Model' in tags:
            metadata['camera_model'] = str(tags['Image Model'])

        return metadata

    def convert_to_degrees(self, value):
        """Konvertera GPS-koordinater till decimalgrader"""
        d = float(value[0].num) / float(value[0].den)
        m = float(value[1].num) / float(value[1].den)
        s = float(value[2].num) / float(value[2].den)
        return d + (m / 60.0) + (s / 3600.0)

    def analyze_social_media_post(self, post_data):
        """Analysera social media-inlägg"""

        analysis = {
            'timestamp': post_data.get('timestamp'),
            'author': post_data.get('author'),
            'location': post_data.get('location'),
            'content': post_data.get('text'),
            'media': []
        }

        # Analysera bifogade bilder
        for image in post_data.get('images', []):
            metadata = self.extract_photo_metadata(image)
            analysis['media'].append(metadata)

        # Korrelera med andra bevis
        self.correlate_evidence(analysis)

        return analysis

    def correlate_evidence(self, new_evidence):
        """Korrelera nytt bevis med befintlig data"""

        # Kolla tidsmässig närhet
        for existing in self.evidence:
            if 'timestamp' in new_evidence and 'timestamp' in existing:
                # Beräkna tidsskillnad
                # Pseudo-kod för korrelering
                pass

        self.evidence.append(new_evidence)

    def generate_timeline(self):
        """Generera tidslinje av händelser"""

        timeline = sorted(
            self.evidence,
            key=lambda x: x.get('timestamp', '')
        )

        print("\n📅 TIDSLINJE:")
        print("="*60)
        for event in timeline:
            print(f"{event.get('timestamp')} - {event.get('location', 'Unknown')}")
            print(f"  {event.get('content', '')}\n")

        return timeline

# Användning
analyzer = MH17_Style_Analysis()

# Analysera bevis
photo_metadata = analyzer.extract_photo_metadata('evidence_photo.jpg')
print(f"📍 Foto taget på: {photo_metadata.get('location')}")
print(f"🕐 Tidpunkt: {photo_metadata.get('timestamp')}")
```

### 🏢 Case Study 2: Fortune 500 Penetration Test

**Scenario:**
Extern penetration test av ett Fortune 500-företag (anonymiserat).

**Fas 1: Reconnaissance (2 veckor)**

```python
import sublist3r
import whois
import dns.resolver
import shodan

class Fortune500_Recon:
    """Reconnaissance mot enterprise-mål"""

    def __init__(self, target_domain, shodan_api_key):
        self.domain = target_domain
        self.shodan = shodan.Shodan(shodan_api_key)
        self.findings = {
            'subdomains': [],
            'ip_addresses': [],
            'technologies': [],
            'vulnerabilities': []
        }

    def passive_subdomain_enum(self):
        """Passiv subdomain enumeration"""

        print(f"🔍 Enumererar subdomains för {self.domain}...\n")

        # Använd Sublist3r
        subdomains = sublist3r.main(
            self.domain,
            threads=40,
            savefile=None,
            ports=None,
            silent=True,
            verbose=False,
            enable_bruteforce=False,
            engines=None
        )

        self.findings['subdomains'] = subdomains
        print(f"✅ Hittade {len(subdomains)} subdomains")

        return subdomains

    def dns_reconnaissance(self):
        """DNS reconnaissance"""

        print(f"\n🔍 DNS reconnaissance för {self.domain}...\n")

        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA']

        for record_type in record_types:
            try:
                answers = dns.resolver.resolve(self.domain, record_type)
                print(f"{record_type} Records:")
                for rdata in answers:
                    print(f"  {rdata}")

                    # Spara IP-adresser
                    if record_type in ['A', 'AAAA']:
                        self.findings['ip_addresses'].append(str(rdata))

            except Exception as e:
                continue

    def shodan_reconnaissance(self):
        """Shodan reconnaissance på identifierade IPs"""

        print(f"\n🔍 Shodan reconnaissance...\n")

        for ip in self.findings['ip_addresses']:
            try:
                host = self.shodan.host(ip)

                print(f"\nIP: {ip}")
                print(f"Organization: {host.get('org', 'N/A')}")
                print(f"Operating System: {host.get('os', 'N/A')}")

                print(f"Ports: {host.get('ports', [])}")

                for item in host['data']:
                    print(f"\n  Port: {item['port']}")
                    print(f"  Service: {item.get('product', 'Unknown')}")

                    # Kolla efter sårbarheter
                    if 'vulns' in item:
                        for cve in item['vulns']:
                            self.findings['vulnerabilities'].append({
                                'ip': ip,
                                'port': item['port'],
                                'cve': cve
                            })
                            print(f"  🚨 Vulnerability: {cve}")

            except shodan.APIError as e:
                print(f"Error: {e}")

    def employee_enumeration(self):
        """Enumerate employees (via LinkedIn, ethical)"""

        print(f"\n🔍 Employee enumeration för {self.domain}...\n")

        # Detta skulle använda LinkedIn API eller liknande
        # För illustration endast
        print("⚠️  Använd LinkedIn Sales Navigator eller liknande verktyg")
        print("⚠️  Samla information om:")
        print("  - Jobbroller (developers, admins, security)")
        print("  - Email-format (firstname.lastname@company.com)")
        print("  - Teknologier som används (från jobblistor)")

    def technology_fingerprinting(self):
        """Identifiera teknologier som används"""

        print(f"\n🔍 Technology fingerprinting...\n")

        # Använd Wappalyzer, BuiltWith, eller liknande
        # Pseudo-kod:
        technologies = [
            'Web Server: nginx',
            'Framework: React',
            'CDN: Cloudflare',
            'Analytics: Google Analytics',
            'CMS: WordPress'
        ]

        self.findings['technologies'] = technologies

        for tech in technologies:
            print(f"  {tech}")

    def generate_report(self):
        """Generera reconnaissance-rapport"""

        print("\n" + "="*60)
        print("📊 RECONNAISSANCE REPORT")
        print("="*60)
        print(f"Target: {self.domain}\n")

        print(f"Subdomains discovered: {len(self.findings['subdomains'])}")
        print(f"IP addresses: {len(self.findings['ip_addresses'])}")
        print(f"Vulnerabilities found: {len(self.findings['vulnerabilities'])}\n")

        if self.findings['vulnerabilities']:
            print("🚨 CRITICAL FINDINGS:")
            for vuln in self.findings['vulnerabilities'][:5]:  # Top 5
                print(f"  {vuln['ip']}:{vuln['port']} - {vuln['cve']}")

        # Spara till fil
        with open(f'recon_report_{self.domain}.json', 'w') as f:
            json.dump(self.findings, f, indent=2)

        print(f"\n✅ Full rapport sparad: recon_report_{self.domain}.json")

# Användning
recon = Fortune500_Recon('target-company.com', 'shodan-api-key')
recon.passive_subdomain_enum()
recon.dns_reconnaissance()
recon.shodan_reconnaissance()
recon.employee_enumeration()
recon.technology_fingerprinting()
recon.generate_report()
```

**Resultat från verkligt pentest:**
- **Fynd:** 127 subdomains, varav 15 var föråldrade dev/staging-miljöer
- **Kritiskt:** 3 staging-servrar med default credentials
- **Högrisk:** 8 servrar med outdated software (kända CVEs)
- **Rekommendationer:** Asset inventory, decommissioning process, patch management

---

## 8. Övningar

### 📝 Övning 5.1: AI-driven OSINT Pipeline

**Uppgift:**
Skapa en komplett AI-driven OSINT pipeline som analyserar ett målföretag.

**Steg:**
1. Samla in data från flera källor (web, social media, paste sites)
2. Använd LLM för att analysera och sammanfatta fynd
3. Identifiera säkerhetsrisker automatiskt
4. Generera executive summary-rapport

**Leverabler:**
- Python-skript för automatiserad datainsamling
- LLM-integration för analys
- PDF-rapport med fynd och rekommendationer

**Tips:**
- Använd OpenAI API eller lokal LLM (Ollama)
- Kombinera med traditional OSINT-verktyg
- Validera AI-genererade resultat manuellt

---

### 📝 Övning 5.2: CI/CD Security Pipeline

**Uppgift:**
Implementera en komplett säkerhetspipeline i Jenkins/GitLab.

**Requirements:**
1. Automatisk OWASP ZAP scan vid varje deploy
2. Fail pipeline om kritiska sårbarheter hittas
3. Automatiska notifications till security team
4. Historisk tracking av sårbarheter

**Leverabler:**
- Jenkinsfile eller `.gitlab-ci.yml`
- ZAP scan-konfiguration
- Notification setup (email/Slack)
- Dashboard för sårbarhetstrend

---

### 📝 Övning 5.3: Multi-Cloud Security Audit

**Uppgift:**
Utför säkerhetsgranskning över AWS, Azure och GCP.

**Scope:**
- Storage (S3, Blob Storage, Cloud Storage)
- Compute (EC2, VM, Compute Engine)
- IAM och access control
- Network security groups

**Leverabler:**
- Unified Python script som granskar alla tre cloud-providers
- JSON-rapport med alla fynd
- Prioriterad åtgärdslista
- Compliance check (CIS Benchmarks)

---

### 📝 Övning 5.4: GraphQL Penetration Test

**Uppgift:**
Utför komplett penetration test av en GraphQL API.

**Test cases:**
1. Introspection queries
2. Batch query attacks
3. Query depth/complexity attacks
4. Field-level authorization bypass
5. Injection attacks (SQLi, XSS via GraphQL)

**Target:** https://demo.saleor.io/graphql/ (testmål)

**Leverabler:**
- Python test suite
- Detaljerad rapport med PoC för varje fynd
- Rekommendationer för säkring

---

### 📝 Övning 5.5: Kubernetes Cluster Hardening

**Uppgift:**
Audita och härda ett Kubernetes-kluster enligt best practices.

**Checklist:**
1. Pod Security Standards
2. Network Policies
3. RBAC configuration
4. Secrets management
5. Ingress security

**Leverabler:**
- Audit script (Python med kubernetes library)
- Före/efter säkerhetsjämförelse
- Hardening playbook (Ansible/kubectl commands)
- Dokumentation av ändringar

---

### 📝 Övning 5.6: Dark Web Monitoring System

**Uppgift:**
Bygg ett system för att övervaka dark web för företagets data.

**Features:**
1. Tor-integration för .onion-sites
2. Paste site monitoring
3. Breach database checking (HIBP)
4. Automated alerts vid fynd
5. Dashboard för visualisering

**Leverabler:**
- Python monitoring system
- Database för lagring av fynd
- Alert mechanism (email/Slack)
- Web dashboard (Flask/Django)

**⚠️ Etisk not:** Använd endast på autoriserade mål och för legitim säkerhetsforskning!

---

### 📝 Övning 5.7: Real-time Threat Intelligence Platform

**Uppgift:**
Skapa en threat intelligence-plattform som aggregerar data från flera källor.

**Källor:**
1. AlienVault OTX
2. VirusTotal
3. AbuseIPDB
4. Shodan
5. Custom feeds

**Features:**
- Real-time IP reputation checking
- Domain/URL analysis
- File hash lookup
- IoC (Indicators of Compromise) tracking
- Integration med SIEM

**Leverabler:**
- Python API aggregator
- REST API för queries
- Web interface
- SIEM integration (Splunk/ELK)

---

### 📝 Övning 5.8: Automated Remediation System

**Uppgift:**
Bygg ett system som automatiskt åtgärdar vanliga säkerhetsproblem.

**Scope:**
1. Automatisk patching av kända CVEs
2. Auto-remediation av ZAP-fynd
3. Config drift detection och correction
4. Automated firewall rule updates

**Workflow:**
```
Scan → Detect → Prioritize → Remediate → Verify → Report
```

**Leverabler:**
- Remediation engine (Python)
- Playbooks för olika sårbarhetskategorier
- Rollback mechanism
- Audit log

---

## 9. Stort Projekt: Enterprise Security Pipeline

### 🎯 Projektbeskrivning

Skapa en komplett enterprise-grade security assessment pipeline som kombinerar alla tekniker från nivå 1-5.

### 📋 Projektspecifikation

**Mål:**
Bygg ett automatiserat system som kan:
1. Utföra fullständig OSINT-reconnaissance
2. Scanna webapplikationer (ZAP)
3. Audita cloud-infrastruktur (AWS/Azure/GCP)
4. Testa APIs (REST/GraphQL)
5. Scanna containers och Kubernetes
6. Generera executive-level rapporter

**Arkitektur:**

```
┌─────────────────────────────────────────────────────┐
│           Security Assessment Platform               │
├─────────────────────────────────────────────────────┤
│                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────┐ │
│  │    OSINT     │  │   ZAP Scan   │  │  Cloud    │ │
│  │   Module     │  │    Module    │  │  Audit    │ │
│  └──────────────┘  └──────────────┘  └───────────┘ │
│                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────┐ │
│  │  API Test    │  │  Container   │  │    K8s    │ │
│  │   Module     │  │   Scanner    │  │   Audit   │ │
│  └──────────────┘  └──────────────┘  └───────────┘ │
│                                                      │
│  ┌──────────────────────────────────────────────┐  │
│  │         Correlation & Analysis Engine        │  │
│  │              (AI-powered)                   │  │
│  └──────────────────────────────────────────────┘  │
│                                                      │
│  ┌──────────────────────────────────────────────┐  │
│  │            Reporting & Dashboard              │  │
│  └──────────────────────────────────────────────┘  │
│                                                      │
└─────────────────────────────────────────────────────┘
```

**Teknisk Stack:**
- **Backend:** Python 3.11+
- **Web Framework:** FastAPI
- **Database:** PostgreSQL + Redis
- **Task Queue:** Celery
- **Frontend:** React + TypeScript
- **Deployment:** Docker + Kubernetes
- **CI/CD:** GitLab CI

**Kod-struktur:**

```
security-assessment-platform/
├── backend/
│   ├── api/
│   │   ├── routers/
│   │   │   ├── osint.py
│   │   │   ├── scanning.py
│   │   │   ├── cloud.py
│   │   │   └── reports.py
│   │   └── main.py
│   ├── modules/
│   │   ├── osint/
│   │   │   ├── subdomain_enum.py
│   │   │   ├── social_media.py
│   │   │   └── shodan_api.py
│   │   ├── scanning/
│   │   │   ├── zap_scanner.py
│   │   │   ├── api_tester.py
│   │   │   └── container_scanner.py
│   │   └── cloud/
│   │       ├── aws_auditor.py
│   │       ├── azure_auditor.py
│   │       └── gcp_auditor.py
│   ├── ai/
│   │   ├── llm_analyzer.py
│   │   ├── ml_prioritizer.py
│   │   └── correlation_engine.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.tsx
│   └── package.json
├── docker-compose.yml
├── Dockerfile
└── README.md
```

### 💻 Core Implementation

**main.py (FastAPI Backend):**

```python
from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uuid
from datetime import datetime

app = FastAPI(title="Security Assessment Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AssessmentRequest(BaseModel):
    target: str
    scope: list[str]  # ['osint', 'web', 'cloud', 'api', 'container']
    depth: str  # 'quick', 'standard', 'comprehensive'

class AssessmentResponse(BaseModel):
    assessment_id: str
    status: str
    created_at: datetime

@app.post("/api/assessments", response_model=AssessmentResponse)
async def create_assessment(request: AssessmentRequest, background_tasks: BackgroundTasks):
    """Skapa ny säkerhetsbedömning"""

    assessment_id = str(uuid.uuid4())

    # Starta bakgrundsprocesser för varje scope
    for scope_item in request.scope:
        if scope_item == 'osint':
            background_tasks.add_task(run_osint_assessment, assessment_id, request.target)
        elif scope_item == 'web':
            background_tasks.add_task(run_web_scan, assessment_id, request.target)
        elif scope_item == 'cloud':
            background_tasks.add_task(run_cloud_audit, assessment_id, request.target)
        # ... etc

    return AssessmentResponse(
        assessment_id=assessment_id,
        status="running",
        created_at=datetime.now()
    )

@app.get("/api/assessments/{assessment_id}")
async def get_assessment_status(assessment_id: str):
    """Hämta status för bedömning"""
    # Implementera databas-lookup
    pass

@app.get("/api/assessments/{assessment_id}/report")
async def get_assessment_report(assessment_id: str):
    """Generera och hämta rapport"""
    # Generera PDF/HTML-rapport
    pass

# Background task functions
async def run_osint_assessment(assessment_id: str, target: str):
    from modules.osint.subdomain_enum import SubdomainEnumerator
    from modules.osint.shodan_api import ShodanRecon

    # Run OSINT modules
    pass

async def run_web_scan(assessment_id: str, target: str):
    from modules.scanning.zap_scanner import ZAPScanner

    # Run ZAP scan
    pass

async def run_cloud_audit(assessment_id: str, target: str):
    from modules.cloud.aws_auditor import AWS_SecurityAuditor

    # Run cloud audit
    pass
```

**docker-compose.yml:**

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/security_db
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis
    volumes:
      - ./backend:/app

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend

  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=security_db
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  celery_worker:
    build: ./backend
    command: celery -A tasks worker --loglevel=info
    depends_on:
      - redis
      - db

  zap:
    image: owasp/zap2docker-stable
    ports:
      - "8090:8090"
    command: zap.sh -daemon -host 0.0.0.0 -port 8090 -config api.key=your-api-key

volumes:
  postgres_data:
```

### 📊 Deliverables

1. **Fullständigt fungerande system** med alla modules
2. **Web dashboard** för att köra och övervaka assessments
3. **API-dokumentation** (Swagger/OpenAPI)
4. **Deployment guide** (Kubernetes manifests)
5. **Användarmanual** (svenska)
6. **Executive Summary-rapport** från verkligt test

### ✅ Acceptanskriterier

- [ ] Kan scanna 100+ subdomains på < 5 minuter
- [ ] ZAP-integration fungerar med alla scan-typer
- [ ] Cloud-audit täcker AWS, Azure och GCP
- [ ] AI-analys genererar användbara insights
- [ ] Rapporter genereras automatiskt i PDF/HTML
- [ ] Dashboard visar real-time progress
- [ ] System är horizontally scalable (Kubernetes)
- [ ] All data krypteras (at rest & in transit)
- [ ] Audit logs för alla åtgärder

---

## 🎓 Sammanfattning Nivå 5

Grattis! Du har nu nått expert-nivå inom OSINT och OWASP ZAP. Du behärskar:

✅ **AI-driven OSINT** - LLM-baserad analys och automation
✅ **CI/CD Security** - Jenkins, GitLab, GitHub Actions integration
✅ **Molnsäkerhet** - AWS, Azure, GCP auditing
✅ **Modern API Testing** - REST, GraphQL, gRPC
✅ **Container Security** - Docker, Kubernetes hardening
✅ **Dark Web OSINT** - Etisk monitoring och reconnaissance
✅ **Case Studies** - Verkliga undersökningar (Bellingcat, Fortune 500)
✅ **Enterprise Systems** - Skalbar säkerhetsplattform

### 🚀 Nästa Steg

1. **Certifieringar:**
   - OSCP (Offensive Security Certified Professional)
   - GWAPT (GIAC Web Application Penetration Tester)
   - GCIH (GIAC Certified Incident Handler)
   - AWS/Azure Security Certifications

2. **Fortsatt Lärande:**
   - Bug Bounty Programs (HackerOne, Bugcrowd)
   - CTF Competitions (Hack The Box, TryHackMe)
   - Open Source Contributions (OWASP projects)
   - Security Research & Publications

3. **Karriärvägar:**
   - Senior Penetration Tester
   - Security Architect
   - Application Security Engineer
   - Security Researcher
   - Red Team Lead

---

## 📚 Avancerade Resurser

**Böcker:**
- "The Hacker Playbook 3" - Peter Kim
- "Real-World Bug Hunting" - Peter Yaworski
- "Practical Cloud Security" - Chris Dotson

**Plattformar:**
- HackerOne Bug Bounty
- Bugcrowd
- Synack
- YesWeHack (Europa)

**Communities:**
- OWASP Chapters (Sverige: Stockholm, Göteborg, Malmö)
- Null Byte
- r/netsec
- Discord: TryHackMe, Hack The Box

**Konferenser:**
- DEF CON
- Black Hat
- RSA Conference
- Nordic Security Conference

---

**🎯 Du är nu redo att ta dig an verkliga säkerhetsutmaningar på expertsnivå!**

*Kom ihåg: Med stor kunskap kommer stort ansvar. Använd alltid dina färdigheter etiskt och lagligt.* ⚖️
