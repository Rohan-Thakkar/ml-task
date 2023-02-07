import openai

openai.api_key = "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"

question = input("enter your queation:- ")

def generate_blog(question):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

blog_content = generate_blog(question)
print("\n", blog_content)

titles = generate_blog(f"Generate titles for a {question}.")
print("\nTitles:\n", titles)

keywords = generate_blog(f"Generate keywords for a {question}.")
print("\nKeywords:\n", keywords)

hashtags = generate_blog(f"Generate hashtags for a {question}.")
print("\nHashtags:\n", hashtags)