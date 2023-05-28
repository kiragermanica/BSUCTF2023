from factordb.factordb import FactorDB
import hashlib

n = 111952518932119
e = 0x10001
c = 76158259501553

f = FactorDB(n)
f.connect()
p, q = f.get_factor_list()

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = str(pow(c, d, n)).encode()

hash_object = hashlib.sha256(m)
sha256m = hash_object.hexdigest()

print('bsuctf{' + sha256m + '}')
