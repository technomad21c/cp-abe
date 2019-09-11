from charm.toolbox.pairinggroup import PairingGroup
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
import pickle

if __name__ == "__main__":
    groupObj = PairingGroup('SS512')
    cpabe = CPabe_BSW07(groupObj)
    hyb_abe = HybridABEnc(cpabe, groupObj)
    (pk, mk) = hyb_abe.setup()
    access_policy = '((four or three) and (two or one))'
    sk = hyb_abe.keygen(pk, mk, ['ONE', 'TWO', 'THREE'])
    print(sk)
    plaintext = "Bounty Name: EMR Functional Testing"

    ciphertext = hyb_abe.encrypt(pk, plaintext, access_policy)
    print(ciphertext)
    ciphertext["c1"]["C"] = groupObj.serialize(ciphertext["c1"]["C"])
    for key in ciphertext["c1"]["Cy"] :
        ciphertext["c1"]["Cy"][key] = groupObj.serialize(ciphertext["c1"]["Cy"][key])
    ciphertext["c1"]["C_tilde"] = groupObj.serialize(ciphertext["c1"]["C_tilde"])
    for key in ciphertext["c1"]["Cyp"] :
        ciphertext["c1"]["Cyp"][key] = groupObj.serialize(ciphertext["c1"]["Cyp"][key])

    ciphertext2 = ciphertext
    ciphertext2["c1"]["C"] = groupObj.deserialize(ciphertext["c1"]["C"])
    for key in ciphertext2["c1"]["Cy"]:
        ciphertext2["c1"]["Cy"][key] = groupObj.deserialize(ciphertext2["c1"]["Cy"][key])
    ciphertext2["c1"]["C_tilde"] = groupObj.deserialize(ciphertext2["c1"]["C_tilde"])
    for key in ciphertext2["c1"]["Cyp"]:
        ciphertext2["c1"]["Cyp"][key] = groupObj.deserialize(ciphertext2["c1"]["Cyp"][key])
    print(hyb_abe.decrypt(pk, sk, ciphertext2) == plaintext)

