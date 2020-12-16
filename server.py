"""
Big Data Privacy using Fully Homomorphic Non-deterministic Encryption.
Acknowledgement: Tejashree P., Girish P.
Code By: Mayur P.
"""

from MachineLearningModel import LinModel
import phe as paillier
import json

"""
The homomorphic properties of the Paillier crypto system are:

1. Encrypted numbers can be multiplied by a non encrypted scalar.
2. Encrypted numbers can be added together.
3. Encrypted numbers can be added to non encrypted scalars.
"""


def getData():
    with open('data.json', 'r') as file:
        d = json.load(file)
    data = json.loads(d)
    return data


def computeData():
    data = getData()
    mycoef = LinModel().getCoef()
    pk = data['public_key']
    pubkey = paillier.PaillierPublicKey(n=int(pk['n']))
    enc_nums_rec = [paillier.EncryptedNumber(pubkey, int(x[0], int(x[1]))) for x in data['values']]
    results = sum([mycoef[i] * enc_nums_rec[i] for i in range(len(mycoef))])
    return results, pubkey


def serializeData():
    results, pubkey = computeData()
    encrypted_data = {}
    encrypted_data['pubkey'] = {'n': pubkey.n}
    encrypted_data['values'] = (str(results.ciphertext()), results.exponent)
    serialized = json.dumps(encrypted_data)
    return serialized


print(sum([data[i] * mycoef[i] for i in range(len(data))]))


def main():
    datafile = serializeData()
    with open('answer.json', 'w') as file:
        json.dump(datafile, file)


# Driver function
if __name__ == '__main__':
    main()
