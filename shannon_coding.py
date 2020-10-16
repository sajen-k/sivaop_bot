import utils
from formulas import *

def shannon(probabilities):
    try:
        answer = {}
        answer['idx_to_bin'] = {}
        probabilities.sort(reverse=True)
        for i in range(len(probabilities)):
            answer['idx_to_bin'][i] = ''
        utils.separate(probabilities, answer['idx_to_bin'])

    except Exception as e:
        return e

    return answer
    
if __name__ == '__main__':
    probs = input("Enter probabilities: ")
    probs = list(map(float, probs.split()))
    answer = shannon(probs)

    answer['idx_to_len'] = {k: len(v) for k,v in answer['idx_to_bin'].items()}
    answer['Entropy'] = entropy(probs)
    answer['Average length'] = Lavg(probabilities=probs, lengths=answer['idx_to_len'].values())
    answer['Efficiency'], answer['Redundancy'] = efficiency_redundancy(answer['Entropy'], answer['Average length'])
    answer['Code Variance'] = code_variance(probs=probs, lengths=answer['idx_to_len'].values(), lavg=answer['Average length'])

    for prob, bin, length in zip(probs, answer['idx_to_bin'].values(), answer['idx_to_len'].values()):
        print(prob, '\t', bin, '\t', length)

    for k, v in answer.items():
        print(k + ':', v) if k not in ['idx_to_bin', 'idx_to_len'] else None