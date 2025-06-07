import pandas as pd

def calculate_demographic_data():
    # Load dataset
    df = pd.read_csv("adult.data.csv")

    # 1. Count each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. % with Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. % with advanced education making >50K
    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_edu = ~higher_edu

    higher_edu_rich = round((df[higher_edu]['salary'] == '>50K').mean() * 100, 1)
    lower_edu_rich = round((df[lower_edu]['salary'] == '>50K').mean() * 100, 1)

    # 5. Min hours per week
    min_work_hours = df['hours-per-week'].min()

    # 6. % of rich among those who work min hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # 7. Country with highest % of >50K earners
    country_income = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()
    rich_country_ratio = (country_income / country_total).dropna()
    highest_earning_country = rich_country_ratio.idxmax()
    highest_earning_country_percentage = round(rich_country_ratio.max() * 100, 1)

    # 8. Most popular high-earning job in India
    top_IN_occupation = df[(df['native-country'] == 'India') & 
                           (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
