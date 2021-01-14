'''
TASK:

Given a list and a number n, create a new list that contains each number of list at most n times without reordering. For example if n=2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drope the next [1,2] since this would lead to 1 and 2 being in the result 3 times and then take 3, which leads to [1,2,3,1,2,3].
'''

list = [1, 2, 3, 1, 2, 1, 2, 3]
n = 2

'''
SOLUTION 1:
- Advantage: shorter code and lower storage costs
- Disadvantage: A runtime of Θ(len(result)) to look up the current count 
'''

result = []

for x in list:
	if result.count(x) < n:
		result.append(x)

print(result)

'''
SOLUTION 2:
- Advantage: it scales better in case of runtime since the lookup of the current count is working in an average of O(1) now (amortized worst case is still O(n) (https://stackoverflow.com/a/1963529/8924689))
- Disadvantage: it takes more storage since you need another dict and the code gets a bit longer
'''

result = []
count = {}

for x in list:
  if x not in count:
    count[x] = 0;
  if count[x] < n:
    result.append(x)
    count[x] += 1

print(result)