# PE4 part 1.1a and 1.1b.

import wikipedia
import time

result = wikipedia.search("generative artificial intelligence")
print(result)

search_results = wikipedia.search("generative artificial intelligence")

for topic in search_results:
	page = wikipedia.page(topic, auto_suggest=False)
	file_name = f"{page.title}.txt"
	with open(file_name, "w", encoding="utf-8") as file:
		file.write(page.content)

	print(f"File '{file_name}' created with the content from the Wikipedia page '{page.title}'")

# print to the console the amount of time it took the program to execute. 

start_time = time.time()

search_results = wikipedia.search("generative artificial intelligence")

for topic in search_results:
	page = wikipedia.page(topic, auto_suggest=False)
	file_name = f"{page.title}.txt"
	with open(file_name, "w", encoding="utf-8") as file:
		file.write(page.content)

	print(f"File '{file_name}' created with the content from the Wikipedia page '{page.title}'")

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")



