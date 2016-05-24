
def clients_client_id_get(client_id, limit) -> str:
    return ('Client_ID: ' + str(client_id))

def clients_client_id_post(client_id, sensor_data) -> str:
    return ('Client_ID: ' + str(client_id) +' | Sensor_Data: ' + str(sensor_data))

def clients_get(limit) -> str:
    return 'do some magic!'
