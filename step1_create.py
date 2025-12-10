from openpyxl import Workbook

# создаём новую книгу
wb = Workbook()

# выбираем активный лист
#ws = wb.active

# записываем текст в ячейку A1
#ws["A1"] = "Привет, Excel!"
#wb.create_sheet(title='Книга 0', index=0)
list_s = ['A','B','C']
for i in list_s:
    wb.create_sheet(i)
# сохраняем файл
wb.save("Проверка.xlsx")
print(wb.sheetnames)
