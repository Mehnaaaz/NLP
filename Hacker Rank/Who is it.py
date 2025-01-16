import re

def resolve_pronouns(text, entities):
    # Extract all pronouns enclosed in ** from the text
    pronouns = re.findall(r'\*\*(\w+)\*\*', text)
    
    # Clean the text by removing the highlighting markers (to match against entities)
    clean_text = re.sub(r'\*\*(\w+)\*\*', r'\1', text)
    
    # Split entities into a list
    entity_list = [entity.strip() for entity in entities.split(';')]
    
    # Initialize result list
    results = []
    
    # Resolve each pronoun
    for pronoun in pronouns:
        match = None
        min_distance = float('inf')
        
        # Check each entity to find the closest one
        for entity in entity_list:
            # Find all occurrences of the entity in the text
            occurrences = [m.start() for m in re.finditer(re.escape(entity), clean_text)]
            
            # Calculate distance for each occurrence
            for occurrence in occurrences:
                pronoun_pos = clean_text.find(pronoun)
                distance = abs(pronoun_pos - occurrence)
                
                # Update the closest match
                if distance < min_distance:
                    min_distance = distance
                    match = entity
        
        results.append(match)
    
    return results

# Input processing
n = int(input())
text = "\n".join(input() for _ in range(n))
entities = input()

# Resolve pronouns
resolved = resolve_pronouns(text, entities)

# Output the results
for r in resolved:
    print(r)
