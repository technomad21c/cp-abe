from charm.toolbox.pairinggroup import PairingGroup
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
import json
import pickle

if __name__ == "__main__":
    groupObj = PairingGroup('MNT224')
    cpabe = CPabe_BSW07(groupObj)
    hyb_abe = HybridABEnc(cpabe, groupObj)
    (pk, mk) = hyb_abe.setup()
    print("*********************************************")
    for key in pk.keys():
        print(key + ": " + str(pk.get(key)))
    print("*********************************************")

    print("*********************************************")
    access_policy = '((FOUR or three) and (two or one))'
    plaintext = "Bounty Name: EMR Functional Testing"
    attr_list = ['ONE', 'FOUR']
    ciphertext = hyb_abe.encrypt(pk, plaintext, access_policy)
    sk = hyb_abe.keygen(pk, mk, attr_list)
    try:
        dt = hyb_abe.decrypt(pk, sk, ciphertext).decode('utf-8')
    except:
        print("failed to decrypt")
    else:
        if (dt == plaintext):
            print(dt)