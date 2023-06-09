from stockmodels.datalayer_mysql_main import Datamanager


class Url(Datamanager):

    def __init__(self, indiz_id):
        super().__init__()
        self.fk_id = indiz_id
        self._url = [list(row) for row in self.select(f"SELECT url, selector, active FROM indiz_url WHERE indiz_id={self.fk_id}")]

    def get_url(self, active=False):
        if active:
            return [row[0] for row in self._url if row[-1]==active]
        else:
            return [row[0] for row in self._url]

    def get_url_selector(self, active=False):
        if active:
            return [list(row[0:2]) for row in self._url if row[-1]==active]
        else:
            return [list(row[0:2]) for row in self._url]

    def get_all_items(self, active=False):
        if active:
            return [list(row[0:]) for row in self._url if row[-1]==active]
        else:
            return [list(row[0:]) for row in self._url]
