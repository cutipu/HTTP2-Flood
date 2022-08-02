import os
c = input("Choose your environment: [0] pip / [1] pip3 : ")

if c == "0":
    os.system("pip install httpx")
    os.system("pip install httpx[socks]")
elif c == "1":
    os.system("pip3 install httpx[socks]")
    os.system("pip3 install httpx")

if os.name == "nt":
    pass
else:
    pass
print("Done.")
