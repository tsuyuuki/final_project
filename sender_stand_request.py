import config
import requests
import data

# Дейкун Анастасия, 33-я когорта — Финальный проект. Инженер по тестированию плюс

# создание заказа
def post_new_order(body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_order(data.new_order)

# получение трек-номера
def get_order_track():
    response = post_new_order(data.new_order)
    return response.json()["track"]
     

# получение инфо о заказе
def get_order_info(track_value):
            full_path = config.GET_ORDER_INFO + str(track_value)
            return requests.get(config.URL_SERVICE + full_path,
                               headers=data.headers)

#Проверка кода ответа
track = get_order_track()
response = get_order_info(track)
assert response.status_code == 200