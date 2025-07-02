import requests

url = "http://127.0.0.1:5000/detect"
input_path = input("Enter the input file: ")
# Step 1: Read the input text file
with open(input_path, "r") as file:
    input_text = file.read()

# Print the original input content
print("\nORIGINAL INPUT TEXT:")
print(input_text)

data = {"text": input_text}
response = requests.post(url, json=data)

#Check if API request
if response.status_code == 200:
    sanitized_data = response.json()
    sanitized_text = sanitized_data["redacted_text"]

    # Print the sanitized output content
    print("\nSANITIZED OUTPUT TEXT:")
    print(sanitized_text)

    # Save output
    with open("output.txt", "w", encoding="utf-8") as output_file:
        output_file.write(sanitized_text)
    
    print("\nFinished! Saved output")
else:
    print(f"\n Error: Unable to sanitize text. Status Code: {response.status_code}")
    print(response.text)
