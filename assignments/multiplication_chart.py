#hunter card, multiplication chart
for row in range(1,16):
    for collum in range(1,16):
        awnser = collum * row
        print(f"{awnser:>4}", end=" ")
    print("\n")