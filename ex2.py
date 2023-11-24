import csv

def find_total_visits():
    visits = 0
    with open(r"./files/week-1.csv") as file1:
        rows = csv.reader(file1, delimiter = ",")
        for row in list(rows):
            for ele in row:
                if (ele.strip() == "1"):
                    visits += 1
    with open(r"./files/week-2.csv") as file2:
        rows = csv.reader(file2, delimiter = ",")
        for row in list(rows):
            for ele in row:
                if (ele.strip() == "1"):
                    visits += 1
    with open(r"./files/week-3.csv") as file3:
        rows = csv.reader(file3)
        for row in list(rows):
            for ele in row:
                if (ele.strip() == "1"):
                    visits += 1
    print(visits)
    return visits


def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")


ex2()