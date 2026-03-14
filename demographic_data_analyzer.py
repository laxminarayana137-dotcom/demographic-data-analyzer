import pandas as pd

def calculate_demographic_data(print_data=True):

    # Read data
    df = pd.read_csv("adult.data.csv")

    # 1. Number of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage of people with Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1
    )

    # 4. Percentage with advanced education earning >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 5. Percentage without advanced education earning >50K
    lower_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education_rich = round(
        (df[lower_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 6. Minimum work hours per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of rich among those who work fewest hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 8. Country with highest percentage of >50K earners
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    highest_earning_country = country_salary['>50K'].idxmax()
    highest_earning_country_percentage = round(
        country_salary['>50K'].max() * 100, 1
    )

    # 9. Most popular occupation in India for >50K earners
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
        ['occupation']
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Higher education rich:", higher_education_rich)
        print("Lower education rich:", lower_education_rich)
        print("Min work hours:", min_work_hours)
        print("Rich percentage:", rich_percentage)
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country percentage:", highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }