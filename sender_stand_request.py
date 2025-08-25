import config
import requests
import data

# создание заказа
def post_new_order(body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

# получение трек-номера
def get_order_track(track):
    url = config.URL_SERVICE + config.ORDER_INFO
    return requests.get(config.URL_SERVICE + config.CREATE_ORDER_PATH, 
                        params={"t": str(track)},
                        headers=data.headers)
