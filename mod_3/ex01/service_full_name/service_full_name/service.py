from fn_interface.srv import FullNameService

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(FullNameService, 'con_name', self.name_callback)

    def name_callback(self, request, response):
        response.full_name = request.last_name + ' ' + request.name + ' ' + request.first_name
        self.get_logger().info('Incoming request with Name: %s' % (request.name))

        return response


def main():
    rclpy.init()

    service = MinimalService()

    rclpy.spin(service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()