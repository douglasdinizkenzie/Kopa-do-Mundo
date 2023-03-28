from exceptions import (
                        NegativeTitlesError,
                        InvalidYearCupError,
                        ImpossibleTitlesError)
from datetime import datetime, timedelta


def data_processing(data):
    titles = data['titles']
    first_cup_format = datetime.strptime(data['first_cup'], '%Y-%m-%d')

    if titles < 0:
        raise NegativeTitlesError("titles cannot be negative")

    year_now = datetime.now().year
    while first_cup_format.year + 4 <= year_now:
        first_cup_format += timedelta(days=4*365)

    if first_cup_format.year < 1930 or (first_cup_format.year - 1930) % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")

    years_since_first_cup = year_now - first_cup_format.year
    max_titles = years_since_first_cup // 4
    if titles > max_titles:
        raise ImpossibleTitlesError("impossible to have more titles "
                                    "than disputed cups")

    return data



