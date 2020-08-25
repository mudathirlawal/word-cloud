def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE STARTS HERE
    cleaned_list = []
    content_list = file_contents.strip().split(punctuations)
    
    def is_relivant(word, jargons):
        if word not in jargons:
            return True
        else:
            return False
    
    def create_cleaned_list(content_list, uninteresting_words):  
        for item in content_list:
            if item.isalpha() and is_relivant(item, uninteresting_words):
                cleaned_list.append(item.lower())
                
    def generate_dictionary(sifted_list):
        words_dictionary = {}
        # More code here ...
        # More code here ...
        # More code here ...
        return words_dictionary
        pass
        pass
    
    
    return generate_dictionary(cleaned_list)
        
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies()
    return cloud.to_array()

    