import re
import spacy
nlp = spacy.load('en_core_web_sm')

# sample text for analysis
# text = '''e Khalistan Commando Force (KCF), a banned terror organisation was designated as an “individual terrorist”

# A Pakistan-based Khalistani terrorist from Punjab was shot dead by two unidentified gunmen in Lahore on May 6, a government source said. Paramjit Singh Panjwar (63), a key leader of the Khalistan Commando Force (KCF), a banned terror organisation, was designated as an “individual terrorist” under the Unlawful Activities Prevention Act (UAPA) in 2020.

# The source said that Singh was shot on Saturday morning when he had gone out for a walk. He was accompanied by a security guard when motorcycle-borne assailants shot at him from a close range. The source added that Singh used to live under Pakistan ISI’s protection. A photograph shared by officials showed Singh, dressed in a track suit and jogging shoes, lying in a pool of blood.

# A Ministry of Home Affairs notification July 1, 2020 had said that Singh arranged arms training for youths in Pakistan and remained engaged in supplying of arms and ammunition, and subsequent infiltration into India for targeting Very Important Persons (VIP) and economic installations.

# Singh belonged to Tarn Taran district of Punjab and had escaped to Pakistan in 1990.'''

text = """Recently machine learning methods are widely used to improve the diagnosis
process of ASD [10–12]. [13] used different machine learning algorithms like Tree
models (random forest, decision tree) and Neural Network and Tree models in order to
reduce the ASD diagnostic process time duration [14]. Piloted an experimental review
for comparison of six major machine learning algorithms viz. Categorical Lasso,
Support Vector Machine, Random Forest, Decision Tree, Logistic Regression, and
Linear Discriminant Analysis, in order to choose the best fitting model for ASD and
ADHD.
[15] studied the common issues associated to psychiatric disorders inclusive of
external validity, small sample sizes, and machine learning algorithmic trials without a
strong emphasis on autism. The authors suggested that one of these classifiers, used
individually or in combination with the previously generated behavioural classifiers
clearly focused on discriminating autism from non-autism category that is encompassing, could behave as a valuable triage tool and pre-clinical screening to evaluate
the risk of autism and ADHD [14].
[16] used FURIA (Fuzzy Unordered Rule Induction Algorithm) on ASD dataset for
forecasting autistic symptoms of children aged between 4-11 Years. The results
exposed that FURIA fuzzy rules were able to identify ASD behaviours with 91.35%
accuracy of classification and 91.40% sensitivity rate; these results were better than
other Rule Induction and Greedy techniques.
[17] and [18] applied Naïve Bayes, SOM, K-Means, etc. on a set of 100 instances
ASD dataset collected using CARS diagnostic tool [19]. Used Random Forest algorithm to predict ASD among 8-year old children in multiple US sites. The results
revealed that the machine learning approach predicted ASD with 86.5% accuracy. The
above appraisals have concentrated on the comprehensive domain of mining clinical
data, the trials encountered, and the results inferred from analysis of clinical data"""
pattern = r'\[\d+]+'
text = re.sub(pattern, '', text)
# parse the text using Spacy
doc = nlp(text)

# create a list of (sentence, score) tuples based on sentence similarity
sentences = [(sent.text.strip(), sent.similarity(doc)) for sent in doc.sents]

# sort the list in descending order of similarity score and select top 5 sentences
top_sentences = sorted(sentences, key=lambda x: x[1], reverse=True)[:5]

# print the top 5 sentences
for i, (sentence, score) in enumerate(top_sentences):
    text = "".join(sentence)
    # print(f'Top {i+1} sentence: {sentence}\nSimilarity score: {score:.2f}\n')
    print(text)
