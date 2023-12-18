import sys
import os
import requests

def request_minifier(_text):
	response = requests.post('https://www.toptal.com/developers/javascript-minifier/api/raw', data=dict(input=_text)).text
	return response

def minifier(source_dir, output_dir):
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)
	for file_path in os.listdir(source_dir):
		source_path = os.path.join(source_dir, file_path)
		destination_path = os.path.join(output_dir, file_path)
		if os.path.isfile(source_path):
			print(source_path)
			# call minifier call function
			source_file=open(source_path,"r")
			source_text = source_file.read()
			source_file.close()
			destination_text = request_minifier(source_text)
			destination_file = open(destination_path, "w")
			destination_file.write(destination_text)
			destination_file.close()

		if os.path.isdir(source_path):
			minifier(source_path, destination_path)

if __name__ == '__main__':
	source = sys.argv[1]
	dest = sys.argv[2]
	minifier(source, dest)