import math

def entropy(probabilities):
	return sum([p * information(p) for p in probabilities])

def information(p):
	return math.log(1/p, 2)

def Lavg(*, probabilities, lengths):
	return sum([i*j for i,j in zip(probabilities, lengths)])

def efficiency(entropy_h, lavg):
	return entropy_h/lavg

def redundancy(efficiency):
	return 1 - efficiency

def code_variance(*, probs, lengths, lavg):
	return sum([p * (l - lavg)**2 for p, l in zip(probs, lengths)])