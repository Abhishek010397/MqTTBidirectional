import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes
import time


class MqTTPub:

    def __init__(self):
        print("Creating Client")
        client = mqtt.Client("client1", protocol=mqtt.MQTTv5)
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.on_disconnect = self.on_disconnect
        client.on_subscribe = self.on_subscribe
        client.on_publish = self.on_publish
        properties = None
        client.connect('your-ip', 1883, properties=properties)
        client.loop_start()
        client.subscribe('org/responses/client1')
        time.sleep(2)
        client.message_received_flag = False
        properties = Properties(PacketTypes.PUBLISH)
        client.publish('org/common', "Hi From Client", properties=properties)
        while not client.message_received_flag:
            time.sleep(1)
        client.message_received_flag = False
        time.sleep(5)
        client.disconnect()

    def on_publish(self, client, userdata, mid):
        print("published")

    def on_connect(self, client, userdata, flags, reasonCode, properties=None):
        print('Connected ', reasonCode)

    def on_message(self, client, userdata, message):
        msg = str(message.payload.decode("utf-8"))
        print('RECV Topic = ', message.topic)
        print('RECV MSG =', msg)
        client.message_received_flag = True

    def on_disconnect(self, client, userdata, rc, properties):
        print('Received Disconnect ', rc)

    def on_subscribe(self, client, userdata, mid, granted_qos, properties=None):
        print('SUBSCRIBED')

    def on_unsubscribe(self, client, userdata, mid, properties, reasonCodes):
        print('UNSUBSCRIBED')

def main():
    mqtt_client = MqTTPub()

if __name__ == "__main__":
    main()