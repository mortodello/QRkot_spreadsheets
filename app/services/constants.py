from datetime import datetime

from app.core.config import settings

FORMAT = "%Y/%m/%d %H:%M:%S"

now_date_time = datetime.now().strftime(FORMAT)

SPREADSHEET_BODY = {
    'properties': {'title': f'Отчёт от {now_date_time}',
                   'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'Лист1',
                               'gridProperties': {'rowCount': 100,
                                                  'columnCount': 11}}}]
}

PERMISSIONS_BODY = {'type': 'user',
                    'role': 'writer',
                    'emailAddress': settings.email}