budget = float(input())
videocards = int(input())
processor = int(input())
ram = int(input())

videocard_price = videocards * 250

processor_price = videocard_price*0.35
processor_price = processor_price * processor

ram_price = videocard_price*0.1
ram_price = ram_price * ram

total = videocard_price + processor_price + ram_price

if videocards > processor:
    total = total - (total*0.15)

if total > budget:
    diff = total - budget
    print(f"Not enough money! You need {diff:.2f} leva more!")
else:
    diff = budget - total
    print(f"You have {diff:.2f} leva left!")