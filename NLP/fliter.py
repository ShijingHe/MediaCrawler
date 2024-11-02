import pandas as pd
from snownlp import SnowNLP
import re
import jieba
from stopwordsiso import stopwords
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load Chinese stopwords using stopwords-iso
chinese_stopwords = stopwords(["zh"])  # Load Chinese stopwords

# Function to clean text, including removing emojis, Chinese-style emojis, and user mentions
def clean_text(text):
    if isinstance(text, str):  # Check if the input is a string
        # Remove URLs
        text = re.sub(r'http\S+|www.\S+', '', text)
        # Remove user mentions like @username, including Chinese usernames
        text = re.sub(r'@\S+', '', text)
        # Remove the word "doge"
        text = re.sub(r'\bdoge\b', '', text, flags=re.IGNORECASE)
        # Remove Chinese-style emojis like [微笑R], [害羞R], etc.
        text = re.sub(r'\[\w+R]', '', text)  # Matches patterns like [textR]
        # Remove standard emojis
        emoji_pattern = re.compile(
            "[\U00010000-\U0010ffff]"  # Matches a wide range of emoji unicode characters
            "|[\u2600-\u26FF]"  # Miscellaneous symbols
            "|[\u2700-\u27BF]",  # Dingbats
            flags=re.UNICODE)
        text = emoji_pattern.sub(r'', text)  # Remove emojis

        # Remove any remaining special characters except for words and spaces
        text = re.sub(r'[^\w\s]', '', text)

        return text.strip()
    return ''  # Return empty string if the input is not a string

# Function to apply Jieba segmentation and stopword removal on cleaned text
def jieba_tokenize(text):
    if isinstance(text, str) and text.strip() != '':
        # Segment the text using Jieba
        tokens = jieba.lcut(text)
        # Remove stopwords
        filtered_tokens = [token for token in tokens if token not in chinese_stopwords]
        # Join tokens with a space to form a segmented string
        return ' '.join(filtered_tokens)
    return text  # Return the original text if it's empty or not a string

# Function to calculate sentiment score using SnowNLP
def sentiment_score(text):
    if isinstance(text, str) and text.strip() != '':
        s = SnowNLP(text)
        return s.sentiments  # Returns a score between 0 (negative) and 1 (positive)
    return None  # Return None if the text is empty or not a string

# Load your CSV file into a DataFrame
df = pd.read_csv('/data/xhs/1_detail_comments_2024-09-06.csv')

# Print columns to verify column names
print(df.columns)

# Apply the clean_text function to the 'content' column only from row 2 to 20778
df.loc[1:20777, 'content'] = df.loc[1:20777, 'content'].apply(clean_text)

# Apply Jieba segmentation and stopword removal to the cleaned 'content' column
df.loc[1:20777, 'content'] = df.loc[1:20777, 'content'].apply(jieba_tokenize)

# Apply sentiment scoring using SnowNLP
df['sentiment_score'] = df['content'].apply(sentiment_score)

# Drop rows with None sentiment scores if necessary
df = df.dropna(subset=['sentiment_score'])

# Grouping and summarizing sentiment scores using pandas
# Example: Group by note_id and calculate average sentiment score and count of comments
sentiment_summary = df.groupby('note_id').agg(
    avg_sentiment=('sentiment_score', 'mean'),
    comment_count=('content', 'count')
).reset_index()

# Print the summarized results
print(sentiment_summary.head())

# Save the sentiment summary to a CSV file
sentiment_summary.to_csv('/Users/shijinghe/PycharmProjects/MediaCrawler-main/data/xhs/sentiment_summary.csv', index=False)

# Visualization of sentiment scores
plt.figure(figsize=(10, 6))
sns.histplot(sentiment_summary['avg_sentiment'], bins=20, kde=True, color='blue')
plt.title('Distribution of Average Sentiment Scores')
plt.xlabel('Average Sentiment Score')
plt.ylabel('Frequency')
plt.show()

# Word Cloud of frequent words in positive and negative sentiments
positive_comments = ' '.join(df[df['sentiment_score'] > 0.5]['content'])
negative_comments = ' '.join(df[df['sentiment_score'] <= 0.5]['content'])

# Generate and display the word cloud for positive comments
plt.figure(figsize=(20, 10))
wordcloud_positive = WordCloud(font_path='Songti.ttc', background_color='white', max_words=200000).generate(positive_comments)
plt.imshow(wordcloud_positive, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Positive Sentiments')
plt.show()

# Generate and display the word cloud for negative comments
plt.figure(figsize=(20, 10))
wordcloud_negative = WordCloud(font_path='Songti.ttc', background_color='white', max_words=200000, colormap='Reds').generate(negative_comments)
plt.imshow(wordcloud_negative, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Negative Sentiments')
plt.show()
