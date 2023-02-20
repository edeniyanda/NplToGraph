import json
import matplotlib.pyplot as plt

# Load the data from the JSON file
with open('npl_tst_recep.json') as f:
    data = json.load(f)

# Extract the keys and values for each response
responses = data['results']
keys = []
values = []
for response in responses:
    for k, v in response.items():
        if isinstance(v, dict):
            for sub_k, sub_v in v.items():
                keys.append(k + '.' + sub_k)
                values.append(sub_v)
        else:
            keys.append(k)
            values.append(v)

# Create a horizontal bar chart of the key-value pairs
fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(range(len(keys)), [str(value) for value in values])
ax.set_yticks(range(len(keys)))
ax.set_yticklabels(keys, fontsize=10)
ax.set_xlabel('Values')
ax.set_title('Key-Value Pairs by Response')
plt.show()

