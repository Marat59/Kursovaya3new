import os.path

from utils import read_file, sort_state, sort_5_operatons, change_date, masked_number


def main():
    oper = read_file(os.path.join('operations.json'))
    last_operation = sort_state(oper)
    filted = sort_5_operatons(last_operation)
    for i in filted:
        car = change_date(i['date'])
        transaction = i['description']
        try:
            from_322 = masked_number(i['from'])
        except KeyError:
            from_322 = "no information"
        try:
            to_322 = masked_number(i['to'])
        except KeyError:
            to_322 = "no information"
        summa = i['operationAmount']['amount']
        valuta = i['operationAmount']['currency']['name']

        print(f'{car} {transaction}\n{from_322} -> {to_322}\n{summa} {valuta}')
        print(" ")
    return

main()