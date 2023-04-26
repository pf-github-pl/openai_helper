import os
from sys import argv
from dotenv import load_dotenv
import openai


def main():

    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    if len(argv) != 3:
        print('Enter the source path.')
        print('Enter destination path.')
        print('Execute: python3 -m openai_form source.py target.py')
        quit()

    if not os.path.exists(argv[1]):
        print('Source file does not exist.')
        quit()

    _, source_file, target_file = argv

    with open(source_file, encoding='utf-8') as file:
        context = "You are the professional Python developer with 10+ years of commercial experience.\n"
        context += "Shorten and format the following code with industry best practices, add docstrings if needed: \n"
        code = "".join(file.readlines())
        command = context + code
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=command,
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

    with open(target_file, 'w') as file:
        file.write(response.choices[0].text)
    return True
