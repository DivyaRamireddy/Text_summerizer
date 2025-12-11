# text_summarizer.py
# UNIQUE INTERMEDIATE PROJECT: Simple Text Summarizer (No external libraries)

import string

def summarize_text(paragraph, sentence_count=2):
    # Step 1: Split into sentences
    sentences = paragraph.split(".")
    sentences = [s.strip() for s in sentences if s.strip()]

    # Step 2: Build word frequency dictionary
    freq = {}
    for sentence in sentences:
        for word in sentence.lower().split():
            word = word.strip(string.punctuation)
            if word:
                freq[word] = freq.get(word, 0) + 1

    # Step 3: Score each sentence based on important words
    scores = {}
    for sentence in sentences:
        score = 0
        for word in sentence.lower().split():
            word = word.strip(string.punctuation)
            if word in freq:
                score += freq[word]
        scores[sentence] = score

    # Step 4: Pick the top N sentences
    sorted_sentences = sorted(scores, key=scores.get, reverse=True)
    
    return sorted_sentences[:sentence_count]


if __name__ == "__main__":
    print("🧠 Simple Text Summarizer")
    print("--------------------------")

    text = input("Enter a paragraph:\n")

    print("\nHow many sentences do you want in the summary?")
    n = int(input("Enter a number: "))

    summary = summarize_text(text, n)

    print("\n✨ Summary:")
    for line in summary:
        print("- " + line)
