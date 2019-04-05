import string

import gspread as gspread
from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account


class GoogleSheetManager:
    credentials = ""
    sheet_id = ""
    client = None
    DEFAULT_SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    def __init__(self, credentials_path, sheet_id, scopes=DEFAULT_SCOPES):
        self.sheet_id = sheet_id
        self._init_credentials(credentials_path=credentials_path, scopes=scopes)

    def _init_credentials(self, credentials_path, scopes):
        self.credentials = service_account.Credentials.from_service_account_file(credentials_path, scopes=scopes)
        self.client = gspread.Client(auth=self.credentials)

    def start_session(self):
        self.client.session = AuthorizedSession(self.credentials)

    def close_session(self):
        if self.client.session is not None:
            self.client.session.close()

    def _get_worksheet(self, wsheet_number):
        sheet = self.client.open_by_key(self.sheet_id)
        worksheet = sheet.get_worksheet(wsheet_number)
        return worksheet

    @staticmethod
    def _build_range(row_number, col_count):
        range_text = "A{0}:{1}{2}".format(row_number, string.ascii_uppercase[col_count - 1], row_number)
        return range_text

    # Create methods

    def append_row(self, row_values, worksheet_number=0):
        worksheet = self._get_worksheet(worksheet_number)
        return worksheet.append_row(row_values)

    def insert_row(self, row_values, row_index, worksheet_number=0):
        worksheet = self._get_worksheet(worksheet_number)
        return worksheet.insert_row(row_values, row_index)

    # Read methods

    def get_row(self, row_number, worksheet_number=0):
        worksheet = self._get_worksheet(worksheet_number)
        return worksheet.row_values(row_number)

    def get_cell_value(self, cell_row, cell_col, worksheet_number=0):
        worksheet = self._get_worksheet(worksheet_number)
        return worksheet.cell(cell_row, cell_col)

    def get_all_rows(self, worksheet_number=0):
        worksheet = self._get_worksheet(worksheet_number)
        return worksheet.get_all_records(head=1)

    def get_cell_value_alpha(self, alpha_index, worksheet_number=0):
        worksheet = self._get_worksheet(worksheet_number)
        return worksheet.acell(alpha_index)

    def get_col_values(self, col_num, worksheet_number=0):
        worksheet = self._get_worksheet(worksheet_number)
        return worksheet.col_values(col=col_num)

    def get_row_count(self, worksheet_number=0):
        worksheet = self._get_worksheet(worksheet_number)
        return worksheet.row_count()

    # Update methods

    def update_cell_value(self, cell_row, cell_col, value, worksheet_number=0):
        worksheet = self._get_worksheet(worksheet_number)
        return worksheet.update_cell(cell_row, cell_col, value=value)

    def update_row(self, row_number, row_values, worksheet_number=0):
        worksheet = self._get_worksheet(worksheet_number)
        cell_range = self._build_range(row_number, len(row_values))
        cell_list = worksheet.range(cell_range)
        for i in range(0, len(row_values)):
            cell_list[i].value = row_values[i]
        return worksheet.update_cells(cell_list)

    # Delete methods

    def delete_row(self, row_number, worksheet_number=0):
        worksheet = self._get_worksheet(worksheet_number)
        return worksheet.delete_row(row_number)
