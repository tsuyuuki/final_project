import sender_stand_request
import data

# Дейкун Анастасия, 33-я когорта — Финальный проект. Инженер по тестированию плюс

def test_order_track():
    # создать заказ
    create_order = sender_stand_request.post_new_order(data.new_order)
    track = create_order.json()["track"]

    # получить заказ по его трек-номеру
    track_order = sender_stand_request.get_order_track(track)
    assert track_order.status_code == 200
