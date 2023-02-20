while True:
    print("Введитое год:")
    year = int(input())
    norm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,]
    ves = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,]
    rez = 0
    if ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0) :
        for i in range(12):
            for j in range(ves[i] +1):
                if 0 < j < 10:
                    rez += j
                elif j >= 10:
                    x = [int(a) for a in str(j)]
                    for k in range(2):
                        rez += x[k]
        print(rez)
    else:
        for i in range(12):
            for j in range(norm[i] +1):
                if 0 < j < 10:
                    rez += j
                elif j >= 10:
                    x = [int(a) for a in str(j)]
                    for k in range(2):
                        rez += x[k]
        print(rez)