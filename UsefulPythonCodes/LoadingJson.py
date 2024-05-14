import json

# Opening JSON file
f = open('mastodon_closed_36.json')

# returns JSON object as
# a dictionary
data = json.load(f)

number = 28


print("First request: ")
print("Request Number: ", data[number]["Request Number"])
print("Title: ", data[number]["Title"])
print("Author: ", data[number]["Author"])
print("Posted Time: ", data[number]["Posted Time"])
print("Initial Comment: ", data[number]["Initial Comment"])
print("Number of Comments: ", data[number]["Number of comments"])
print("All Comments: ", data[number]["All Comments"])
print("--------------------- Discussion --------------------------------")
for i, comment in enumerate(data[number]["All Comments"]):
    print("Comment No: ", i)
    print(comment['Text: '])
    print("-------------------------------------")

# 70 - 160 - 72 - 115 - 50
# 150 - 117 - 161 - 76 -



