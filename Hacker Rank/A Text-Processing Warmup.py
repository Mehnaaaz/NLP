import re

def count_articles_and_dates(text):
    # Count occurrences of articles
    count_a = len(re.findall(r'\ba\b', text, re.IGNORECASE))
    count_an = len(re.findall(r'\ban\b', text, re.IGNORECASE))
    count_the = len(re.findall(r'\bthe\b', text, re.IGNORECASE))
    
    # Define regex patterns for dates
    date_patterns = [
        r'\b(\d{1,2}(?:st|nd|rd|th)?[-/ ](?:\d{1,2}|(?:January|February|March|April|May|June|July|August|September|October|November|December)[a-zA-Z]*[-/ ]\d{2,4}))\b',
        r'\b(?:\d{1,2}(?:st|nd|rd|th)? (?:January|February|March|April|May|June|July|August|September|October|November|December)[a-zA-Z]*,? \d{2,4})\b',
        r'\b(?:\d{1,2} (?:of )?(?:January|February|March|April|May|June|July|August|September|October|November|December),? \d{2,4})\b'
    ]
    
    # Combine all patterns into one
    combined_pattern = '|'.join(date_patterns)
    
    # Count occurrences of dates
    count_dates = len(re.findall(combined_pattern, text, re.IGNORECASE))
    
    return count_a, count_an, count_the, count_dates

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    T = int(data[0].strip())
    results = []
    
    for i in range(1, 2 * T, 2):
        text_fragment = data[i].strip()
        count_a, count_an, count_the, count_dates = count_articles_and_dates(text_fragment)
        
        results.append(f"{count_a}")
        results.append(f"{count_an}")
        results.append(f"{count_the}")
        results.append(f"{count_dates}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()