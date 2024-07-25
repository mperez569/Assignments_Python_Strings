#1. Product Review Analysis
#Task 1: Keyword Highlighter
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "Poor", "average"]

def highlight_keywords(reviews, keywords):
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        print(review)
highlight_keywords(reviews, keywords)

#Task 2: Sentiment Tally
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def sentiment_tally(reviews, positive_words, negative_words):
    total_positive = 0
    total_negative = 0
    
    for review in reviews:
        review_lower = review.lower()  # Convert review to lowercase for case insensitive matching
        for word in positive_words:
            total_positive += review_lower.count(word)
        for word in negative_words:
            total_negative += review_lower.count(word)
    
    return total_positive, total_negative

positive_count, negative_count = sentiment_tally(reviews, positive_words, negative_words)
print(f"Total positive words: {positive_count}")
print(f"Total negative words: {negative_count}")

#Task 3: Review Summary

def create_summary(review, length=30):
    if len(review) <= length:
        return review
    
    end = length
    if review[length] != " ":
        while end > 0 and review[end] != " ":
            end -= 1
    
    summary = review[:end] + "…" if end > 0 else review[:length] + "…"
    return summary

for review in reviews:
    print(create_summary(review))
