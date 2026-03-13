<div align="center">
<br/>

```
███████╗ ██████╗ ██████╗ ███╗   ██╗ ██████╗ ███╗   ███╗██╗ ██████╗    ██████╗ ██╗   ██╗██╗     ███████╗███████╗
██╔════╝██╔════╝██╔═══██╗████╗  ██║██╔═══██╗████╗ ████║██║██╔════╝    ██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
█████╗  ██║     ██║   ██║██╔██╗ ██║██║   ██║██╔████╔██║██║██║         ██████╔╝██║   ██║██║     ███████╗█████╗  
██╔══╝  ██║     ██║   ██║██║╚██╗██║██║   ██║██║╚██╔╝██║██║██║         ██╔═══╝ ██║   ██║██║     ╚════██║██╔══╝  
███████╗╚██████╗╚██████╔╝██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║╚██████╗    ██║     ╚██████╔╝███████╗███████║███████╗
╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝    ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝
```

<h3>— Real-Time Financial News & Market Sentiment Pipeline —</h3>

<br/>

[![Python](https://img.shields.io/badge/Python-3.12-FFD43B?style=flat-square&logo=python&logoColor=black)](https://python.org)
[![Kafka](https://img.shields.io/badge/Apache_Kafka-7.3.0-000000?style=flat-square&logo=apache-kafka&logoColor=white)](https://kafka.apache.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![NLP](https://img.shields.io/badge/NLP-TextBlob-5C3EE8?style=flat-square)](https://textblob.readthedocs.io)

<br/>

> *A production-grade, containerised data pipeline that ingests live financial news, scores headline sentiment using NLP, correlates it against real-time stock market data, and surfaces everything on an auto-refreshing terminal-style dashboard.*

<br/>

</div>

---

<br/>

## `>_ OVERVIEW`

Economic Pulse is an end-to-end streaming data engineering project built from scratch. It demonstrates the full lifecycle of a real-time data pipeline — from ingestion, to transport, to processing, to visualisation — using industry-standard tools.

Every 5 minutes, the system automatically:

- Pulls the **10 latest economy headlines** from NewsAPI
- Fetches live **S&P 500** and **FTSE 100** prices from Yahoo Finance
- Publishes all data to **Apache Kafka** topics
- Consumes and scores each headline with **TextBlob NLP** (polarity: -1.0 → +1.0)
- Persists structured records to **PostgreSQL**
- Renders everything on a **Streamlit dashboard** that auto-refreshes every 30 seconds

<br/>

---

<br/>

## `>_ ARCHITECTURE`

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           ECONOMIC PULSE PIPELINE                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   DATA SOURCES          TRANSPORT            PROCESSING        STORAGE      │
│                                                                             │
│   ┌──────────┐          ┌─────────┐          ┌───────────┐   ┌──────────┐  │
│   │ NewsAPI  │─────────▶│  Kafka  │─────────▶│    NLP    │──▶│Postgres  │  │
│   │          │          │  topic: │          │ Sentiment │   │          │  │
│   │ 10 live  │          │  "news" │          │ Analysis  │   │  news    │  │
│   │ headlines│          └─────────┘          │           │   │  stocks  │  │
│   └──────────┘                               │ TextBlob  │   └────┬─────┘  │
│                          ┌─────────┐         │ polarity  │        │        │
│   ┌──────────┐           │  Kafka  │─────────▶  score    │        │        │
│   │  Yahoo   │──────────▶│  topic: │          └───────────┘        │        │
│   │ Finance  │           │"stocks" │                               ▼        │
│   │ S&P FTSE │           └─────────┘                        ┌──────────┐   │
│   └──────────┘                                              │Streamlit │   │
│                                                             │Dashboard │   │
│                                                             └──────────┘   │
│                                                                             │
│   fetcher.py ──────────────────────────▶ processor.py ──────▶ dashboard.py │
└─────────────────────────────────────────────────────────────────────────────┘
```

<br/>

---

<br/>

## `>_ TECH STACK`

<br/>

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Ingestion** | `yfinance` · `newsapi-python` | Pull live stock prices and news headlines |
| **Transport** | `Apache Kafka 7.3.0` · `Zookeeper` | Fault-tolerant real-time message streaming |
| **Processing** | `TextBlob` · `kafka-python` | NLP sentiment scoring, message consumption |
| **Storage** | `PostgreSQL 15` · `psycopg2` | Structured persistent data store |
| **Presentation** | `Streamlit` · `Pandas` | Live auto-refreshing dashboard |
| **Infrastructure** | `Docker` · `Docker Compose` | Fully containerised, portable deployment |
| **Language** | `Python 3.12` | End-to-end pipeline logic |

<br/>

---

<br/>

## `>_ PROJECT STRUCTURE`

```
economic-pulse/
│
├── docker-compose.yml          # Spins up Kafka, Zookeeper & PostgreSQL
│
├── fetcher/
│   └── fetcher.py              # Kafka producer — fetches news & stock data
│
├── processor/
│   └── processor.py            # Kafka consumer — NLP scoring & DB writes
│
├── dashboard/
│   └── dashboard.py            # Streamlit live dashboard
│
└── README.md
```

<br/>

---

<br/>

## `>_ GETTING STARTED`

<br/>

**Prerequisites**
- Docker & Docker Compose
- Python 3.10+
- Free API key from [newsapi.org](https://newsapi.org)

<br/>

**Step 1 — Clone**
```bash
git clone https://github.com/Saif14061/economic-pulse.git
cd economic-pulse
```

**Step 2 — Install dependencies**
```bash
pip install kafka-python newsapi-python yfinance textblob psycopg2-binary streamlit pandas
```

**Step 3 — Start infrastructure**
```bash
docker-compose up -d
```

**Step 4 — Run the pipeline** *(3 terminals)*
```bash
# Terminal 1 — ingest data
python3 fetcher/fetcher.py

# Terminal 2 — process & store
python3 processor/processor.py

# Terminal 3 — launch dashboard
streamlit run dashboard/dashboard.py
```

**Step 5 — Open dashboard**
```
http://localhost:8501
```

<br/>

---

<br/>

## `>_ DASHBOARD`

```
┌──────────────────────────────────────────────────────────────────────┐
│  FINANCIAL NEWS TRACKER                                              │
├──────────────────────┬──────────────────────┬────────────────────────┤
│   S&P 500            │   FTSE 100           │   Market Sentiment     │
│   6,655.67           │   10,261.15          │   neutral              │
├──────────────────────┴──────────────────────┴────────────────────────┤
│  LATEST HEADLINES                 │  SENTIMENT DISTRIBUTION          │
│  ────────────────                 │  ──────────────────────          │
│  Headline 1 · Wired  🔴 negative  │                                  │
│  Headline 2 · BBC    ⚪ neutral   │  negative  [████████]  ~35%      │
│  Headline 3 · CNBC   🟢 positive  │  neutral   [████████]  ~45%      │
│  Headline 4 · WSJ    🟢 positive  │  positive  [██████  ]  ~20%      │
│  ...                              │                                  │
├───────────────────────────────────┴──────────────────────────────────┤
│  STOCK PRICES                                                        │
│  S&P500    6655.67    2026-03-13 17:18:11                            │
│  FTSE100   10261.15   2026-03-13 17:18:11                            │
└──────────────────────────────────────────────────────────────────────┘
  auto-refreshes every 30 seconds
```

<br/>

---

<br/>

## `>_ SENTIMENT SCORING`

Each headline is scored using **TextBlob polarity analysis**:

```
Score > 0.0  →  🟢  POSITIVE   "Markets surge to record highs"
Score = 0.0  →  ⚪  NEUTRAL    "Fed meets Wednesday to discuss rates"  
Score < 0.0  →  🔴  NEGATIVE   "Recession fears grip Wall Street"
```

> Scores range from **-1.0** (most negative) to **+1.0** (most positive)

<br/>



<br/>

<div align="center">

```
built by SAIF ABBAS· MAR 13 · 2026


