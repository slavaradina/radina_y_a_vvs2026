import pandas as pd
import numpy as np

print("часть 2")

#6
df = pd.read_csv('tested.csv')

#7
try:
    n_input = input("введите количество строк для вывода: ")
    n = int(n_input) if n_input.strip() else 5
except EOFError:
    n = 5
print(f"\n первые {n} строк таблицы:")
print(df.head(n))

#8
print("\n последние 5 строк таблицы:")
print(df.tail(5))

#9
rows, cols = df.shape
print(f"\n количество строк: {rows}, столбцов: {cols}")

#10
print("\n названия всех столбцов:")
print(df.columns.tolist())

#11
print("\n типы данных каждого столбца:")
print(df.dtypes)

#12
numeric_features = ['Age', 'SibSp', 'Parch', 'Fare']
categorical_features = ['Survived', 'Pclass', 'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
id_features = ['PassengerId']
print("числовые признаки:", numeric_features)
print("категориальные признаки:", categorical_features)
print("технический идентификатор:", id_features)

#13
print("\n статистика числовых признаков:")
stats_summary = pd.DataFrame({
    'среднее': df[numeric_features].mean(),
    'медиана': df[numeric_features].median(),
    'минимум': df[numeric_features].min(),
    'максимум': df[numeric_features].max(),
    'ст. отклонение': df[numeric_features].std()
})
print(stats_summary.round(4))

#14
print("\n количество пассажиров каждого класса:")
print(df['Pclass'].value_counts().sort_index())

#15
print("\n количество уникальных значений в Embarked:", df['Embarked'].nunique())
print("сами уникальные значения:", df['Embarked'].unique())

#часть 3
print("часть 3")

shape_before = df.shape

#16
missing_counts = df.isnull().sum()
print("\n количество пропусков в каждом столбце:")
print(missing_counts)

#17
missing_percents = (df.isnull().sum() / len(df)) * 100
print("\n процент пропусков в каждом столбце:")
print(missing_percents.round(2))

#18
max_missing_col = missing_counts.idxmax()
print(f"\n столбец с максимальным числом пропусков: {max_missing_col} ({missing_counts.max()} пропусков)")

#19
age_before = {
    'mean': df['Age'].mean(),
    'median': df['Age'].median(),
    'min': df['Age'].min(),
    'max': df['Age'].max(),
    'std': df['Age'].std(),
    'count': df['Age'].count()
}
print("\n показатели Age до заполнения пропусков:")
for k, v in age_before.items():
    print(f"  {k}: {v:.4f}" if isinstance(v, float) else f"  {k}: {v}")

#20
df['Age'] = df['Age'].fillna(age_before['median'])
print(f"\n пропуски в Age заполнены медианой ({age_before['median']}).")

#21
age_after = {
    'mean': df['Age'].mean(),
    'median': df['Age'].median(),
    'min': df['Age'].min(),
    'max': df['Age'].max(),
    'std': df['Age'].std(),
    'count': df['Age'].count()
}

#22
age_comparison_table = pd.DataFrame({
    'показатель': [
        'среднее арифметическое',
        'медиана',
        'минимальный возраст',
        'максимальный возраст',
        'стандартное отклонение',
        'количество известных значений'
    ],
    'до обработки': [
        round(age_before['mean'], 4),
        round(age_before['median'], 4),
        round(age_before['min'], 4),
        round(age_before['max'], 4),
        round(age_before['std'], 4),
        age_before['count']
    ],
    'после обработки': [
        round(age_after['mean'], 4),
        round(age_after['median'], 4),
        round(age_after['min'], 4),
        round(age_after['max'], 4),
        round(age_after['std'], 4),
        age_after['count']
    ]
})
print("\n таблица сравнения возраста до и после обработки:")
print(age_comparison_table.to_string(index=False))

#23
df = df.dropna(subset=['Embarked'])

#24
cabin_missing_share = df['Cabin'].isnull().mean() * 100
print(f"\n доля пропусков в Cabin: {cabin_missing_share:.2f}%")
if cabin_missing_share > 50:
    df = df.drop(columns=['Cabin'])
    print("столбец Cabin удален, так как доля пропусков выше 50%.")

#25
print("\n пропуски в таблице после обработки:")
print(df.isnull().sum())

#26
shape_after = df.shape
print(f"\n размер до обработки: {shape_before}, после обработки: {shape_after}")

#часть 4
print("часть 4")

survived_arr = df['Survived'].to_numpy()
sex_arr = df['Sex'].to_numpy()
age_arr = df['Age'].to_numpy()
fare_arr = df['Fare'].to_numpy()

#31
total_surv_pct = np.mean(survived_arr) * 100
print(f"\n общий процент выживших: {total_surv_pct:.2f}%")

#32
male_mask = (sex_arr == 'male')
female_mask = (sex_arr == 'female')

male_surv_pct = np.mean(survived_arr[male_mask]) * 100
female_surv_pct = np.mean(survived_arr[female_mask]) * 100
print(f"процент выживших мужчин: {male_surv_pct:.2f}%, женщин: {female_surv_pct:.2f}%")

#33
male_age_mean = np.mean(age_arr[male_mask])
female_age_mean = np.mean(age_arr[female_mask])
print(f"средний возраст мужчин: {male_age_mean:.2f} лет, женщин: {female_age_mean:.2f} лет")

#34
def safe_np_mean(arr):
    return round(float(np.mean(arr)), 2) if len(arr) > 0 else "нет данных"

m_surv_age = safe_np_mean(age_arr[male_mask & (survived_arr == 1)])
m_died_age = safe_np_mean(age_arr[male_mask & (survived_arr == 0)])
f_surv_age = safe_np_mean(age_arr[female_mask & (survived_arr == 1)])
f_died_age = safe_np_mean(age_arr[female_mask & (survived_arr == 0)])

print("средний возраст по группам выживаемости и пола:")
print(f"  выжившие мужчины: {m_surv_age}")
print(f"  погибшие мужчины: {m_died_age}")
print(f"  выжившие женщины: {f_surv_age}")
print(f"  погибшие женщины: {f_died_age}")

#35
fare_min = np.nanmin(fare_arr)
fare_max = np.nanmax(fare_arr)
fare_mean = np.nanmean(fare_arr)
print(f"стоимость билета - мин: {fare_min:.4f}, макс: {fare_max:.4f}, средняя: {fare_mean:.4f}")

#36
age_std_np = np.std(age_arr)
print(f"стандартное отклонение возраста: {age_std_np:.4f}")

numpy_comparison = pd.DataFrame({
    'показатель': [
        'количество человек',
        'процент выживших',
        'средний возраст (общий)',
        'средний возраст выживших',
        'средний возраст погибших'
    ],
    'мужчины': [
        int(np.sum(male_mask)),
        round(male_surv_pct, 2),
        round(male_age_mean, 2),
        m_surv_age,
        m_died_age
    ],
    'женщины': [
        int(np.sum(female_mask)),
        round(female_surv_pct, 2),
        round(female_age_mean, 2),
        f_surv_age,
        f_died_age
    ]
})
print("\n сводная таблица:")
print(numpy_comparison.to_string(index=False))

#часть 5
print("часть 5")

#1
task1_df = df[(df['Sex'] == 'male') & (df['Age'] > 30) & (df['Pclass'] == 1)]
print(f"\n мужчины > 30 лет в 1-м классе. количество: {len(task1_df)}")
print(task1_df.head(10))

#2
task2_df = df[((df['Age'] < 18) | (df['Sex'] == 'female')) & (df['Survived'] == 1)]
print(f"\n (моложе 18 лет или женщины) и при этом выжили. количество: {len(task2_df)}")

#3
mean_fare_class3 = df[df['Pclass'] == 3]['Fare'].mean()
task3_df = df[(df['Pclass'] == 3) & (df['Fare'] > mean_fare_class3)]
print(f"\n средняя цена билета в 3 классе: {mean_fare_class3:.4f}. пассажиров с билетом дороже среднего: {len(task3_df)}")
print(task3_df.head(5))

#4
task4_df = df[(df['Age'] >= 20) & (df['Age'] <= 40) & (df['Embarked'] == 'S')]
print(f"\n пассажиры 20-40 лет из порта S. количество: {len(task4_df)}")
print(task4_df.head(5))

#часть 6
print("часть 6")

#37
grouped_class_sex = df.groupby(['Pclass', 'Sex']).agg(
    Passenger_Count=('PassengerId', 'count'),
    Mean_Age=('Age', 'mean'),
    Survived_Rate_Pct=('Survived', lambda x: x.mean() * 100),
    Mean_Fare=('Fare', 'mean')
).reset_index()
print("\n группировка по Pclass и Sex:")
print(grouped_class_sex.round(2))

#38
grouped_embarked = df.groupby('Embarked').agg(
    Passenger_Count=('PassengerId', 'count'),
    Survived_Rate_Pct=('Survived', lambda x: x.mean() * 100)
).reset_index()
print("\n группировка по порту посадки:")
print(grouped_embarked.round(2))

#39
survival_by_class = df.groupby('Pclass')['Survived'].mean() * 100
best_class = survival_by_class.idxmax()
print("\n процент выживших по классам:")
print(survival_by_class.round(2))
print(f"класс с наибольшей долей выживших: {best_class}-й класс ({survival_by_class.max():.2f}%)")

#часть 7
print("часть 7")

#40
df.to_csv('titanic_processed.csv', index=False)

#41
grouped_class_sex.to_csv('titanic_statistics.csv', index=False)

#42
check_df = pd.read_csv('titanic_processed.csv')
print(check_df.head(3))
