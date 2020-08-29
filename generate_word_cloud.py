
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()

def is_relivant(word, jargons):
    '''
    Checks wether a word is relevant or not.
    Accepts the word and a list of irrelivant words as input.
    Returns a boolean value.
    '''
    if word not in jargons:
        return True
    else:
        return False

def create_cleaned_list(content_list, irrelivant_jargons):
    '''
    Given a list, this filters irrelivant words in it and
    returns a list of only relevent words. It accepts both
    the list and a list of irrelevant words.
    '''
    neat_list = []
    for item in content_list:
        if item.isalpha() and is_relivant(item, irrelivant_jargons):
            neat_list.append(item.lower())
    return neat_list        

def generate_word_freq_dict(sifted_list):
    '''
    This function takes a list of words, calculates the frequency of 
    each word and generates a dictionary from it. Making the word a 
    key and the frequency a value. It returns the generated dictionary.
    '''
    words_dictionary = {}
    for word in sifted_list:
        words_dictionary[word] = words_dictionary.get(word, 0) + 1        
    return words_dictionary

def calculate_frequencies(file_contents):
    '''
    Takes a text file as input and generates a word-frequency dictionary from it leveraging the wordcloud module.
    '''
    # Here is a list of punctuations and uninteresting words for use in processing the text
    # punctuations = '''\! |(|)|-|\[|\]|{|}|; |: |'|"|\\|, |\||<|>|\. |\|? |@|#|$|%|\^|&|\*|_|~'''
    puctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE STARTS HERE
    content_list = file_contents.strip().split()
    cleaned_list = create_cleaned_list(content_list, uninteresting_words)
    words_dict = generate_word_freq_dict(cleaned_list)
        
    # Wordcloud module
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(words_dict)
    return cloud.to_array()

# Display your wordcloud image
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()