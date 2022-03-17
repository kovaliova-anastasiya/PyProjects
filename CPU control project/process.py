import psutil as pt


class CpuBar:

    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=False)  # выводит количество ядер у процессора - 2
        self.cpu_count_logical = pt.cpu_count()  # выводит количство потоков - 4, на ядре по 2 потока

    def cpu_percent_return(self):  # выдаёт среднюю загрузку по каждому ядру: [15.6, 31.2, 31.2, 28.1]
        return pt.cpu_percent(percpu=True)

    # для мин окна: ф-ция будет считывать не показатели по каж.проц, а суммарную загрузку процессора
    def cpu_one_return(self):
        return pt.cpu_percent()

    def ram_usage(self):
        return pt.virtual_memory()  # возвр  именованный кортеж
# svmem(total=8472711168, available=1399427072, percent=83.5, used=7073284096, free=1399427072)
