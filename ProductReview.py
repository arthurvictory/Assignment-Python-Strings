# Task 1: Keyword Highlighter

# Write a program that searches through reviews list and looks for keywords such as "good", "excellent", 
# "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. 
# Print out each review with the keywords in uppercase so they stand out.

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

def capitalize(review, keywords):
        for keyword in keywords:
                review = review.replace(keyword, keyword.upper())
        return review

for review in reviews:
        print(capitalize(review,keywords))

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.

# function to count all positive and negative words in the review list
def word_tally(reviews, positive_words, negative_words):
    positive = 0
    negative = 0
    
    for review in reviews:
        for word in positive_words:
            positive += review.lower().count(word)
        for word in negative_words:
            negative += review.lower().count(word)
    
    return positive, negative

positive, negative = word_tally(reviews, positive_words, negative_words)
print(f"Total positive words: {positive}")
print(f"Total negative words: {negative}")

# Task 3: Review Summary
# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
# Ensure that the summary does not cut off in the middle of a word.
# Example: "This product is really good. I'm...",

def summary(review, length=30):
    if len(review) <= length:
        return review
    else:
        summary = review[:length].rsplit(' ', 1)[0]
        return summary + "…"

for review in reviews:
        print(summary(review))