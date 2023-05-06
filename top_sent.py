import re
import spacy
nlp = spacy.load('en_core_web_sm')


def top_sentences(page_text):
    summarized_pages=[]
    for i in page_text:
        try:
            textt=""
            pattern = r'\[\d+]+'
            text = re.sub(pattern, '', i)
            text=text.replace("\n"," ")
            # parse the text using Spacy
            doc = nlp(text)

            # create a list of (sentence, score) tuples based on sentence similarity
            sentences = [(sent.text.strip(), sent.similarity(doc))
                        for sent in doc.sents]

            # sort the list in descending order of similarity score and select top 5 sentences
            top_sentences = sorted(sentences, key=lambda x: x[1], reverse=True)[:5]

            # print the top 5 sentences
            for i, (sentence, score) in enumerate(top_sentences):
                textt += "".join(sentence)
            # print(f'Top {i+1} sentence: {sentence}\nSimilarity score: {score:.2f}\n')
            summarized_pages.append([textt])
        except:
            pass
            print("error top_sent")
    return summarized_pages
