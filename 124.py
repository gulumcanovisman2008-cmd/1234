adamlar = {}

with open("adamlar.txt", "w") as f:
    while True:
        ad = input().strip()
        if ad.upper() == "DONE":
            break
        adamlar[ad.upper()] = True

    for ad in adamlar:
        f.write(ad + "\n")

print(adamlar)
