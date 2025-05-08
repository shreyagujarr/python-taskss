number_list = []

for x in range(1, 11):
  number_list.append(x)

print(f"Original list: {number_list}")

extracted_list = []

for x in range(0, 5):
  extracted_list.append(number_list[x])

print(f"Extracted first five elements: {extracted_list}")

reversed_list = extracted_list.reverse()
print(f"Reversed extracted elements: {extracted_list}")