import spacy
import pandas as pd

nlp = spacy.load("en_core_web_trf")

# Function to detect and redact unstructured sensitive data
def ner_method(text):
    sensitive_texts = nlp(text)
    sanitizer_text = text
    for sensitive in sensitive_texts.ents:
        sanitizer_text = sanitizer_text.replace(sensitive.text, "[SENSITIVE]")
    return sanitizer_text
