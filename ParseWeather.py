import urllib.request
from bs4 import BeautifulSoup


def ParseWeatherYandex(city):
    url = 'https://yandex.ru/pogoda/' + city
    page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')

    # getting time now, temperature and condition
    day = soup.find('time', 'fact__time').contents
    temperature = soup.find('span', 'temp__value').contents
    weather_type = soup.find('div', 'link__condition day-anchor i-bem').contents

    # parsing feeling temperature
    t = soup.find('dl', 'term term_orient_h fact__feels-like')
    t = ((t.div).span).contents

    # joining lists in one
    feels = list(soup.find('dt', 'term__label').contents) + t

    print(day[0] + '\n' + 'Температура сейчас: ' + (temperature[0]).replace('\u2212', '-'), end='\n')
    print('Погода: %s' % weather_type[0], end=', ')
    print('%s %s' % (feels[0].lower(), feels[1].replace('\u2212', '-')))


def main():
    ParseWeatherYandex(input('Введите город: '))
    input()


if __name__ == '__main__':
    main()

