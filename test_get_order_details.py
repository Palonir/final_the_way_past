# Чечерин Николай, 10-я когорта - Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def test_status_get_order_details_response(): # Проверяем,что код ответа равен 200
    response = sender_stand_request.post_new_order(data.orders_body)
    order_track = sender_stand_request.get_new_order_track(response)
    details_response = sender_stand_request.get_order_details(order_track)
    assert details_response.status_code == 200
