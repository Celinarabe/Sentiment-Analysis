# original data source: http://jmcauley.ucsd.edu/data/amazon/

import json
import random
import string

data = []
file_name = 'Beauty'

# select only reviews from 2012 or later
with open(f'reviews_{file_name}_5.json', 'r') as f:
	for line in f:
		review = json.loads(line)
		year = int(review['reviewTime'].split(' ')[-1])
		if year >= 2012:
			data.append(review)

# select 2000 random reviews
data_2000 = random.sample(data, 2000)

print(len(data_2000))
print(data_2000[0:3])

# convert to all lowercase and strip punctuation
for x in data_2000:
	no_punc = x['reviewText'].translate(str.maketrans('', '', string.punctuation))
	lower_case = no_punc.lower()
	x['reviewText'] = lower_case


# export cleaned to file
with open(f'{file_name}_review_data.json', 'w') as f:
	for review in data_2000:
		f.write(json.dumps(review)+'\n')


