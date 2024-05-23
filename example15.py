import random

def rastgele_renk():
    renkler = ['kırmızı', 'mavi', 'yeşil', 'sarı', 'mor', 'turuncu', 'pembe', 'siyah', 'beyaz']
    return random.choice(renkler)

secilen_renk = rastgele_renk()
print("SANA UYAN RENK:", secilen_renk)
