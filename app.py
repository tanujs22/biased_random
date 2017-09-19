import numpy

def biased_rand():
	for_prob = int(numpy.random.rand()*100)
	if for_prob<73:
		return (int(numpy.random.rand()*100)%5)+5
	else:
		return int(numpy.random.rand()*100)%5


print biased_rand()