import wordcloud
#cleans a text file, filters out non alpha characters
#removes common words
#ports to a set, counting instances of duplicate words
#creates a wordcloud of the resulting set
def calculate_frequencies():
    with open("[your text file]", "r", endoding="utf-8") as file_contents:
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
            "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
            "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
            "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
            "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
        for character in file_contents:
            if character.isalpha():
                filtered_characters += character
            if character == " ":
                filtered_characters+= character
            if character in punctuations:
                pass
            else:
                pass
        lower_case_substrings = filtered_characters.lower()
        substring_list = lower_case_substrings.split(" ")
        txt_set = {}
        deleted_words = [word for word in substring_list if word not in uninteresting_words]   
        txt_set = {i:deleted_words.count(i) for i in deleted_words}
        for k in deleted_words:
            if k in uninteresting_words:
                del txt_set[k]   
        return txt_set
    file_contents.close()
print(calculate_frequencies())
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(calculate_frequencies())
cloud.to_file("frequencies.jpg")  
