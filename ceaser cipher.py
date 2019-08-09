def cs(pt,key):
      al='abcdefghijklmnopqrstuvwxyz'
      en=''
      for l in pt.lower():
            k=(al.index(l)+key)%26
            en+=al[k]
      print("Encrypted Text",en)

      de=''
      for l in en:
            k=(al.index(l)-key)%26
            de+=al[k]
      print("Decrypted Text",de)

pt=input("Enter some text:")
key=int(input("Enter a key:"))
cs(pt,key)
