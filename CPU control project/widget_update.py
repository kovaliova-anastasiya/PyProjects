# класс, который находится здесь, будет обновлять конфигурацию виджетов

class ConfigureWidgets:

    def configure_cpu_bar(self):
        r = self.cpu.cpu_percent_return()  # здесь хранится список с процентами загрузки
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].configure(text=f'core{i + 1} usage:{r[i]}%')
            self.list_pbar[i].configure(value=r[i])

        r2 = self.cpu.ram_usage()
        self.ram_lab.configure(text=f'RAM usage: {r2[2]}%, used: {round(r2[3] / 1048576)} Mb,\
        \n available: {round(r2[1] / 1048576)} Mb')

        self.ram_bar.configure(value=r2[2])

        self.wheel = self.after(1000, self.configure_cpu_bar)  # позволяет циклически запускать ф-цию раз в 1000 мс

    # ф-ция для перемещения окошка ниже

    def configure_win(self):
        if self.wm_overrideredirect():  # если окно с рамкой, возвращает True
            self.overrideredirect(False)
        else:
            self.overrideredirect(True)
        self.update()

    def clear_win(self):
        for i in self.winfo_children():  # возвращает список виджетов с главного окна
            i.destroy()

    # конфигурирует виджеты в малом окне
    def configure_minimal_win(self):
        self.bar_one.configure(value=self.cpu.cpu_one_return())
        self.ram_bar.configure(value=self.cpu.ram_usage()[2])
        self.wheel = self.after(1000, self.configure_minimal_win)
