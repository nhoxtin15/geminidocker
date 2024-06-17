

import google.generativeai as genai
import os

class GenAI:
	api_key = None
	model = None
	def init(api_key):
		GenAI.api_key = api_key
		genai.configure(api_key=api_key)
		GenAI.model = genai.GenerativeModel("gemini-1.5-flash") 
		
	def gen():
		PromptsDict = GenAI.list_text_files("Prompt")

		for prompt in PromptsDict:
			with open(PromptsDict[prompt], 'r') as file:
				promptText = file.read()
				response = GenAI.model.generate_content(promptText)
				with open("Result/"+prompt, 'w') as file:
					file.write(response.text)
					print("Generated: "+prompt)
					print(response.text)

	def list_text_files(directory):
		ansDict = {}
		for root, dirs, files in os.walk(directory):
			for file in files:
				if file.endswith('.txt') and not file.endswith('-swap.txt'):
					ansDict[file] = os.path.join(root, file)
		return ansDict




key = ""

GenAI.init(key)
GenAI.gen()
