sınav1 = int(input("birinci dönem birinci sınav notunuzu girin:"))
sınav2 = int(input("ikinci dönem ikinci sınav notunuzu girin:"))
sınav3 = int(input("ikinci dönem birinci sınav notunuzu girin:"))
sınav4 = int(input("ikinci dönem ikinci sınav notunuzu girin:"))
trmi = str(input("ders türkçe mi(E/H) :"))
ortalama1 = (sınav1 + sınav2)/2
ortalama2 = (sınav3 + sınav4)/2
genelortalama = (ortalama1+ortalama2)/2
if trmi==("H") :
    if ortalama1>50:
                print(f"""birinci dönemi  {ortalama1} ortalama ile geçtiniz.""")
    else:
                print(f"""birinci dönemden {ortalama1} ortalama ile kaldınız""")
    if ortalama2>50:
                print(f"""2.dönemi {ortalama2} ortalama ile geçtiniz.""")
    else:
                print(f"""ikinci dönemden {ortalama2} ortalama ile kaldınız""")
    if genelortalama>50:
                print(f"""bu yılı {genelortalama} ortalama ile geçtiniz.""")
    else:
                print(f"""bu yıldan {genelortalama} ortalama ile kaldınız""")
if trmi==("h") :
    if ortalama1>50:
                print(f"""birinci dönemi  {ortalama1} ortalama ile geçtiniz.""")
    else:
                print(f"""birinci dönemden {ortalama1} ortalama ile kaldınız""")
    if ortalama2>50:
                print(f"""2.dönemi {ortalama2} ortalama ile geçtiniz.""")
    else:
                print(f"""ikinci dönemden {ortalama2} ortalama ile kaldınız""")
    if genelortalama>50:
                print(f"""bu yılı {genelortalama} ortalama ile geçtiniz.""")
    else:
                print(f"""bu yıldan {genelortalama} ortalama ile kaldınız""")
if trmi==("E") :
    if ortalama1>70:
                print(f"""birinci dönemi  {ortalama1} ortalama ile geçtiniz.""")
    else:
                print(f"""birinci dönemden {ortalama1} ortalama ile kaldınız""")
    if ortalama2>70:
                print(f"""2.dönemi {ortalama2} ortalama ile geçtiniz.""")
    else:
                print(f"""ikinci dönemden {ortalama2} ortalama ile kaldınız""")
    if genelortalama>70:
                print(f"""bu yılı {genelortalama} ortalama ile geçtiniz.""")
    else:
                print(f"""bu yıldan {genelortalama} ortalama ile kaldınız""")
if trmi==("e") :
    if ortalama1>70:
                print(f"""birinci dönemi  {ortalama1} ortalama ile geçtiniz.""")
    else:
                print(f"""birinci dönemden {ortalama1} ortalama ile kaldınız""")
    if ortalama2>70:
                print(f"""2.dönemi {ortalama2} ortalama ile geçtiniz.""")
    else:
                print(f"""ikinci dönemden {ortalama2} ortalama ile kaldınız""")
    if genelortalama>70:
                print(f"""bu yılı {genelortalama} ortalama ile geçtiniz.""")
    else:
                print(f"""bu yıldan {genelortalama} ortalama ile kaldınız""")
