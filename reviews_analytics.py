data = []  #first list is data, with 100000 reviews
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
		    print(len(data))
print('Reviews have been extracted with a total of', len(data), 'reviews')
print('------------------')

sum_len = 0
for d in data:
	sum_len += len(d)
print('The average length of each review is', sum_len/len(data))

new = [] #second list is sorted data, with 20000 reviews which have < 100 words
for d in data:
	if len(d) < 100:
		new.append(d)
print(len(new), 'reviews have less than 100 words.')
print(new[0])