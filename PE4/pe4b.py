# PE4_1.2a.

import wikipedia

def download_wiki_page(topic):
	page = wikipedia.page(topic, auto_suggest=False)
	file_name = f"{page.title}.txt"
	with open(file_name, "w", encoding="utf-8") as file:
		file.write(page.content)
	print(f"File '{file_name}' created with the content from the Wikipedia page '{page.title}'")

# Usage:
topic = "generative artificial intelligence"
download_wiki_page(topic)


#PE4_1.2c. and PE4_1.2d.

import wikipedia
from concurrent.futures import ThreadPoolExecutor
import time

def download_wiki_page(topic):
	page = wikipedia.page(topic, auto_suggest=False)
	file_name = f"{page.title}.txt"
	with open(file_name, "w", encoding="utf-8") as file:
		file.write(page.content)
	print(f"File '{file_name}' created with the content from the Wikipedia page '{page.title}'")

# Get the related topics
search_results = wikipedia.search("generative artificial intelligence")

# Use ThreadPoolExecutor to concurrently execute the code for each topic
start_time = time.time()

with ThreadPoolExecutor() as executor:
	futures = [executor.submit(download_wiki_page, topic) for topic in search_results]

# Wait for all the tasks to complete
for future in futures:
	future.result()

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


