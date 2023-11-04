import configuration
import requests
import data

def post_new_order(body): # Функция для отправки POST-запроса на создание нового заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


def get_new_order_track(response): # Функция для извлечения трекера заказа из ответа POST-запроса на создание нового заказа
    json_response = response.json()
    order_track = json_response.get('track')
    return order_track

def get_order_details(order_track): # Функция для выполнения запроса на получение заказа по трекеру заказа
    url = f"{configuration.URL_SERVICE}{configuration.CREATE_ORDER_DETAILS}?t={order_track}"
    headers = data.headers.copy()
    response = requests.get(url, headers=headers)
    return response

response = post_new_order(data.orders_body)
order_track = get_new_order_track(response)
response = get_order_details(order_track)
print(response.status_code)
print(response.headers)
print(response.json())