import csv
from itertools import islice

import numpy as np


from importfiles.services.parsers import get_excel_workbook
from importfiles.storage import uploads_storage


def read_input_excel(path: str) -> tuple[np.array, np.array]:
    """Читает таблицу с первого листа первой ячейки экселевского файла вида
    ---------
    id | sum|
    ---------
    id0| 100
    id1| 3000
    ...| ....
    ---------

    И возвращает два вектора numpy одинаковой длины - ids и sums.

    Args:
        path (str): путь к файлу.

    Returns:
        np.array: вектор ids со строками-идентификаторами, shape [len(data),]
        np.array: вектор sums с суммами (float), shape [len(data),]

        строки векторов отсортированы по (-sums, ids) по возрастанию
    """
    rows = []
    with get_excel_workbook(path) as wb:
        sheet0 = wb[wb.sheetnames[0]]
        for value in sheet0.iter_rows(min_row=2, values_only=True):
            rows.append((str(value[0]), float(value[1])))

    rows = sorted(rows, key=lambda x: (-x[1], x[0]))
    ids = []
    sums = []

    for row in rows:
        ids.append(str(row[0]))
        sums.append(float(row[1]))
    return np.array(ids), np.array(sums, dtype=np.float32)


def read_input_csv(path: str) -> tuple[np.array, np.array]:
    """Читает файл csv популяции
    Первая строка - header, следующие содержат элементы популяции

    Пример файла:
    id,sum
    A10,90.1
    A9,1000

    Args:
        path (str): путь к csv-файлу

    Returns:
        tuple[np.array, np.array]: вектор ids и вектор sums
            для элементов популяции
    """
    rows = []
    with uploads_storage.open(path, 'r') as f:
        csvreader = csv.reader(f, delimiter=",", quotechar='"')
        for line in islice(csvreader, 1, None):
            if line != []:
                rows.append([line[0].strip(), float(line[1].strip())])

    rows = sorted(rows, key=lambda x: (-x[1], x[0]))
    ids = []
    sums = []

    for row in rows:
        ids.append(str(row[0]))
        sums.append(row[1])
    return np.array(ids), np.array(sums, dtype=np.float32)

def read_input_txt(path:str, col_del: str) -> tuple[np.array, np.array]:
    """Читает файл txt популяции
        Первая строка - header, следующие содержат элементы популяции

        Пример файла:
        id,sum
        A10,90.1
        A9,1000

        Args:
            path (str): путь к csv-файлу
            col_del (str): разделитель колонок

        Returns:
            tuple[np.array, np.array]: вектор ids и вектор sums
                для элементов популяции
        """
    rows = []
    with uploads_storage.open(path, 'r') as f:
        for line in f.readlines()[1:]:
            line = line.rstrip('\n').rstrip('\r')
            if line != '':
                rows.append((str(line.split(col_del)[0]), float(line.split(col_del)[1])))

    rows = sorted(rows, key=lambda x: (-x[1], x[0]))
    ids = []
    sums = []

    for row in rows:
        ids.append(str(row[0]))
        sums.append(row[1])
    return np.array(ids), np.array(sums, dtype=np.float32)