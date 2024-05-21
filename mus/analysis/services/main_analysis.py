import csv
import os

from analysis.services.read_data import read_input_excel, read_input_csv, read_input_txt
from importfiles.models import InitialUploadedFile
from importfiles.storage import uploads_storage


def process_files(
    files: list[InitialUploadedFile],
    spm: float,
    new_sample_path_save: str
) -> str:
    """Основная функция для запуска сэмплирования"""

    # чтение популяций
    ids, sums = [], []
    for file in files:
        file_name = file.initial_file.name
        if file_name.endswith(".xlsx"):
            ids_pop, sums_pop = read_input_excel(file_name)
        elif file_name.endswith('csv'):
            ids_pop, sums_pop = read_input_csv(file_name)
        else:
            col_del = file.initial_file.txt_column_delimiter
            ids_pop, sums_pop = read_input_txt(file_name, col_del)
        ids.append(ids_pop)
        sums.append(sums_pop)

    write_sample(
        new_sample_path_save,
        ids,
        sums,
        spm
    )

    return new_sample_path_save




def write_sample(
    path: str,
    row_ids: list[str],
    row_sums: list[float],
    spm: float
) -> None:
    """Записывает выборку в csv-формате в файл path.

    Выборка - csv-файл с следующими колонками:
    pop_ids,row_ids,row_sums,is_IS_list,mus_rec_hit_list

    Первая строка - название колонок, остальные - элементы выборки.

    Args:
        path (str): путь для записи выборки
        row_ids (list[str]): список mus_id элементов
        row_sums (list[float]): список значений элементов
        spm: уровень существенности
    """
    with open(path, "w") as f:
        csvwriter = csv.writer(f, delimiter=",", quotechar='"')
        csvwriter.writerow(["mus_is", "row_sum"])
        for row_id, row_sum in zip(
            *row_ids, *row_sums
        ):
            if row_sum >= spm:
                csvwriter.writerow(
                    [str(row_id), row_sum]
                    )