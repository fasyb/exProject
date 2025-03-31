import requests
from django.conf import settings
from django.http import JsonResponse

def get_users(table_id):
    url = f'{settings.NOCODB_BASE_URL}tables/{table_id}/records'
    headers = {'xc-token': settings.NOCODB_API_KEY}
    params = {'limit': 25}  # Можно задать другие параметры запроса
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Ошибка при получении данных: {response.text}')

def get_nocodb_data(request):
    # URL API NocoDB (замените на ваш URL)
    url = f'{settings.NOCODB_BASE_URL}tables/mf830hfoed91tav/records'
    headers = {'xc-token': settings.NOCODB_API_KEY}

    # Получаем данные из NocoDB
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()  # Данные таблицы
        records = data.get('list', [])  # Извлекаем записи из ключа 'list'

        # Формируем JSON-ответ
        response_data = {
            "nocodb-data": "http://localhost:8000/nocodb-data/",  # Ссылка на таблицу
            "records": records  # Данные таблицы
        }
        return JsonResponse(response_data, status=200)
    else:
        # Если произошла ошибка, возвращаем пустой JSON
        return JsonResponse({"error": "Не удалось получить данные из NocoDB"}, status=response.status_code)