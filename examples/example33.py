import random
x=random.randint(1,100)
while True:
    tahmin = (int(input("""kendileride dahil olarak 1 ve 100 arasında bir sayı tahmin edin :""")))
    if x == tahmin:
        print("""TEBRİKLER SAYIYI BULDUN""")
        break
    else:
        print("""TEKRAR DENEYiN""")
        pass
