from collections import defaultdict
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_winery_age() -> str:
    """Calculate winery age and return proper string."""
    winery_age = str(datetime.now().year - 1920)
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
    excel_df_sorted = excel_df.sort_values(by='Категория')
    wines = excel_df_sorted.to_dict(orient='records')
    wine_sorted_by_categories = defaultdict(list)
    for wine in wines:
        wine_sorted_by_categories[wine['Категория']].append(wine)
    return wine_sorted_by_categories


def main() -> None:
    """Render index.html and start HTTP server."""
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    
    template = env.get_template('template.html')
    rendered_page = template.render(
        winery_age=get_winery_age(),
        wines=get_wines('wine3.xlsx')
    )

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
