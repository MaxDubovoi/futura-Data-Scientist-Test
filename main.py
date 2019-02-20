import pandas as pd


def table_constructor(_country_list):
    _final_table = {}
    for _country in _country_list:
        _lvt = compute_lifetime_value(data_weekly_revenue, data_weekly_users, _country)
        _roi = list_avg(roi(data_weekly_revenue.get(_country), data_weekly_costs.get(_country)))
        _cpi = list_avg(cpi(data_weekly_costs.get(_country), data_weekly_installs.get(_country)))

        _final_table[_country, 'Cost per Install'] = list_avg(_lvt)
        _final_table[_country, 'LTV'] = list_avg(_lvt)
        _final_table[_country, 'ROI'] = list_avg(_roi)
    return _final_table


def compute_lifetime_value(revenue, users, _country):
    def compute_lifetime_value_column(revenue_for_country, users_for_country):
        return revenue_for_country / users_for_country

    return compute_lifetime_value_column(revenue.get(_country), users.get(_country))


def list_avg(_list: list):
    return sum(_list) / len(_list)


def roi(_revenue, _cost):
    _roi_list = []
    for _revenue_item in _revenue:
        for _cost_item in _cost:
            _roi_list.append((_revenue_item - _cost_item) / _cost)
    return _roi_list


def cpi(_cost, _install):
    return _cost / _install


# read data
data_weekly_revenue = pd.read_csv('res/Weekly Revenue.csv', ',', skiprows=2)
data_weekly_users = pd.read_csv('res/Weekly Active Users.csv', ',', skiprows=2)
data_weekly_installs = pd.read_csv('res/Weekly Installs.csv', ',')
data_weekly_costs = pd.read_csv('res/Weekly Costs.csv', ',')
country_list = list(data_weekly_revenue.columns.values)
country_list.remove('Week')
final_table = table_constructor(country_list)
