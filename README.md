# Phishing Email Analyzer

## Overview
Phishing Email Analyzer is a lightweight, rule-based Python tool for performing initial triage of suspicious email messages.
The tool analyzes plain-text email content and highlights indicators commonly associated with phishing attempts, producing a risk score and human-readable explanations.

This project is intentionally designed to be:

- Explainable
- Auditable
- Deterministic
- Easy to extend

The analyzer does not attempt to automatically classify emails as malicious.
Instead, it assists analysts by identifying risk signals that warrant further investigation.

This tool supports early-stage triage by:

- Identifying common phishing patterns
- Prioritizing higher-risk emails
- Providing clear reasoning behind every finding

## Features
- Plain-text email analysis (.txt)
- URL extraction and inspection
- Detection of:
  - Urgent or threatening language
  - URLs containing IP addresses
  - Unknown or uncommon domains
- Simple, explainable risk scoring
- Command-line interface (CLI)
- Modular and extensible architecture

## Project Structure
```
phishing-email-analyzer/
├── analyzer.py # CLI entry point and workflow orchestration
├── rules.py # Rule-based detection logic
├── utils.py # Helper functions (URL parsing, text analysis)
├── examples/
│ └── sample_email.txt
└── README.md
```
Design rationale
- Separation of concerns – rules, utilities, and orchestration are isolated
- Audit-friendly – each rule is explicit and easy to review
- Extensible – new rules can be added without modifying core logic

### Usage
Requirements
- Python 3.10+
Run the analyzer
```
python analyzer.py examples/sample_email.txt
```

### Example output
```
Risk score: 5
Findings:
- Email contains urgent or threatening language
- Email contains URL with IP address instead of domain
- URL domain 'secure-login-example.ru' is not in known trusted domains
```

### Risk Scoring Model
Each detection rule contributes a configurable number of points to the total risk score.
The score represents relative risk, not certainty of malicious intent.
Example weighting:
<ins>Indicator	    Points </ins>
Urgent language	    2
IP address in URL	3
Unknown domain	    2

The scoring model is intentionally simple and transparent.

### Limitations
This tool is intended for initial triage only and has the following limitations:
- Does not parse email headers 
- Does not analyze attachments
- No domain reputation or DNS checks
- No machine learning
- No external APIs
- Rule-based detection only

These limitations are intentional to preserve:
- Offline usability
- Deterministic behavior
- Auditability

### Extensibility

The analyzer is designed to be easily extended.
Potential future enhancements include:
- Email header analysis
- TLD-based risk scoring
- Domain age heuristics
- JSON output for SIEM integration
- Unit tests and CI integration

### Disclaimer
This tool does not replace human analysis.
It provides indicators to support decision-making and prioritization.
Final assessment and response actions should always be performed by a qualified analyst.