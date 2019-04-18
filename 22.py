if __name__ == "__main__":
    file_name = "language.txt"
    with open(file_name, 'r', encoding="utf-8") as f:
        print(f.readline())
    ls = [1, 2, 3, 4]
    for idx in range(len(ls)):
        ls[idx] = ls[idx]**2

    for i, l in enumerate(ls):
        ls[i] = l ** 2
    ls = [x**2 for x in ls]
    print(ls)
