# Deployment Guide - Medical AI Agent (Python + FastAPI)

En komplett guide för att deploya din Medical AI Agent till produktion.

## 📋 Innehåll

1. [Deployment Options](#deployment-options)
2. [Railway Deployment](#railway-deployment-rekommenderat)
3. [Render Deployment](#render-deployment)
4. [Docker Deployment](#docker-deployment)
5. [AWS Deployment](#aws-deployment)
6. [Production Checklist](#production-checklist)
7. [Monitoring & Logging](#monitoring--logging)
8. [Scaling](#scaling)

---

## Deployment Options

### Jämförelse av Hosting Providers

| Provider | Kostnad | Setup | Scaling | Docker | GDPR | Rekommendation |
|----------|---------|-------|---------|--------|------|----------------|
| **Railway** | $5-20/mån | ⭐⭐⭐⭐⭐ | Auto | ✅ | EU available | ✅ Bäst för MVP |
| **Render** | $7-25/mån | ⭐⭐⭐⭐⭐ | Auto | ✅ | EU available | ✅ Bäst för MVP |
| **Fly.io** | $0-10/mån | ⭐⭐⭐⭐ | Manual | ✅ | EU available | Bra för small scale |
| **AWS** | Varierar | ⭐⭐⭐ | Manual | ✅ | ✅ | Enterprise |
| **Azure** | Varierar | ⭐⭐⭐ | Manual | ✅ | ✅ | Enterprise |
| **Heroku** | $7-25/mån | ⭐⭐⭐⭐⭐ | Auto | ✅ | EU available | Enkel men dyrare |

**Rekommendation:** Railway eller Render för MVP/small scale, AWS/Azure för enterprise.

---

## Railway Deployment (Rekommenderat)

Railway är perfekt för MVP - enkel setup, auto-deploy från Git, och rimlig kostnad.

### **Steg 1: Förberedelser**

#### 1.1 Skapa `Procfile`
```bash
# I medical-agent-python/
echo "web: uvicorn app.main:app --host 0.0.0.0 --port \$PORT" > Procfile
```

#### 1.2 Skapa `runtime.txt`
```bash
echo "python-3.11" > runtime.txt
```

#### 1.3 Uppdatera `requirements.txt`
Lägg till Gunicorn för production:
```bash
echo "gunicorn==21.2.0" >> requirements.txt
```

#### 1.4 Skapa `railway.json` (optional)
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### **Steg 2: Deploy till Railway**

#### 2.1 Skapa Railway Account
1. Gå till https://railway.app/
2. Sign up med GitHub
3. Skapa nytt projekt: "New Project" → "Deploy from GitHub repo"

#### 2.2 Länka GitHub Repo
1. Välj ditt repo: `Victory-Redovisning`
2. Välj branch: `claude/eye-care-secretary-app-01Q3Z1r2G9zSVHZ9WTmGV2ZG`
3. Root directory: `medical-agent-python`

#### 2.3 Konfigurera Environment Variables
I Railway dashboard → Variables:

```bash
ANTHROPIC_API_KEY=sk-ant-xxx
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_ANON_KEY=eyJxxx
SUPABASE_SERVICE_KEY=eyJxxx
SUPABASE_DB_PASSWORD=xxx
ENVIRONMENT=production
LOG_LEVEL=INFO
PORT=8000
```

#### 2.4 Deploy!
Railway deployer automatiskt. Vänta ~2-3 minuter.

### **Steg 3: Custom Domain (Optional)**

1. I Railway dashboard → Settings
2. Lägg till custom domain: `api.your-domain.com`
3. Uppdatera DNS:
   ```
   Type: CNAME
   Name: api
   Value: xxx.railway.app
   ```

### **Steg 4: Testa Deployment**

```bash
# Health check
curl https://your-app.railway.app/health

# WebSocket test
wscat -c wss://your-app.railway.app/ws/test-session
```

---

## Render Deployment

Render är ett annat utmärkt alternativ med liknande features som Railway.

### **Steg 1: Förberedelser**

#### 1.1 Skapa `render.yaml`
```yaml
# medical-agent-python/render.yaml
services:
  - type: web
    name: medical-agent
    env: python
    region: frankfurt  # EU region för GDPR
    plan: starter  # $7/mån
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app.main:app --host 0.0.0.0 --port $PORT
    healthCheckPath: /health
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
      - key: ANTHROPIC_API_KEY
        sync: false
      - key: SUPABASE_URL
        sync: false
      - key: SUPABASE_ANON_KEY
        sync: false
      - key: SUPABASE_SERVICE_KEY
        sync: false
      - key: ENVIRONMENT
        value: production
```

### **Steg 2: Deploy**

1. Gå till https://render.com/
2. Sign up med GitHub
3. New → Web Service
4. Connect ditt repo
5. Settings:
   - **Root Directory:** `medical-agent-python`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. Lägg till environment variables
7. Deploy!

### **Steg 3: Auto-Deploy från Git**

Render deployer automatiskt när du pushar till branchen.

---

## Docker Deployment

För maximal kontroll och portabilitet.

### **Steg 1: Skapa Dockerfile**

```dockerfile
# medical-agent-python/Dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### **Steg 2: Skapa .dockerignore**

```
# medical-agent-python/.dockerignore
__pycache__
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv
.env
.git
.gitignore
.pytest_cache
*.log
model_cache/
```

### **Steg 3: Skapa docker-compose.yml**

```yaml
# medical-agent-python/docker-compose.yml
version: '3.8'

services:
  medical-agent:
    build: .
    ports:
      - "8000:8000"
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - SUPABASE_URL=${SUPABASE_URL}
      - SUPABASE_ANON_KEY=${SUPABASE_ANON_KEY}
      - SUPABASE_SERVICE_KEY=${SUPABASE_SERVICE_KEY}
      - ENVIRONMENT=production
      - LOG_LEVEL=INFO
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 3s
      retries: 3
      start_period: 40s

  # Optional: Nginx reverse proxy
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - medical-agent
    restart: unless-stopped
```

### **Steg 4: Build & Run**

```bash
# Build image
docker build -t medical-agent:latest .

# Run container
docker run -d \
  --name medical-agent \
  -p 8000:8000 \
  --env-file .env \
  medical-agent:latest

# Med docker-compose
docker-compose up -d

# View logs
docker logs -f medical-agent

# Stop
docker-compose down
```

### **Steg 5: Push till Docker Hub**

```bash
# Tag image
docker tag medical-agent:latest yourusername/medical-agent:latest

# Push
docker push yourusername/medical-agent:latest
```

---

## AWS Deployment

För enterprise-grade deployment med full kontroll.

### **Option 1: AWS Elastic Beanstalk (Enklast)**

#### 1. Install EB CLI
```bash
pip install awsebcli
```

#### 2. Initialize EB
```bash
cd medical-agent-python
eb init -p python-3.11 medical-agent --region eu-north-1
```

#### 3. Create Environment
```bash
eb create medical-agent-prod \
  --instance-type t3.medium \
  --region eu-north-1 \
  --envvars ANTHROPIC_API_KEY=xxx,SUPABASE_URL=xxx
```

#### 4. Deploy
```bash
eb deploy
```

#### 5. Open App
```bash
eb open
```

### **Option 2: AWS ECS + Fargate (Rekommenderat)**

#### 1. Push Docker Image till ECR
```bash
# Create ECR repository
aws ecr create-repository --repository-name medical-agent

# Login to ECR
aws ecr get-login-password --region eu-north-1 | \
  docker login --username AWS --password-stdin YOUR_ACCOUNT_ID.dkr.ecr.eu-north-1.amazonaws.com

# Tag and push
docker tag medical-agent:latest YOUR_ACCOUNT_ID.dkr.ecr.eu-north-1.amazonaws.com/medical-agent:latest
docker push YOUR_ACCOUNT_ID.dkr.ecr.eu-north-1.amazonaws.com/medical-agent:latest
```

#### 2. Skapa Task Definition
```json
{
  "family": "medical-agent",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "512",
  "memory": "1024",
  "containerDefinitions": [
    {
      "name": "medical-agent",
      "image": "YOUR_ACCOUNT_ID.dkr.ecr.eu-north-1.amazonaws.com/medical-agent:latest",
      "portMappings": [
        {
          "containerPort": 8000,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "ENVIRONMENT",
          "value": "production"
        }
      ],
      "secrets": [
        {
          "name": "ANTHROPIC_API_KEY",
          "valueFrom": "arn:aws:secretsmanager:eu-north-1:xxx:secret:medical-agent/anthropic-key"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/medical-agent",
          "awslogs-region": "eu-north-1",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ]
}
```

#### 3. Skapa ECS Service
```bash
aws ecs create-service \
  --cluster medical-agent-cluster \
  --service-name medical-agent-service \
  --task-definition medical-agent:1 \
  --desired-count 2 \
  --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={subnets=[subnet-xxx],securityGroups=[sg-xxx],assignPublicIp=ENABLED}"
```

#### 4. Setup Application Load Balancer
- Skapa ALB i AWS Console
- Target group → medical-agent ECS service
- Listener: HTTPS (port 443) → Target group
- SSL Certificate från AWS Certificate Manager

### **Option 3: AWS Lambda (Serverless)**

För WebSocket behövs API Gateway + Lambda - mer komplext men kan vara billigare för låg traffic.

**Rekommendation:** Använd ECS Fargate för production, Lambda för very low traffic.

---

## Production Checklist

### **Säkerhet**

- [ ] **HTTPS Only** - Tvinga SSL/TLS
  ```python
  # I app/main.py
  from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
  app.add_middleware(HTTPSRedirectMiddleware)
  ```

- [ ] **CORS Policy** - Begränsa till ditt frontend domain
  ```python
  app.add_middleware(
      CORSMiddleware,
      allow_origins=["https://your-frontend.com"],  # Inte "*"
      allow_credentials=True,
      allow_methods=["GET", "POST"],
      allow_headers=["*"],
  )
  ```

- [ ] **Rate Limiting** - Förhindra abuse
  ```bash
  pip install slowapi
  ```
  ```python
  from slowapi import Limiter, _rate_limit_exceeded_handler
  from slowapi.util import get_remote_address

  limiter = Limiter(key_func=get_remote_address)
  app.state.limiter = limiter
  app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

  @app.post("/sessions/start")
  @limiter.limit("5/minute")
  async def start_session(request: Request, ...):
      ...
  ```

- [ ] **API Keys** - Använd Secrets Manager (AWS Secrets Manager, Azure Key Vault)
  ```python
  import boto3

  def get_secret(secret_name):
      client = boto3.client('secretsmanager', region_name='eu-north-1')
      response = client.get_secret_value(SecretId=secret_name)
      return response['SecretString']

  ANTHROPIC_API_KEY = get_secret('medical-agent/anthropic-key')
  ```

- [ ] **Input Validation** - Redan gjort med Pydantic ✓
- [ ] **SQL Injection Protection** - Använd Supabase client ✓

### **Performance**

- [ ] **Caching** - Redis för RAG results
  ```bash
  pip install redis
  ```
  ```python
  import redis
  r = redis.Redis(host='localhost', port=6379, db=0)

  # Cache RAG results
  cached = r.get(f"disease_search:{symptoms_hash}")
  if cached:
      return json.loads(cached)
  ```

- [ ] **Connection Pooling** - För database
  ```python
  from sqlalchemy import create_engine
  from sqlalchemy.pool import QueuePool

  engine = create_engine(
      DATABASE_URL,
      poolclass=QueuePool,
      pool_size=20,
      max_overflow=0
  )
  ```

- [ ] **Async Operations** - Redan gjort ✓
- [ ] **Load Balancing** - Via AWS ALB eller Nginx

### **Monitoring**

- [ ] **Health Checks** - Redan implementerat ✓
- [ ] **Logging** - Structured logging
  ```python
  import logging
  import json

  class JSONFormatter(logging.Formatter):
      def format(self, record):
          return json.dumps({
              'timestamp': self.formatTime(record),
              'level': record.levelname,
              'message': record.getMessage(),
              'module': record.module
          })

  handler = logging.StreamHandler()
  handler.setFormatter(JSONFormatter())
  logger.addHandler(handler)
  ```

- [ ] **Error Tracking** - Sentry
  ```bash
  pip install sentry-sdk[fastapi]
  ```
  ```python
  import sentry_sdk
  from sentry_sdk.integrations.fastapi import FastApiIntegration

  sentry_sdk.init(
      dsn="https://xxx@xxx.ingest.sentry.io/xxx",
      integrations=[FastApiIntegration()],
      environment="production"
  )
  ```

- [ ] **Metrics** - Prometheus
  ```bash
  pip install prometheus-fastapi-instrumentator
  ```
  ```python
  from prometheus_fastapi_instrumentator import Instrumentator

  Instrumentator().instrument(app).expose(app)
  ```

### **Reliability**

- [ ] **Graceful Shutdown**
  ```python
  import signal
  import sys

  def signal_handler(sig, frame):
      logger.info("Shutting down gracefully...")
      # Cleanup resources
      sys.exit(0)

  signal.signal(signal.SIGTERM, signal_handler)
  ```

- [ ] **Retry Logic** - För external API calls
  ```bash
  pip install tenacity
  ```
  ```python
  from tenacity import retry, stop_after_attempt, wait_exponential

  @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
  async def call_anthropic_api(...):
      ...
  ```

- [ ] **Circuit Breaker** - För downstream services
  ```bash
  pip install pybreaker
  ```

- [ ] **Backup Strategy** - Supabase har auto-backup ✓

---

## Monitoring & Logging

### **Setup Sentry (Error Tracking)**

```python
# app/main.py
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    environment=os.getenv("ENVIRONMENT", "development"),
    integrations=[
        FastApiIntegration(),
        LoggingIntegration(level=logging.INFO, event_level=logging.ERROR)
    ],
    traces_sample_rate=0.1,  # 10% av requests
)
```

### **Setup CloudWatch (AWS)**

```python
import watchtower
import logging

logger = logging.getLogger(__name__)
logger.addHandler(watchtower.CloudWatchLogHandler(
    log_group='/medical-agent/production',
    stream_name='api-logs'
))
```

### **Custom Metrics**

```python
from prometheus_client import Counter, Histogram

# Metrics
transcription_counter = Counter('transcriptions_total', 'Total transcriptions processed')
agent_latency = Histogram('agent_processing_seconds', 'Agent processing time')

# Usage
@agent_latency.time()
async def process_transcription(self, text):
    transcription_counter.inc()
    ...
```

---

## Scaling

### **Horizontal Scaling**

#### Railway/Render
- Auto-scaling baserat på CPU/memory
- Settings → Scale → Enable auto-scaling

#### AWS ECS
```bash
# Auto-scaling policy
aws application-autoscaling register-scalable-target \
  --service-namespace ecs \
  --resource-id service/medical-agent-cluster/medical-agent-service \
  --scalable-dimension ecs:service:DesiredCount \
  --min-capacity 2 \
  --max-capacity 10

# CPU-based scaling
aws application-autoscaling put-scaling-policy \
  --policy-name medical-agent-cpu-scaling \
  --service-namespace ecs \
  --resource-id service/medical-agent-cluster/medical-agent-service \
  --scalable-dimension ecs:service:DesiredCount \
  --policy-type TargetTrackingScaling \
  --target-tracking-scaling-policy-configuration '{
    "TargetValue": 75.0,
    "PredefinedMetricSpecification": {
      "PredefinedMetricType": "ECSServiceAverageCPUUtilization"
    }
  }'
```

### **Database Scaling**

Supabase har auto-scaling. För custom PostgreSQL:
- Read replicas för läsoperationer
- Connection pooling (PgBouncer)
- Query optimization

### **Caching Strategy**

```python
# Redis för RAG results
import redis
from functools import wraps

redis_client = redis.Redis(host='localhost', port=6379)

def cache_rag_result(ttl=3600):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Generate cache key
            key = f"rag:{func.__name__}:{hash(str(args) + str(kwargs))}"

            # Check cache
            cached = redis_client.get(key)
            if cached:
                return json.loads(cached)

            # Call function
            result = await func(*args, **kwargs)

            # Cache result
            redis_client.setex(key, ttl, json.dumps(result))

            return result
        return wrapper
    return decorator

@cache_rag_result(ttl=3600)
async def search_diseases(symptoms):
    ...
```

---

## Kostnadsprojektioner

### **Railway/Render (Hobby/Starter)**
```
Base: $7-10/mån
Usage (500 req/dag): +$5/mån
Total: ~$15/mån
```

### **AWS (Production)**
```
ECS Fargate (2 tasks, t3.medium equivalent): $50/mån
ALB: $20/mån
RDS (db.t3.small): $30/mån
CloudWatch: $10/mån
Data transfer: $10/mån
Total: ~$120/mån
```

### **Supabase**
```
Pro plan: $25/mån (inkluderar database, vector storage, auth)
```

---

## Troubleshooting

### Problem: Container crashes on startup

**Lösning:**
```bash
# Check logs
docker logs medical-agent

# Check health
docker inspect medical-agent

# Common issues:
# 1. Missing environment variables
# 2. Port already in use
# 3. Out of memory
```

### Problem: Slow API responses

**Lösning:**
1. Check database queries
2. Enable caching
3. Use async operations
4. Profile code:
   ```bash
   pip install py-spy
   py-spy record -o profile.svg -- python -m uvicorn app.main:app
   ```

### Problem: High memory usage

**Lösning:**
```python
# Limit LLM context
Settings.context_window = 4096  # Mindre än default

# Clear cache periodically
import gc
gc.collect()
```

---

## Sammanfattning

**För MVP/Small Scale:**
✅ Använd Railway eller Render - enklast och snabbast

**För Production/Enterprise:**
✅ Använd AWS ECS Fargate eller Azure Container Apps - full kontroll

**Nästa steg:**
1. Välj hosting provider
2. Setup environment variables
3. Deploy!
4. Setup monitoring (Sentry)
5. Test i produktion
6. Enable auto-scaling

**Frågor?** Se [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)
