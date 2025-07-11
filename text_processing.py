with open ("text.txt","r") as fd:
    inner_content = fd.read()
    # print(inner_content)
    
# paras = inner_content.split("\n\n")

# print(len(paras))

# lines = inner_content.split("\n")

# print(len(lines))

# words = inner_content.split(" ")

# print(len(words))

cite_cleaned = inner_content
for i in range(7, 20):
    cite_cleaned = cite_cleaned.replace(f"[{i}]", "")
print(cite_cleaned)


