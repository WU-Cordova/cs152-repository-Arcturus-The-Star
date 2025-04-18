import json
import sys

def main():
    file = open(sys.argv[1])
    drink_totals = json.load(file)
    print(f"Report for {" at ".join(sys.argv[1].split("\\")[-1].split(".")[0].split("_")[-2:])}:\nDrink - Total Sold - Total Revenue\n{"\n".join([f"{i.capitalize()} - {drink_totals[i][0]} - {drink_totals[i][1]}" for i in drink_totals])}\nTotal revenue: ${str(round(sum([drink_totals[i][1] for i in drink_totals]), 2))}")

if __name__ == "__main__":
    main()