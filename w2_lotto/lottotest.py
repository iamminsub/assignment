lotto_list = []
import random	
while len(lotto_list) < 6:
	ball = random.randint(1,35)
	lotto_list.append(ball)
	lotto_list = list(set(lotto_list))
else:
	print sorted(lotto_list)