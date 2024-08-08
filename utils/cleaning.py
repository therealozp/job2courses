from transformers import BertTokenizerFast, BertModel, pipeline
import torch
from sklearn.metrics.pairwise import cosine_similarity
import re
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('punkt')

tokenizer = BertTokenizerFast.from_pretrained("google-bert/bert-base-uncased")
model = BertModel.from_pretrained("google-bert/bert-base-uncased")
summarizer = pipeline("summarization", model="google-t5/t5-base", tokenizer="google-t5/t5-base", framework="pt")

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def remove_spaces(text):
    text = " ".join(text.split())
    text = text.strip()
    return text

def tokenize(text): 
    return tokenizer.encode_plus(text, add_special_tokens=True, max_length=512, truncation=True, return_tensors='pt')

def load_stopwords():
    with open('stopwords.txt') as f:
        stopwords = f.read().splitlines()
    return stopwords

def filter_stopwords(text):
    stop_words = set(load_stopwords())
    filtered_text = [word for word in text.split() if word not in stop_words]
    return ' '.join(filtered_text)

def lemmatize(text): 
    words = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

def preprocess_text(text):
    text = clean_text(text)
    text = filter_stopwords(text)
    # text = lemmatize(text)
    return text

def get_bert_embeddings(text):
    text = clean_text(text)
    tokenized_text = tokenize(text)
    with torch.no_grad():
        outputs = model(**tokenized_text)
        embeddings = outputs.last_hidden_state
        return embeddings

def get_bert_embeddings_sliding_window(text, max_length=510, stride=256, use_summary=False):
    text = clean_text(text)

    if use_summary:
        text = summarize(text)

    # Tokenize the text
    tokenized_text = tokenizer.encode_plus(text, add_special_tokens=True, return_tensors='pt')
    input_ids = tokenized_text['input_ids'].squeeze().tolist()
    attention_mask = tokenized_text['attention_mask'].squeeze().tolist()

    embeddings = []

    with torch.no_grad():
        for i in range(0, len(input_ids), stride):
            start = i
            end = min(i + max_length, len(input_ids))
            input_ids_chunk = input_ids[start:end]
            attention_mask_chunk = attention_mask[start:end]

            # Append [CLS] and [SEP] tokens if not already present
            if start == 0:
                input_ids_chunk = [tokenizer.cls_token_id] + input_ids_chunk
                attention_mask_chunk = [1] + attention_mask_chunk
            if end < len(input_ids):
                input_ids_chunk = input_ids_chunk + [tokenizer.sep_token_id]
                attention_mask_chunk = attention_mask_chunk + [1]

            # Convert to PyTorch tensors and add batch dimension
            input_dict = {
                'input_ids': torch.tensor([input_ids_chunk]),
                'attention_mask': torch.tensor([attention_mask_chunk])
            }

            # Get embeddings from the model
            outputs = model(**input_dict)
            embeddings.append(outputs.last_hidden_state[:, 0, :])  # [CLS] token embeddings

        # Stack and average the embeddings
        embeddings = torch.cat(embeddings, dim=0)
        average_embeddings = embeddings.mean(dim=0)
        return average_embeddings

def summarize(text, max_length=256):
    return summarizer(text, min_length=50, max_length=max_length, do_sample=False)