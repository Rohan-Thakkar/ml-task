import firebase_admin
import nltk

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
from firebase_admin import credentials, firestore
import openai
from nltk.tokenize import word_tokenize

# Initialize Firebase Admin SDK
cred = credentials.Certificate("D:\Rohan\ml_task\ml_task\ml-task-47f6c-firebase-adminsdk-wmr4y-b91feb1ae2.json")
firebase_admin.initialize_app(cred)
# https://your-firebase-project.firebaseio.com/

# Connect to Firebase Database
db = firestore.client()

# Set OpenAI API key
openai.api_key = "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"

# User's question
question = input("Enter your Question:- ")

# Tokenize the question
tokens = nltk.word_tokenize(question)

# Use NLTK's part-of-speech tagging to extract nouns
nouns = [word.lower() for word, pos in nltk.pos_tag(tokens) if pos.startswith('NN')]

# Convert the extracted nouns to lowercase
# lower_nouns = [noun.lower() for noun in nouns]

# Use the extracted nouns to query the Firebase database for similar questions
questions_ref = db.collection('questions')
query = questions_ref.where('nouns', 'array_contains_any', nouns).get()

# Keep track of the answers found in the Firebase database
answers = []

# Iterate through the query results
for doc in query:
    doc_ref = db.collection("questions").document(doc.id)
    doc = doc_ref.get()
    answers.append(doc.to_dict()["answer"])

# If answers were found in the Firebase database, display them
# if answers:
#     for answer in answers:
#         print("Answer from Firebase Database:", answer)

# Use GPT-2 to extract context and make deductions
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=(f"{question} \n\n"),
    max_tokens=3000,
    n=1,
    stop=None,
    temperature=0
)

# Extract the answer from the response
openai_answer = response.choices[0].text

# Compare the answer from Firebase database with the answer from OpenAI
if answers and openai_answer in answers:
    print("Answer from OpenAI:", answers)
else:
    print("Answer from OpenAI:", openai_answer)
    for line in answers:
        print("Answer from database:", line)
    # print("Answer from database:", ''.join(answers))
    #openai_answer.append(answers)

# Store the question, answer, and nouns in the Firebase Firestore database
doc_ref = db.collection("questions").document()
doc_ref.set({
    "question": question,
    "answer": openai_answer,
    "nouns": nouns
})
print("Question, answer, and nouns successfully stored in Firestore database.")