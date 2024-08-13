
import re

# Open the input file and read its contents
with open("Taerel14April2023.xml", "r") as f:
    text = f.read()

# Use regular expressions to extract the text content of each page
pattern = re.compile("<text.*?>(.*?)</text>", re.DOTALL)
text_content_list = pattern.findall(text)

# Write the extracted text to the output file
with open("taerelwikitextstage1.txt", "w") as f:
    for text_content in text_content_list:
        # Remove any remaining XML tags and whitespace
        text_content = re.sub("<.*?>", "", text_content).strip()

        # Write the extracted text to the output file
        if text_content:
            f.write(text_content + "\n")
