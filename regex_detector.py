import re

sensitive_texts = {
    "SSN": r"\b\d{3}-\d{2}-\d{4}\b",
    "Card Number": r"\b\d{4}-\d{4}-\d{4}-\d{4}\b",
    "Email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "Phone Number": r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b",
    "IP Address": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    "Transaction ID": r"\bTXN\d+\b",
    "Password": r"(?i)(?:password|pass|pwd)\s*[:=]\s*[^\s]+",
    "IBAN": r"\b[A-Z]{2}\d{2}\s\d{4}\s\d{4}\s\d{4}\s\d{4}\b",
    "Medical ID": r"\bMED\d{7}\b",
    "Vehicle Plate": r"\b[A-Z]{2}-\d{4}-[A-Z]{2}\b",
    "Tax ID": r"\b\d{2}-\d{7}\b",
    "API Key / Key": r"(?i)(?:api[_-]?key|secret|access[_-]?key|token)\s*[:=]\s*[^\s]+",
    "Account Number": r"\b\d{10,16}\b",
    "Routing Number": r"\b\d{9}\b",
    "Personal ID": r"\b(?:ID|PID|EMP)[-]?\d{4,12}\b"
}


# Function to mask detected sensitive information
def regex_method(text):
    sanitizer_text = text

    for sensitive in sensitive_texts.values():
        sanitizer_text = re.sub(sensitive, "[SENSITIVE]", sanitizer_text)
    return sanitizer_text
