import openpyxl
import numbers


def get_excel_sheet(filename):
    income_excel = openpyxl.load_workbook(filename)
    data_sheet = income_excel.active
    return data_sheet


def main():
    income_data_sheet = get_excel_sheet("MedianIncomeByStateCensusGov.xlsx")
    examine_data(income_data_sheet)

def examine_data(income_sheet):
    answer = int(input("What is the cutoff for income growth"))
    print(f"States Whose Median Income Grew more than {answer} in 2015-2020")
    for row in income_sheet.rows:
        first_cell = row[0]
        income_cell = row[1]
        income_value = income_cell.value
        if not isinstance(income_value, numbers.Number):
            continue
        income2015_cell = row[13]
        income2015 = income2015_cell.value
        if income_value-income2015 > answer:
            print(f"{first_cell.value} : {income_value} old 2105 income {income2015}")


main()