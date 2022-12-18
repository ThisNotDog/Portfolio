import wordcloud

#cleans a text file, filters out non \w characters
#removes common words
#ports to a set, counting instances of duplicate words
#creates a wordcloud of the resulting set

y = open(<'your text file'>, 'r')
file_contents = y.read()

def calculate_frequencies(file_contents):
    iterated = ""
    processed = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
        "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
        "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
        "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
        "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    for i in file_contents:
        if i.isalpha():
            iterated += i
        if i == " ":
            iterated += i
        if i == ".":
            iterated += " "        
        else:
            pass
    processed = iterated.lower()
    split = processed.split(" ")
    txt_set = {}
    delete_words = [k for k in split if k not in uninteresting_words]
    
    txt_set = {i:delete_words.count(i) for i in delete_words}
    for k in delete_words:
        if k in uninteresting_words:
            del txt_set[k]   
    return txt_set
print(calculate_frequencies(file_contents))
 
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(calculate_frequencies(file_contents))
cloud.to_file("frequencies.jpg")  
