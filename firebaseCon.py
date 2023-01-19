import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import openai

# Initialize Firebase Admin SDK
cred = credentials.Certificate("D:\Rohan\ml_task\ml_task\ml-task-47f6c-firebase-adminsdk-wmr4y-b91feb1ae2.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ml-task-47f6c-default-rtdb.firebaseio.com/'
})
# https://your-firebase-project.firebaseio.com/

# Connect to Firebase Database
ref = db.reference()

# Set OpenAI API key
openai.api_key = "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"

# Get data from Firebase Database
#Get data from Firebase Database
# ref.child("products1").push({"description": '''Machine Learning (ML) is a method of data analysis that automates analytical model building. It is a branch of artificial intelligence based on the idea that systems can learn from data, identify patterns and make decisions with minimal human intervention.
# There are different types of ML algorithms, including supervised learning, unsupervised learning, semi-supervised learning and reinforcement learning.
# Supervised learning is the most common type of ML, where the system is trained on a labeled dataset, and then used to make predictions on new, unseen data. Common examples of supervised learning algorithms include linear regression, logistic regression, and decision trees.
# Unsupervised learning, on the other hand, is used when the system is not given any labeled data but is still expected to find patterns in the input data. Common examples of unsupervised learning algorithms include k-means clustering and hierarchical clustering.
# Semi-supervised learning is a combination of supervised and unsupervised learning, where the system is given some labeled data and some unlabeled data, and it is expected to find patterns in the unlabeled data.
# Reinforcement learning is a type of ML that is concerned with learning how to make decisions. The system learns by interacting with its environment, and it is rewarded or penalized based on its actions.
# ML has a wide range of applications, including natural language processing, computer vision, speech recognition, and financial forecasting, to name a few. It is widely used in industries such as healthcare, finance, and retail.
# In conclusion, Machine Learning is a powerful tool for data analysis and decision making. It allows systems to learn from data and make predictions with minimal human intervention. With the rapid advancement in technology, the potential for ML applications is limitless.
#
# More information about ML blog-
#
# Here are some hashtags for ML-
# #MLrevolution
# #MLmindset
# #MLpower
# #MLfuture
# #MLinnovation
# #MLtransformation
# #MLdisruption
# #MLpredictive
# #MLautomation
# #MLdeeplearning
# #MLbigdata
# #MLalgorithm
# #MLAI
# #MLlearning
#
# Here are some titles for ML-
# "Unlocking the Power of Machine Learning for Predictive Analytics"
# "The Future of Business: How Machine Learning is Changing the Game"
# "AI and ML: The Dynamic Duo Transforming Industries"
# "Deep Learning and Machine Learning: A Comparative Study"
# "The Impact of Machine Learning on Big Data Analytics"
# "Real-World Applications of Machine Learning: From Healthcare to Finance"
# "Reinforcement Learning: A Game-Changing Approach to Machine Learning"
# "The Role of Machine Learning in Automating Business Processes"
# "Unsupervised Learning: A Powerful Tool in Machine Learning"
# "Machine Learning and the Rise of Intelligent Systems"
#
# Here are some keywords for ML-
# Artificial Intelligence
# Deep Learning
# Predictive Analytics
# Supervised Learning
# Unsupervised Learning
# Reinforcement Learning
# Neural Networks
# Natural Language Processing
# Computer Vision
# Machine Learning Algorithms
# Big Data
# Data Mining
# Predictive Modeling
# Automation
# Decision Making
# Regression
# Clustering
# Gradient Descent
# Feature Selection
# Overfitting
# Regularization
# Hyperparameter tuning
# Ensemble methods
# Transfer learning
# Explainable AI (XAI)
# Reinforcement learning
# Generative Adversarial Networks (GANs)
# Recurrent Neural Networks (RNNs)
# Convolutional Neural Networks (CNNs)
# Long-Short Term Memory (LSTM)
# Natural Language Understanding (NLU)
# Natural Language Generation (NLG)
# Machine Learning as a Service (MLaaS)
# Predictive Maintenance
# Anomaly detection
# Time series forecasting
# Recommender systems.'''})

data = ref.child("products1").get()

# create a string of all the products
# products = ' '.join([f'{key}:{value}' for key, value in data.items()])

# Send data to GPT-3 as a prompt
prompt = (f"Echo {data}")
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=3000,
    n=1,
    stop=None,
    temperature=0,
)

a = input("enter your question here:-")
if a == "write a blog on ml":
    print(response["choices"][0]["text"])
else:
    print("please enter valid input")