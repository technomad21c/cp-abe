from charm.toolbox.pairinggroup import PairingGroup, GT
from bsw07 import BSW07

# instantiate a bilinear pairing map
# 'MNT224' represents an asymmetric curve with 224-bit base field
pairing_group = PairingGroup('MNT224')
    
# CP-ABE under DLIN (2-linear)
cpabe = BSW07(pairing_group, 2)

# run the set up
(pk, msk) = cpabe.setup()
# choose a random message pretend to be public's record of bounty
# public = pairing_group.random(GT)
public = "plain text"
print(public)

# public = "bounty name: EMR functional testing"
# choose a random message pretend to be private's record of bounty
private1 = pairing_group.random(GT)
# choose a random message pretend to be private 2 record of bounty
private2 = pairing_group.random(GT)
# enrypt  public data with policy1
policy_str1 = '(SKILL and CATEGORY)'
ctxt1 = cpabe.encrypt(pk, public, policy_str1)
# enrypt private1 with policy2
policy_str2 = '(BOUNTYID)'
ctxt2 = cpabe.encrypt(pk, private1, policy_str2)
# enrypt private2  with policy3
policy_str3 = '(CONTRACTID1 or CONTRACTID2 or CONTRACTID3 or CONTRACTID4) '
ctxt3 = cpabe.encrypt(pk, private2, policy_str3)


def stage1():
  # Stage 1:
    #generate a Tester1 key
  tester1_attr_list = ['SKILL', 'CATEGORY']
  tester1_key = cpabe.keygen(pk, msk, tester1_attr_list)


  # decryption as Tester1
  rec_msg = cpabe.decrypt(pk, ctxt1, tester1_key)
  if (rec_msg == public):
    print ("Decrypt as Tester1 ===> ", rec_msg)
  else:
    print ("Decryption as a Tester1 failed.")
  print(public)

def stage2():
  # Stage 2:
  myList = ["JOHN", "DAVID", "WANG", "JIA", "GAIL"]
  name = input("Please input your name:")
  tester1_key = None
  for x in myList:
    if (name == x):
      #generate a Tester1 key
      tester1_attr_list = ['SKILL', 'CATEGORY','BOUNTYID']
      tester1_key = cpabe.keygen(pk, msk, tester1_attr_list)

  #generate a Tester2 key
  tester2_attr_list = ['SKILL', 'CATEGORY']
  tester2_key = cpabe.keygen(pk, msk, tester2_attr_list)

  # decryption as Tester1 of public
  rec_msg = cpabe.decrypt(pk, ctxt1, tester1_key)
  if (rec_msg == public):
    print ("decryption as Tester1 of public")
  else:
    print ("Decryption as a Tester1 of public data failed.")
  # decryption as Tester2 of public
  rec_msg = cpabe.decrypt(pk, ctxt1, tester2_key)
  if (rec_msg == public):
    print ("Decrypt as Tester2 of public")
  else:
    print ("Decryption as a Tester2 of public failed.")
  # decryption as Tester1 of private1
  rec_msg = cpabe.decrypt(pk, ctxt2, tester1_key)
  if (rec_msg == private1):
    print ("Decrypt as Tester1 of private1")
  else:
    print ("Decryption as a Tester1 of private1 failed.")
  # decryption as Tester2 of private1
  rec_msg = cpabe.decrypt(pk, ctxt2, tester2_key)
  if (rec_msg == private1):
    print ("Decrypt as Tester2 of private1")
  else:
    print ("Decryption as a Tester2 of private1 failed.")

def stage3():
  # Stage 3:
    #generate a Tester1 key
  tester1_attr_list = ['SKILL', 'CATEGORY','BOUNTYID']
  tester1_key = cpabe.keygen(pk, msk, tester1_attr_list)
    #generate a Tester2 key
  tester2_attr_list = ['SKILL', 'CATEGORY','CONTRACTID1']
  tester2_key = cpabe.keygen(pk, msk, tester2_attr_list)
    #generate a Tester3 key
  tester3_attr_list = ['CONTRACTID2']
  tester3_key = cpabe.keygen(pk, msk, tester3_attr_list)

  # decryption as Tester1 of public
  rec_msg = cpabe.decrypt(pk, ctxt1, tester1_key)
  print ("public")
  if (rec_msg == public):
    print ("Decrypt as Tester1")
  else:
    print ("Decryption as a Tester1 failed.")
  # decryption as Tester2 of public
  rec_msg = cpabe.decrypt(pk, ctxt1, tester2_key)
  if (rec_msg == public):
    print ("Decrypt as Tester2")
  else:
    print ("Decryption as a Tester2 failed.")
  # decryption as Tester3 of public
  rec_msg = cpabe.decrypt(pk, ctxt1, tester3_key)
  if (rec_msg == public):
    print ("Decrypt as Tester3")
  else:
    print ("Decryption as a Tester3 failed.")
  print ("private1")
  # decryption as Tester1 of private1
  rec_msg = cpabe.decrypt(pk, ctxt2, tester1_key)
  if (rec_msg == private1):
    print ("Decrypt as Tester1")
  else:
    print ("Decryption as a Tester1 failed.")
  # decryption as Tester2 of private1
  rec_msg = cpabe.decrypt(pk, ctxt2, tester2_key)
  if (rec_msg == private1):
    print ("Decrypt as Tester2")
  else:
    print ("Decryption as a Tester2 failed.")
  # decryption as Tester3 of private1
  rec_msg = cpabe.decrypt(pk, ctxt2, tester3_key)
  if (rec_msg == private1):
    print ("Decrypt as Tester3")
  else:
    print ("Decryption as a Tester3 failed.")
  print ("private2")
  # decryption as Tester1 of private2
  rec_msg = cpabe.decrypt(pk, ctxt3, tester1_key)
  if (rec_msg == private2):
    print ("Decrypt as Tester1")
  else:
    print ("Decryption as a Tester1 failed.")
  # decryption as Tester2 of private2
  rec_msg = cpabe.decrypt(pk, ctxt3, tester2_key)
  if (rec_msg == private2):
    print ("Decrypt as Tester2")
  else:
    print ("Decryption as a Tester2 failed.")
  # decryption as Tester3 of private2
  rec_msg = cpabe.decrypt(pk, ctxt3, tester3_key)
  if (rec_msg == private2):
    print ("Decrypt as Tester3")
  else:
    print ("Decryption as a Tester3 failed.")


def main():
  stage = int(input("IN which stage do you wanna enter: "))
  if stage == 1:
    stage1()
  elif stage == 2:
    stage2()
  elif stage == 3:
    stage3()

if __name__ == "__main__":
    main()
