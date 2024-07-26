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

def highlight(reviews, keywords):
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        print(review)
highlight(reviews, keywords)

#Task 2: Sentiment Tally
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def sentiment_tally(reviews, positive_words, negative_words):
    total_positive = 0
    total_negative = 0
    
    for review in reviews:
        review_lower = review.lower()  
        for word in positive_words:
            total_positive += review_lower.count(word)
        for word in negative_words:
            total_negative += review_lower.count(word)
    
    return total_positive, total_negative

positive_count, negative_count = sentiment_tally(reviews, positive_words, negative_words)
print("Total positive words: " + str(positive_count))
print("Total negative words: " + str(negative_count))

#Task 3: Review Summary
def create_summary(review, length=30):
    if len(review) <= length:
        return review
    
    end = length
    while end < len(review) and review[end] != " ":
        end += 1
    
    summary = review[:end] + "…" if end < len(review) else review
    return summary

for review in reviews:
    print(create_summary(review))
    
######
#2. User Input Data Processor
#Task 1: Input Length Validator
def name_length():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    if len(first_name) < 2:
        print("Error: First name must be at least 2 characters long.")
    if len(last_name) < 2:
        print("Error: Last name must be at least 2 characters long.")
    
    if len(first_name) >= 2 and len(last_name) >= 2:
        print("First name and last name are valid.")

name_length()


