import csv
import os

from analysis.services.read_data import read_input_excel, read_input_csv, read_input_txt


def process_files(
    paths: list[str],
    spm: float,
    analysis_name: str,
    save_folder: str,
    col_del=""
) :
    """Основная функция для запуска сэмплирования"""

    # чтение популяций
    ids, sums = [], []
    for path in paths:
        if path.endswith(".xlsx"):
            ids_pop, sums_pop = read_input_excel(path)
        elif path.endswith('csv'):
            ids_pop, sums_pop = read_input_csv(path)
        else:
            ids_pop, sums_pop = read_input_txt(path, col_del)
        ids.append(ids_pop)
        sums.append(sums_pop)

    new_sample_path_save = os.path.join(save_folder, analysis_name)

    write_sample(
        new_sample_path_save,
        ids,
        sums,
        spm
    )




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
    with open(path, "w", encoding="utf-8", newline="") as f:
        csvwriter = csv.writer(f, delimiter=",", quotechar='"')
        csvwriter.writerow(["mus_is", "row_sum"])
        for row_id, row_sum in zip(
            row_ids, row_sums
        ):
            if row_sum >= spm:
                csvwriter.writerow(
                    [str(row_id), row_sum]
                )