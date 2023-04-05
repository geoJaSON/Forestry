from openpyxl import load_workbook
xls = r""
wb = load_workbook('names.xlsx')
ws = wb['Sheet1']
ws['A1'] = 'A1'
wb.save(f"{ContractTitle} Abstract of Bids.xlsx")
