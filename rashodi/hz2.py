# Подключаем библиотеки
import httplib2 
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials	

CREDENTIALS_FILE = 'python-294009-dcee9da23ee4.json'  # Имя файла с закрытым ключом, вы должны подставить свое

# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = googleapiclient.discovery.build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API 

spreadsheetId = '1538VHl-NM1XvRJp_80V7k3kX4YgzapuRLq3hEhBQ4po' # сохраняем идентификатор файла
print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)

# Добавление листа
results = service.spreadsheets().batchUpdate(
    spreadsheetId = spreadsheetId,
    body = 
{
  "requests": [
    {
      "addSheet": {
        "properties": {
          "title": "Еще один лист233",
          "gridProperties": {
            "rowCount": 20,
            "columnCount": 12
          }
        }
      }
    }
  ]
}).execute()


# Получаем список листов, их Id и название
spreadsheet = service.spreadsheets().get(spreadsheetId = spreadsheetId).execute()
sheetList = spreadsheet.get('sheets')
for sheet in sheetList:
    print(sheet['properties']['sheetId'], sheet['properties']['title'])
    
sheetId = sheetList[0]['properties']['sheetId']

print('Мы будем использовать лист с Id = ', sheetId)