energy = {"calorie": 0,
          "proteins": 0,
          "carbs": 0,
          "fat": 0}
weight = 0
while True:
    data = input("Enter weight, calories, proteins, carbs, fat \nOr 'x' to calculate result\n")
    if data == 'x':
        print(f"\nTotal weight: {weight}g")
        print("\nFood energy")
        for x, y in energy.items():
            print(f"{x} - {y}g")
        break
    w, cal, p, c, f = map(float, data.split())
    weight += w
    energy["calorie"] += cal
    energy["proteins"] += p
    energy["carbs"] += c
    energy["fat"] += f

