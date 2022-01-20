import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes
import time


class MqTTSub:

    def __init__(self):
        print("creating client")
        client = mqtt.Client("server", protocol=mqtt.MQTTv5)
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.on_disconnect = self.on_disconnect
        client.on_subscribe = self.on_subscribe
        client.on_publish = self.on_publish
        properties = None
        client.connect('your-ip', 1883, properties=properties)
        time.sleep(5)
        client.subscribe('org/common')
        time.sleep(2)
        properties = Properties(PacketTypes.PUBLISH)
        properties.ResponseTopic = 'org/responses/server'
        client.loop_forever()


    def on_publish(self,client, userdata, mid):
        print("published")


    def on_connect(self,client, userdata, flags, reasonCode, properties=None):
        print('Connected ', reasonCode)


    def on_message(self,client, userdata, message):
        msg = str(message.payload.decode("utf-8"))
        print('RECV Topic = ', message.topic)
        print('RECV MSG =', msg)
        properties = Properties(PacketTypes.PUBLISH)
        client.publish('org/responses/client1',"Hi From Server", properties=properties)

    def on_disconnect(self,client, userdata, rc):
        print('Received Disconnect ', rc)

    def on_subscribe(self,client, userdata, mid, granted_qos, properties=None):
        print('SUBSCRIBED')

    def on_unsubscribe(self,client, userdata, mid, properties, reasonCodes):
        print('UNSUBSCRIBED')

def main():
    while True:
        mqtt_client = MqTTSub()

if __name__ == "__main__":
    main()