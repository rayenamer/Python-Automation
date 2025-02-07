import fitz

with fitz.open("students.pdf") as pdf:
  text = ''
  for page in pdf:
    text = text + page.get_text()
    print(text)

import tabula

table = tabula.read_pdf('weather.pdf', pages=1)

print(type(table[0]))

table[0].to_csv('output.csv', index=None)