# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Настройте окружение. Для этого выполните следующие действия:
  - установите Python3.x;
  - создайте виртуальное окружение [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.
  - установите необходимые зависимости:

    ```pip install -r requirements.txt```
- Подготовьте входные данные (по умолчанию таблица вин хранится в файле-примере wines.xlsx):
  - создайте xlsx-файл;
  - создайте в нем таблицу, содержащую столбцы с именами как в примере ниже, и занесите свои данные в тело таблицы.
    | Категория    | Название            | Сорт            | Цена | Картинка                 | Акция                |
    |--------------|---------------------|-----------------|------|--------------------------|----------------------|
    | Белые вина   | Белая леди          | Дамский пальчик | 399  | belaya_ledi.png          | Выгодное предложение |
    | Напитки      | Коньяк классический |                 | 350  | konyak_klassicheskyi.png |                      |
    | Белые вина   | Ркацители           | Ркацители       | 499  | rkaciteli.png            |                      |
    | Красные вина | Черный лекарь       | Качич           | 399  | chernyi_lekar.png        |                      |
    | Красные вина | Хванчкара           | Александраули   | 550  | hvanchkara.png           |                      |
    | Белые вина   | Кокур               | Кокур           | 450  | kokur.png                |                      |
    | Красные вина | Киндзмараули        | Саперави        | 550  | kindzmarauli.png         |                      |
    | Напитки      | Чача                |                 | 299  | chacha.png               | Выгодное предложение |
    | Напитки      | Коньяк кизиловый    |                 | 350  | konyak_kizilovyi.png     |                      |
- При необходимости путь к xlsx-файлу можно хранить в переменной окружения в файле ```.env``` в директории скрипта.
- Запустите сайт командой:

  ```
  python main.py [--h] [--path <путь к файлу с таблицей вин>]
  ```
  Либо, если используете переменную окружения:

  ```
  python main.py [--h] [--var <имя переменной окружения>]
  ```

- Перейдите на сайт по адресу:

  [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).