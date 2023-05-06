import re
import spacy
nlp = spacy.load('en_core_web_sm')


def top_sentences(text):
    # sample text for analysis
    # text = '''e Khalistan Commando Force (KCF), a banned terror organisation was designated as an “individual terrorist”

    # A Pakistan-based Khalistani terrorist from Punjab was shot dead by two unidentified gunmen in Lahore on May 6, a government source said. Paramjit Singh Panjwar (63), a key leader of the Khalistan Commando Force (KCF), a banned terror organisation, was designated as an “individual terrorist” under the Unlawful Activities Prevention Act (UAPA) in 2020.

    # The source said that Singh was shot on Saturday morning when he had gone out for a walk. He was accompanied by a security guard when motorcycle-borne assailants shot at him from a close range. The source added that Singh used to live under Pakistan ISI’s protection. A photograph shared by officials showed Singh, dressed in a track suit and jogging shoes, lying in a pool of blood.

    # A Ministry of Home Affairs notification July 1, 2020 had said that Singh arranged arms training for youths in Pakistan and remained engaged in supplying of arms and ammunition, and subsequent infiltration into India for targeting Very Important Persons (VIP) and economic installations.

    # Singh belonged to Tarn Taran district of Punjab and had escaped to Pakistan in 1990.'''
    pattern = r'\[\d+]+'
    text = re.sub(pattern, '', text)
    # parse the text using Spacy
    doc = nlp(text)

    # create a list of (sentence, score) tuples based on sentence similarity
    sentences = [(sent.text.strip(), sent.similarity(doc))
                 for sent in doc.sents]

    # sort the list in descending order of similarity score and select top 5 sentences
    top_sentences = sorted(sentences, key=lambda x: x[1], reverse=True)[:5]

# print the top 5 sentences
    for i, (sentence, score) in enumerate(top_sentences):
        text = "".join(sentence)
    # print(f'Top {i+1} sentence: {sentence}\nSimilarity score: {score:.2f}\n')
        return text
