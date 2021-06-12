"""
Bunda da csv dosyalarını deniyorum neden böyle şeyleri bu dosyaya kaydediyorsun derseniz herkes yapıodu ama ben tdd a tam hakim olmayınca böle işte.
"""


with open(r"C:\Users\fazil\Desktop\deneme.csv", "w+") as file:

    file.write("1,2,3,3,2,2")

with open(r"C:\Users\fazil\Desktop\deneme.csv", "r") as file:

    print(file.read().split(","))