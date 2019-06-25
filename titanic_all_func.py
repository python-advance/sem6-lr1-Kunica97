import pandas as pd

df = pd.read_csv('train.csv')
data = pd.read_csv('train.csv', usecols=['Name', 'Age'])

def titanic2 (df):
    '''
    Вывод количества людей по портам
    '''
    print('Задание 2')
    cnt = (df.groupby(['Embarked'])['PassengerId'].count())

    for summ in list(cnt):
        print(summ, end=' ')
    print()

def titanic4 (df):
    '''
    Функция для выполнения 4 домашнего задания по титанику
    '''
    print('Задание 4')
    def procent(x):
        '''
        функция для расчета доли пассажиров 1, 2 и 3 классов
        '''
        a = 0
        for sum in x:
            a = a + sum
        for cnt in x:
            print("%.2f" % (cnt / a), end=' ')
        print()

    cnt = list((df.groupby(['Pclass'])['PassengerId'].count()))
    procent(cnt)

def titanic6 (df):
    '''
    Функция для расчета корреляции между:
    - возрастом и параметром survival;
    - полом человека и параметром survival;
    - классом, в котором пассажир ехал, и параметром survival.
    '''
    print('Задание 6')
    sex = list(df['Sex'])
    ln = len(sex)

    # Замещаем male и female на 1 и 0 соответственно
    for i in range(ln):
        if sex[i] == 'male':
            sex[i] = 1
        else:
            sex[i] = 0

    # Преобразуем в DataFrame
    sx = pd.DataFrame({'Sex': sex})

    print(df['Age'].corr(df['Survived']))
    print(sx['Sex'].corr(df['Survived']))
    print(df['Pclass'].corr(df['Survived']))

def titanic8 (df):
    '''
    Функция для расчета средней цены и медианы
    '''
    print('Задание 8')
    md = df['Fare'].median()
    mn = df['Fare'].mean()
    print(md, mn)

def titanic10 (df, data):
    '''
    Функция для нахождения самых популярных
    мужских и женских имен людей, старше 15 лет на корабле
    '''
    print('Задание 10')
    na = df[df.Age > 15][['Sex', 'Name', 'Age']]
    fe = na[na.Sex == 'female'][['Name', 'Age']]

    ma = na[na.Sex == 'male'][['Name', 'Age']]
    ma = pd.DataFrame(ma.Name.str.split(' ', 1).tolist())

    fe = pd.DataFrame(fe.Name.str.split(' ', 1).tolist())

    # fe[0] - исследуем столбик с именем, index[0] - выводит первый элемент
    print(fe[0].value_counts().index[0], ma[0].value_counts().index[0])

titanic2(df)
titanic4(df)
titanic6(df)
titanic8(df)
titanic10(df, data)