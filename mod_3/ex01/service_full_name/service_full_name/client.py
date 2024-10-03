import sys

from fn_interface.srv import FullNameService
import rclpy
from rclpy.node import Node


class ClientAsync(Node):

    def __init__(self):
        super().__init__('client_async')
        self.cli = self.create_client(FullNameService, 'con_name')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = FullNameService.Request()

    def send_request(self, last_name, name, first_name):
        self.req.last_name = last_name
        self.req.name = name
        self.req.first_name = first_name
        return self.cli.call_async(self.req)


def main():
    rclpy.init()

    client = ClientAsync()
    future = client.send_request(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))
    rclpy.spin_until_future_complete(client, future)
    response = future.result()
    client.get_logger().info('Result of Your Full Name: %s' % (response.full_name))

    client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()