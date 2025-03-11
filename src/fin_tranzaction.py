import csv
import pandas as pd


def csv_file(file):
    """Cчитывает финансовые операции из CSV-файлов"""
    try:
        with open(file) as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("отсутствует файл")


def xlsx_file(file):
    """Cчитывает финансовые операции из XLSX-файлов"""
    try:
        pd_xlsx = pd.read_excel(file)
        print(pd_xlsx)
    except FileNotFoundError:
        print("отсутствует файл")
