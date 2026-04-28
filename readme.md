# Проект Yatube parsing

### Основные команды

1. Установка библиотеки:
```bash
pip install scrapy
```

```bash
pip install sqlalchemy
```

2. Создание проекта:
```bash
scrapy startproject yatube_parsing .
```

3. Создание "Паука":
```bash
scrapy genspider yatube 158.160.212.51
```

```bash
scrapy genspider group 158.160.212.51
```

4. Запуск работы "Паука":
```bash
scrapy crawl yatube -o django.csv
```

```bash
scrapy crawl group -o groups.csv
```
