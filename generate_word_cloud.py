def is_relivant(word, jargons):
    if word not in jargons:
        return True
    else:
        return False

def create_cleaned_list(content_list, irrelivant_jargons):
    neat_list = []
    for item in content_list:
        if item.isalpha() and is_relivant(item, irrelivant_jargons):
            cleaned_list.append(item.lower())
    return neat_list        

def generate_frequencies(sifted_list):
    words_dictionary = {}
    for word in sifted_list:
        words_dictionary[word] = words_dictionary.get(word, 0) + 1        
    return list(words_dictionary.values()).sort()

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE STARTS HERE
    content_list = file_contents.strip().split(punctuations)
    cleaned_list = create_cleaned_list(content_list, uninteresting_words)
    frequencies_list = generate_frequencies(cleaned_list)
        
    # Wordcloud module
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies_list)
    return cloud.to_array()
