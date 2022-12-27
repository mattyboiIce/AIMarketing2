print("\n App Opened")
providence = input("What is your State: ")
industry = input ("what is your industry: ")

import openai
#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
openai.api_key = "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"

# choices = openai.Completion.create(
#     engine="text-davinci-003",
#     prompt="Give me the top 5 things relevant to " + industry + "in " + providence,
#     temperature=1.0,
#     max_tokens=300,
#     top_p=1,
#     n=1,
#     stream=None
# )

# print(f"choices: {choices}")

# list = choices['choices'][0]['text']

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=industry + " in " + providence,
    temperature=1.0,
    max_tokens=300,
    top_p=1,
    n=1,
    stream=None
)

print("\nMarket Research on the given industry and providence: ")
print(response['choices'][0]['text'])

print("\nBased on the market research, here is the suggested 5-step marketing plan: \n1. Identify the target market and create a customer profile. \n2. Develop a unique value proposition. \n3. Design a creative marketing strategy. \n4. Implement the marketing plan. \n5. Monitor and adjust the marketing plan as needed.")

# print(list)

print("\nWould you like to get more in-depth research on the industry and providence? Here are 5 options you can choose from: \n1. Industry Trends \n2. Competitors \n3. Customer Segments \n4. Buyer Personas \n5. Market Size")

option = input("\nPlease select an option (1-5): ")

if option == '1':
    response2 = openai.Completion.create(
        engine="text-davinci-003",
        prompt="What are the industry trends in " + industry + " in " + providence + "?",
        temperature=1.0,
        max_tokens=300,
        top_p=1,
        n=1,
        stream=None
    )
elif option == '2':
    response2 = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Who are the competitors in " + industry + " in " + providence + "?",
        temperature=1.0,
        max_tokens=300,
        top_p=1,
        n=1,
        stream=None
    )
elif option == '3':
    response2 = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Who are the customer segments in " + industry + " in " + providence + "?",
        temperature=1.0,
        max_tokens=300,
        top_p=1,
        n=1,
        stream=None
    )
elif option == '4':
    response2 = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Who are the buyer personas in " + industry + " in " + providence + "?",
        temperature=1.0,
        max_tokens=300,
        top_p=1,
        n=1,
        stream=None
    )
elif option == '5':
    response2 = openai.Completion.create(
        engine="text-davinci-003",
        prompt="What is the size of the market for " + industry + " in " + providence + "?",
        temperature=1.0,
        max_tokens=300,
        top_p=1,
        n=1,
        stream=None
    )

print("\nIn-depth research on the given option: ")
print(response2['choices'][0]['text'])