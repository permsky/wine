import os
from collections import defaultdict
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import click
import pandas as pd
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape


WINERY_ESTABLISHED_YEAR = 1920


def get_winery_age() -> str:
    """Calculate winery age and return proper string."""
    winery_age = str(datetime.now().year - WINERY_ESTABLISHED_YEAR)
    if winery_age[-1] == '1' and winery_age[-2] != '1':
        winery_age += ' год'
    elif (int(winery_age[-1]) in range(2,5)) and winery_age[-2] != '1':
        winery_age += ' года'
    else:
        winery_age += ' лет'
    return winery_age


def get_wines(filename: str) -> defaultdict:
    """
    Get wines information from xlsx file and sort them by
    categories.
    """
    excel_df = pd.read_excel(filename, na_values='nan', keep_default_na='')
    sorted_excel_df = excel_df.sort_values(by='Категория')
    wines = sorted_excel_df.to_dict(orient='records')
    grouped_by_categories_wine = defaultdict(list)
    for wine in wines:
        grouped_by_categories_wine[wine['Категория']].append(wine)
    return grouped_by_categories_wine


@click.command()
@click.option(
    '--path',
    default='wines.xlsx',
    help='Путь к xlsx-файлу с таблицей вин'
)
@click.option(
    '--var',
    help='Имя переменной окружения, хранящей путь к xlsx-файлу с таблицей вин'
)
def main(path, var) -> None:
    """Render index.html and start HTTP server."""
    load_dotenv()
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    
    if var:
        path = os.getenv(var)
    template = env.get_template('template.html')
    rendered_page = template.render(
        winery_age=get_winery_age(),
        wines=get_wines(path)
    )

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
