from datetime import datetime


class Logger:
    def __init__(self, path):
        self.path = path

    def write_log(self, log_data: str):
        """
        Запись в файл данных
        :param log_data:
        :return: None
        """
        try:
            with open(self.path, 'a', encoding="windows-1251") as f:
                now = datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
                data = now + ' : ' + log_data
                f.write(data)
        except IOError:
            print("Ошибка ввода-вывода")
        finally:
            f.close()
