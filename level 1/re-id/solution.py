def solution(i):
	primes = ''
	upper = 20500

	for num in range(0, upper):
		if num > 1:
			for j in range(2, num):
				if (num % j) == 0:
					break
			else:
				primes = primes + str(num)
				if len(primes) >= 10006:
					break

	id = ''
	while (len(id) < 5):
		id = id + primes[i]
		i = i + 1

	return id