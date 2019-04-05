import sys

from googlesheets.google_sheet_manager import GoogleSheetManager


def main():
    args = sys.argv[1:]
    credentials_path = args[0]
    sheet_id = args[1]
    manager = GoogleSheetManager(credentials_path=credentials_path, sheet_id=sheet_id)
    manager.start_session()
    rows = manager.get_all_rows()
    cols = manager.get_col_values(2)
    new_row = ("Some Name", "Some Phone Number", "Some Address")
    manager.append_row(new_row)
    manager.insert_row(new_row, 2)
    manager.close_session()
    pass


if __name__ == '__main__':
    main()
