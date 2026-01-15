import re
from urllib.parse import urlparse

URL_REGEX = re.compile(r"https?://[^\s]+", re.IGNORECASE)

KNOWN_DOMAINS = {
    "google.com",
    "microsoft.com",
    "apple.com",
    "amazon.com",
    "facebook.com",
    "paypal.com"
}


def extract_urls(text: str) -> list[str]:
    return URL_REGEX.findall(text)


def contains_urgent_language(text: str) -> bool:
    keywords = [
        "urgent",
        "immediatley",
        "your account will be suspended",
        "verify your account",
        "act now",
    ]
    lowered = text.lower()
    return any(keyword in lowered for keyword in keywords)


def has_ip_url(urls: list[str]) -> bool:
    ip_pattern = re.compile(r"https?://\d+\.\d+\.\d+\.\d+")
    return any(ip_pattern.match(url) for url in urls)

def extract_domain(url: str) -> str:
    parsed =urlparse(url)
    return parsed.hostname or ""

def is_unknown_domain(domain: str)->bool:
    if not domain:
        return False
    for known in KNOWN_DOMAINS:
        if domain.endswith(known):
            return False
    return True