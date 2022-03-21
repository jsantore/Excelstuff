import openpyxl


def get_excel_sheet(filename):
    income_excel = openpyxl.load_workbook(filename)
    data_sheet = income_excel.active
    return data_sheet


def main():
    income_data_sheet = get_excel_sheet("MedianIncomeByStateCensusGov.xlsx")
    examine_data(income_data_sheet)

def examine_data(income_sheet):
    for row in income_sheet.rows:
        first_cell = row[0]
        print(first_cell.value)


main()