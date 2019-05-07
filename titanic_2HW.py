# Решение

# импорт необходимых библиотек для работы
import pandas as pd

# создаём DataFrame
df = pd.read_csv('train.csv')

# группируем людей по портам отправления и считаем их
# отдельно для каждого порта
cnt = (df.groupby(['Embarked'])['PassengerId'].count())

# выводим количество людей для каждого порта через пробел
for summ in list(cnt):
    print (summ, end = ' ')