from openai import OpenAI
import google.generativeai as genai
import api_keys
from transformers import pipeline

genai.configure(api_key=api_keys.gemini_api_key)
gemini = genai.GenerativeModel("gemini-1.5-flash")
openai = OpenAI(api_key=api_keys.openai_api_key)

class ChatGPT:
    def get_response(self, prompt):
        prompt = f"Write code as per this prompt:\n{prompt}"
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.text
    
    def get_explanation(self, code):
        prompt = f"Explain this code:\n{code}"
        response = openai.chat.completions.create( 
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.text

    def get_modification(self, code, prompt):
        prompt = f"Modify the following code as per this prompt: {prompt}\n{code}"
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.text

class Gemini:
    def get_response(self, prompt):
        prompt = f"Write code as per this prompt:\n{prompt}"
        response = gemini.generate_content(prompt)
        return response.text
    
    def get_explanation(self, code):
        prompt = f"Explain this code:\n{code}"
        response = gemini.generate_content(prompt)
        return response.text
    
    def get_modification(self, code, prompt):
        prompt = f"Modify the following code as per this prompt: {prompt}\n{code}"
        response = gemini.generate_content(prompt)
        return response.text


class gpt2_local:
    
    def __init__(self):
        self.gpt2 = pipeline("text-generation", model="gpt2")

    def get_response(self, prompt):
        prompt = f"Write code as per this prompt:\n{prompt}"
        response = self.gpt2(prompt, max_length=100, truncation=True, clean_up_tokenization_spaces=True)
        return response[0]['generated_text'] 
    
    def get_explanation(self, code):
        prompt = f"Explain this code:\n{code}"
        response = self.gpt2(prompt, max_length=100, truncation=True, clean_up_tokenization_spaces=True)
        return response[0]['generated_text']
    
    def get_modification(self, code, prompt):
        prompt = f"Modify the following code as per this prompt: {prompt}\n{code}"
        response = self.gpt2(prompt, max_length=100, truncation=True, clean_up_tokenization_spaces=True)
        return response[0]['generated_text']
        
if __name__ == "__main__":


    try:
        cmd = int(input("Choose an option:\n1.OpenAI\n2.Gemini\n3.  GPT-2\n"))

        if cmd == 1:
            chatgpt = ChatGPT()
            cmd1 = int(input("What would you like ChatGPT to do:\n1.Explain Code\n2.Write Code\n3.Modify Code\n"))

            if cmd1 == 1:
                code = input("Enter the code you want to explain: ")
                print(chatgpt.get_explanation(code))

            elif cmd1 == 2:
                prompt = input("Enter the prompt for your code: ")
                print(chatgpt.get_response(prompt))

            elif cmd1 == 3:
                code = input("Enter the code you want to modify: ")
                prompt = input("Explain the change you want to make: ")
                print(chatgpt.get_modification(code, prompt))

            else:
                print("Invalid Option")

        elif cmd == 2:
            gemini_ai = Gemini()
            cmd1 = int(input("What would you like Gemini to do:\n1.Explain Code\n2.Write Code\n3.Modify Code\n"))

            if cmd1 == 1:
                code = input("Enter the code you want to explain: ")
                print(gemini_ai.get_explanation(code))

            elif cmd1 == 2:
                prompt = input("Enter the prompt for your code: ")
                print(gemini_ai.get_response(prompt))

            elif cmd1 == 3:
                code = input("Enter the code you want to modify: ")
                prompt = input("Explain the change you want to make: ")
                print(gemini_ai.get_modification(code, prompt))
            else:
                print("Invalid Option")
        
        elif cmd == 3:

            gpt2 = gpt2_local()
            cmd1 = int(input("What would you like GPT-2 to do:\n1.Explain Code\n2.Write Code\n3.Modify Code\n"))

            if cmd1 == 1:
                code = input("Enter the code you want to explain: ")
                print(gpt2.get_explanation(code))

            elif cmd1 == 2:
                prompt = input("Enter the prompt for your code: ")
                print(gpt2.get_response(prompt))

            elif cmd1 == 3:
                code = input("Enter the code you want to modify: ")
                prompt = input("Explain the change you want to make: ")
                print(gpt2.get_modification(code, prompt))
        else:
            print("Invalid Option")
    except Exception as e:
        print(f"An error occurred: {e}")

