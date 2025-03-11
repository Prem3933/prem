from transformers import pipeline

summarizer = pipeline("summarization")
from transformers import pipeline

# Load a smaller, efficient model explicitly
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Example text to summarize
text = "Artificial Intelligence is a field that focuses on creating intelligent machines that can perform tasks typically requiring human intelligence."

# Generate summary
summary = summarizer(text, max_length=50, min_length=20, do_sample=False)
print(summary)
