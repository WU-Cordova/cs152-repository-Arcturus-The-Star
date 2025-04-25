import sys
import pickle

def main():
    with open(sys.argv[1], "rb") as file:
        drink_totals = pickle.loads(file.read())
    print(f"Report for {" at ".join(sys.argv[1].split("\\")[-1].split(".")[0].split("_")[-2:])}:\nDrink - Total Sold - Total Revenue\n{"\n".join([f"{i.capitalize()} - {drink_totals[i][0]} - {drink_totals[i][1]}" for i in drink_totals])}\nTotal revenue: ${str(round(sum([drink_totals[i][1] for i in drink_totals]), 2))}")

if __name__ == "__main__":
    main()