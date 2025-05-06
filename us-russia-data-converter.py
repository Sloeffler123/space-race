import pandas as pd
import plotly.express as px

all_data = pd.read_csv('rocket-data.csv')

def get_dates(dates):
    joined_dates = ' '.join(dates)
    new_lst = joined_dates.split()
    lst = []
    for j in new_lst:
        if j.isdigit() and int(j) < 1976:
            lst.append(j) 
    return lst

def get_space_race_data(data, dates, dict):
    status_lst = []
    company_lst = []
    date_lst = []
    location_lst = []
    outcome_lst = []
    details_lst = []
    price_lst = []
    for i in range(len(dates)):
        for j in range(len(dates)):
            try:
                if dict[i] in dates[j]:
                    status_lst.append(data['status'].values[j])
                    company_lst.append(data['company'].values[j])
                    date_lst.append(data['date'].values[j])
                    location_lst.append(data['location'].values[j])
                    outcome_lst.append(data['outcome'].values[j])
                    details_lst.append(data['details'].values[j].replace('\n', ''))
                    price_lst.append(data['price'].values[j])
                    break
            except IndexError:
                break
    return status_lst, company_lst, date_lst, location_lst, outcome_lst, details_lst, price_lst     


us_data = all_data[all_data['company'] == 'NASA']
us_dates = us_data['date'].values
us_year_dict = get_dates(us_dates)
us_status_lst, us_company_lst, us_date_lst, us_location_lst, us_outcome_lst, us_details_lst, us_price_lst = get_space_race_data(us_data, us_dates, us_year_dict)

russia_data = all_data[all_data['company'] == 'RVSN USSR']
russia_dates = russia_data['date'].values
russia_year_dict = get_dates(russia_dates)
russia_status_lst, russia_company_lst, russia_date_lst, russia_location_lst, russia_outcome_lst, russia_details_lst, russia_price_lst = get_space_race_data(russia_data, russia_dates, russia_year_dict)

russia_dict = {
    'status': russia_status_lst,
    'company': russia_company_lst,
    'date': russia_date_lst,
    'location': russia_location_lst,
    'outcome': russia_outcome_lst,
    'details': russia_details_lst,
    'price': russia_price_lst
}

us_dict = {
    'status': us_status_lst,
    'company': us_company_lst,
    'date': us_date_lst,
    'location': us_location_lst,
    'outcome': us_outcome_lst,
    'details': us_details_lst,
    'price': us_price_lst
}
us_df = pd.DataFrame(us_dict)
russia_df = pd.DataFrame(russia_dict)

us_df.to_csv('us-space-race-data.csv')
russia_df.to_csv('russia-space-race-data.csv')
