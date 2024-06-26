import csv
import pathlib


from analysis.services.read_data import read_input_excel, read_input_csv, read_input_txt
from importfiles.models import InitialUploadedFile



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
            col_del = file.txt_column_delimiter
            ids_pop, sums_pop = read_input_txt(file_name, col_del)
        ids.extend(ids_pop.tolist())
        sums.extend(sums_pop.tolist())

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
    mus_id,row_sum

    Первая строка - название колонок, остальные - элементы выборки.

    Args:
        path (str): путь для записи выборки
        row_ids (list[str]): список mus_id элементов
        row_sums (list[float]): список значений элементов
        spm: уровень существенности
    """
    p = pathlib.Path(path)
    pathlib.Path(p.parent.absolute()).mkdir(parents=True, exist_ok=True)

    with open(path, "w") as f:
        csvwriter = csv.writer(f, delimiter=",", quotechar='"')
        csvwriter.writerow(["mus_id", "row_sum"])
        for row_id, row_sum in zip(
            row_ids, row_sums
        ):
            if row_sum >= spm:
                csvwriter.writerow(
                    [str(row_id), row_sum]
                    )