import firebase_admin
import spacy
from firebase_admin import credentials, firestore
import openai
from spacy import load


cred = credentials.Certificate("ml-task-47f6c-firebase-adminsdk-wmr4y-b91feb1ae2.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

openai.api_key = "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"

nlp = spacy.load('en_core_web_lg')
question = input("Enter your Question:- ").lower()


doc = nlp(question)

nouns = [tok.text.lower() for tok in doc if tok.pos_=='PROPN']

if not nouns:
    nouns = [tok.text.lower() for tok in doc if tok.pos_=='NOUN']

questions_ref = db.collection('questions')

if len(nouns) > 1:
    query = questions_ref.where('nouns', 'array_contains', nouns[1]).get()
    final_result = list(query)
    for i in range(2, len(nouns)):
        query = questions_ref.where('nouns', 'array_contains', nouns[i]).get()
        final_result.extend(query)
else:
    query = questions_ref.where('nouns', 'array_contains_any', nouns).get()
    final_result = list(query)

answers_noun_match = []

for doc in final_result:
    answers_noun_match.append(doc.to_dict()["answer"])

# check if there is any exact question match in database
query = questions_ref.where('question', '==', question).get()
answers_question_match = []

for doc in query:
    answers_question_match.append(doc.to_dict()["answer"])

if answers_question_match:
    print(answers_question_match[0])
else:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"{question} \n\n"),
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0
    )
    openai_answer = response.choices[0].text

    print(openai_answer)


if answers_noun_match:
    for answer in answers_noun_match:
        print(answer)
    doc_ref = db.collection("questions").document()
    doc_ref.set({
        "question": question,
        "answer": openai_answer,
        "nouns": nouns
    })
else:
    doc_ref = db.collection("questions").document()
    doc_ref.set({"question": question,
                 "answer": openai_answer,
                 "nouns": nouns
                 })

if len(answers_noun_match) > 0:
    matching_nouns = [doc.to_dict()["nouns"] for doc in final_result if doc.to_dict()["nouns"] == nouns]
    if len(matching_nouns) > 0:
        print()
    else:
        pass
else:
    pass

