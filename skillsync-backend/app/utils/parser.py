import textract, os, spacy
from typing import Dict, Any
nlp = spacy.load("en_core_web_sm")
DEFAULT_SKILLS = [
    "python", "java", "c++", "sql", "postgresql", "javascript", "react", "node", "docker",
    "aws", "azure", "git", "linux", "tensorflow", "pytorch", "nlp", "machine learning"
]
def extract_text_from_file(filepath: str) -> str:
    text = textract.process(filepath).decode("utf-8", errors="ignore")
    return text
def parse_resume_text(text: str) -> Dict[str, Any]:
    doc = nlp(text)
    tokens = [t.text.lower() for t in doc if not t.is_stop and not t.is_punct]
    words = set(tokens)
    found_skills = [s for s in DEFAULT_SKILLS if s in words]
    emails = [ent.text for ent in doc.ents if ent.label_ == "EMAIL"]
    parsed = {
        "skills": found_skills,
        "emails": emails,
        "text_length": len(text),
    }
    return parsed
