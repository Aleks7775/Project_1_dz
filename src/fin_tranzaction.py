import csv
import pandas as pd


def csv_file(file):
    """Cчитывает финансовые операции из CSV-файлов"""
    try:
        with open(file) as f:
            reader = csv.DictReader(f, delimiter=';')
            rows = []
            for row in reader:
                rows.append(row)
            return rows
    except FileNotFoundError:
        return "отсутствует файл"


def xlsx_file(file):
    """Cчитывает финансовые операции из XLSX-файлов"""
    try:
        pd_xlsx = pd.read_excel(file)
        tr = pd_xlsx.to_dict('records')
        return tr
    except FileNotFoundError:
        return "отсутствует файл"
