from random import choice

def get_positive_int_input(question):
    while True:
        answer = input(question)
        
        try:
            if int(answer) <= 0:
                print("O valor deve ser positivo.")
            else:
                return int(answer)
        except ValueError:
            print("O valor deve ser inteiro.")

people_quant = get_positive_int_input("Quantas pessoas? ")

quant = get_positive_int_input("Quantas questões? ")


people = []
for i in range(people_quant):
    name = input(f"Nome da {i+1}° pessoa: ")
    people.append({
        "name": name,
        "total": 0
    })

#total_distributed = 0

class bcolors:
    COLOR1 = '\033[95m'
    COLOR2 = '\033[96m'
    END = '\033[0m'

print("\n")
for i in range(quant-quant%people_quant):
    if i%2 == 0:
        current_color = bcolors.COLOR1
    else:
        current_color = bcolors.COLOR2

    while True:
        chosen = choice(people)
        if chosen["total"] < quant // people_quant:
            chosen["total"] += 1
            print(current_color, i+1, " - ", chosen["name"], bcolors.END)
            break

for i in range(quant-(quant%people_quant), quant):
    if i%2 == 0:
        current_color = bcolors.COLOR1
    else:
        current_color = bcolors.COLOR2

    while True:
        chosen = choice(people)
        if chosen["total"] < quant // people_quant + 1:
            chosen["total"] += 1
            print(current_color, i+1, " - ", chosen["name"], bcolors.END)
            break



print("\n")
