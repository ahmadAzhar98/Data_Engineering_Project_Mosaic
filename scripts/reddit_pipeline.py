import praw
import os
import csv
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Reddit API Credentials from .env file
CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")

# Paths for raw and cleaned data
RAW_PATH = "/Users/ahmadazhar/Desktop/Assignment1/datasets/raw/reddit_comments_raw.csv"
CLEAN_PATH = "/Users/ahmadazhar/Desktop/Assignment1/datasets/clean/reddit_comments_clean.csv"

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

# READ DATA
def fetch_reddit_comments(url, raw_path, limit=200):
    submission = reddit.submission(url=url)
    submission.comments.replace_more(limit=0)
    
    data = []
    for comment in submission.comments.list()[:limit]:
        data.append({
            "title": submission.title,
            "post_text": comment.body,  # Corrected to fetch comment text
            "author": comment.author.name if comment.author else "[deleted]",
            "date": comment.created_utc,
            "upvotes": comment.score,
            "subreddit": submission.subreddit.display_name
        })
    
    df = pd.DataFrame(data)
    df.to_csv(raw_path, index=False)
    print("Raw Reddit comments saved successfully!")
    return df

# TEXT CLEANING FUNCTION
def clean_text(text):
    if pd.isna(text) or text in ["[deleted]", "[removed]"]:
        return ""
    
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters & punctuation
    tokens = word_tokenize(text)  # Tokenization
    tokens = [word for word in tokens if word not in stopwords.words('english')]  # Remove stopwords
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]  # Lemmatization
    return " ".join(tokens)

# DATA PREPROCESSING
def data_preprocessing(input_file, output_file):
    df = pd.read_csv(input_file)
    
    # Apply text cleaning
    df['post_text'] = df['post_text'].apply(clean_text)
    
    # Remove empty comments
    df = df[df['post_text'].str.strip() != ""]
    
    # Remove duplicates
    duplicates = df.duplicated().sum()
    print(f"Total duplicate values removed: {duplicates}")
    df.drop_duplicates(inplace=True)
    
    df.to_csv(output_file, index=False)
    print("Data cleaned and saved successfully!")
    
# ANALYZE DATA
def analyze_data(clean_file):
    df = pd.read_csv(clean_file)
    
    # Top upvoted comment
    top_comment = df.loc[df['upvotes'].idxmax(), ['author', 'upvotes']]
    print(f"🔥 Top Comment: {top_comment['author']} ({top_comment['upvotes']} upvotes) 🔥")

# RUN THE PIPELINE
if __name__ == "__main__":
    URL = "https://www.reddit.com/r/Cricket/comments/17z01xd/australia_are_champions_of_the_2023_odi_world_cup/"
    df_raw = fetch_reddit_comments(URL, RAW_PATH)
    data_preprocessing(RAW_PATH, CLEAN_PATH)
    analyze_data(CLEAN_PATH)
