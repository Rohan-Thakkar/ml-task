import firebase_admin
import nltk
from firebase_admin import credentials, firestore
import openai


cred = credentials.Certificate("D:\Rohan\ml_task\ml_task\ml-task-47f6c-firebase-adminsdk-wmr4y-b91feb1ae2.json")
firebase_admin.initialize_app(cred)


db = firestore.client()


openai.api_key = "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"

question = input("Enter your Question:- ")

tokens = nltk.word_tokenize(question)

nouns = [word.lower() for word, pos in nltk.pos_tag(tokens) if pos.startswith('NN')]

questions_ref = db.collection('questions')
query = questions_ref.where('nouns', 'array_contains_any', nouns).get()

answers = []

for doc in query:
    doc_ref = db.collection("questions").document(doc.id)
    doc = doc_ref.get()
    answers.append(doc.to_dict()["answer"])

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=(f"{question} \n\n"),
    max_tokens=3000,
    n=1,
    stop=None,
    temperature=0
)

openai_answer = response.choices[0].text

if answers and openai_answer in answers:
    print("Answer from OpenAI:", answers)
else:
    print("Answer from OpenAI:", openai_answer)
    for line in answers:
        print("Answer from database:", line)


doc_ref = db.collection("questions").document()
doc_ref.set({
    "question": question,
    "answer": openai_answer,
    "nouns": nouns
})
print("Question, answer, and nouns successfully stored in Firestore database.")