import openpyxl
import numbers
import openpyxl.utils
import plotly.graph_objects
from state_abbrev import us_state_to_abbrev


def get_excel_sheet(filename):
    income_excel = openpyxl.load_workbook(filename)
    data_sheet = income_excel.active
    return data_sheet


def main():
    income_data_sheet = get_excel_sheet("MedianIncomeByStateCensusGov.xlsx")
    examine_data(income_data_sheet)

def examine_data(income_sheet):
    #answer = int(input("What is the cutoff for income growth"))
    #print(f"States Whose Median Income Grew more than {answer} in 2015-2020")
    list_of_state_abrev = []
    list_of_income_changes = []
    for row in income_sheet.rows:
        first_cell = row[0]
        income_cell = row[1]
        income_value = income_cell.value
        if not isinstance(income_value, numbers.Number):
            continue
        if first_cell.value not in us_state_to_abbrev:
            continue
        state_name = first_cell.value
        state_abrev = us_state_to_abbrev[state_name]
        list_of_state_abrev.append(state_abrev)
        income2015_cell_number = openpyxl.utils.cell.column_index_from_string('n')-1
        income2015_cell = row[income2015_cell_number]
        income2015 = income2015_cell.value
        income_change = income_value - income2015
        list_of_income_changes.append(income_change)
        # income_chance_percent = income_change/income_value
        # income_chance_percent = income_chance_percent *100

    map_to_show = plotly.graph_objects.Figure(
        data=plotly.graph_objects.Choropleth(
            locations= list_of_state_abrev,
            z= list_of_income_changes,
            locationmode="USA-states",
            colorscale='Picnic',
            colorbar_title="amount of income"
        )
        )
    map_to_show.update_layout(
        title_text= "Income Change 2015 to 2020",
        geo_scope="usa"
    )
    map_to_show.show()

#old stuff below
        # if income_value-income2015 > answer:
        #     print(f"{first_cell.value} : {income_value} old 2105 income {income2015}")


main()