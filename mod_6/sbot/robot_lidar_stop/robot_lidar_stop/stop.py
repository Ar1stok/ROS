import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class Publisher(Node):
    def __init__(self):
        super().__init__('publisher')
        self.publisher = self.create_publisher(Twist, '/robot/cmd_vel', 10)
        self.sub = self.create_subscription(LaserScan, '/robot/scan', self.laser_callback, 1)
        self.timer = self.create_timer(0.2, self.go_forward)
        self.msg = LaserScan()

    def laser_callback(self, data):
        self.msg = data

    def go_forward(self):
        message = Twist()
        flag_free = 1
        scan_data = self.msg.ranges
        front = scan_data[160:200]
        close_points = [i for i in front if i < 1]
        if len(close_points) >= 5:
            self.get_logger().info('I see an obstacle in the distance: ' + str(min(close_points)))
            flag_free = 0

        message.linear.x = -0.5 if flag_free else 0.0
        self.publisher.publish(message)            

def main(args=None):
    rclpy.init(args=args)
    publisher = Publisher()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()