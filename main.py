homerseklet = [0, 12, 13, 9, 2, 7]

i = 1
while i < len(homerseklet):
    if (homerseklet[i - 1] > homerseklet[i] + 3):
        print(f"Október {i + 1}. - {homerseklet[i - 1]} => {homerseklet[i]}")
    i += 1

