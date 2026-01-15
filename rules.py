from utils import extract_urls, extract_domain, contains_urgent_language, has_ip_url, is_unknown_domain


def analyze_text(text: str) -> dict:
    score = 0
    reasons = []

    urls = extract_urls(text)

    if contains_urgent_language(text):
        score += 2
        reasons.append("Email contains urgent or threatening language")
    if has_ip_url(urls):
        score += 3
        reasons.append("Email contains URL with IP address instead od domain")

    for url in urls:
        domain = extract_domain(url)
        if is_unknown_domain(domain):
            score += 2
            reasons.append(f"URL domain {domain} is not in known trusted domains")
            break

    return {"score": score, "reasons": reasons}
