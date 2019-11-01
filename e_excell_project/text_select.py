import re
info = open("XX.txt", "r").read()
sentences = []
keywords = ["sale","sold","sell", "discount"]
for sentence in re.split(r"[\.\?\!\n]+", info):
    if any(keyword in sentence.lower() for keyword in keywords):
        sentences.append(sentence)
with open("W.txt", "a+") as f:
    f.write("\n".join(sentences))

#open and read after

f = open("W.txt", "r")
print(f.read())
