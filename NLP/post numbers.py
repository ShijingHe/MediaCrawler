import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Load data from a CSV file
csv_file_path = '/Users/shijinghe/Desktop/post_number.csv'
df = pd.read_csv(csv_file_path)

# Function to convert Chinese number formats (e.g., '1.5万' -> 15000)
def convert_chinese_numbers(value):
    if isinstance(value, str):
        if '万' in value:
            return float(value.replace('万', '')) * 10000
        else:
            return float(re.sub(r'[^\d.]', '', value))  # Remove any non-numeric, non-decimal characters
    return value  # Return the value as-is if it's already numeric

# Apply conversion to relevant columns
for col in ['liked_count', 'collected_count', 'comment_count', 'share_count']:
    df[col] = df[col].apply(convert_chinese_numbers)

# Define a function to format numbers as K/M/B for the plot
def format_number(x, pos):
    if x >= 1e9:
        return f'{x*1e-9:.1f}B'  # Billion
    elif x >= 1e6:
        return f'{x*1e-6:.1f}M'  # Million
    elif x >= 1e3:
        return f'{x*1e-3:.1f}K'  # Thousand
    else:
        return int(x)  # Less than 1,000, no formatting

# Visualization setup for individual distributions
plt.figure(figsize=(14, 10))

# Create subplots for each metric's distribution on a single figure
plt.subplot(2, 2, 1)
sns.histplot(df['liked_count'], bins=30, color='skyblue')
#plt.title('Distribution of Liked Counts')
plt.xlabel('Liked Count')
#plt.ylabel('Frequency')
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(format_number))

plt.subplot(2, 2, 2)
sns.histplot(df['collected_count'], bins=30, color='salmon')
#plt.title('Distribution of Collected Counts')
plt.xlabel('Collected Count')
#plt.ylabel('Frequency')
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(format_number))

plt.subplot(2, 2, 3)
sns.histplot(df['comment_count'], bins=30, color='lightgreen')
#plt.title('Distribution of Comment Counts')
plt.xlabel('Comment Count')
#plt.ylabel('Frequency')
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(format_number))

plt.subplot(2, 2, 4)
sns.histplot(df['share_count'], bins=30, color='coral')
#plt.title('Distribution of Share Counts')
plt.xlabel('Share Count')
#plt.ylabel('Frequency')
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(format_number))

plt.tight_layout()
plt.show()

# Scatterplot Matrix using pairplot
sns.pairplot(df[['liked_count', 'collected_count', 'comment_count', 'share_count']],
             diag_kind='kde', plot_kws={'alpha':0.5})
plt.suptitle('Scatterplot Matrix of Interaction Counts', y=1.02)
plt.show()
