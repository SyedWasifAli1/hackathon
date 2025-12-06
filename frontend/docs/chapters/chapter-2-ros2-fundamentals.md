---
sidebar_position: 2
title: "Chapter 2: Fundamentals of Robot Operating System (ROS 2)"
description: "Introduction to ROS 2 concepts, architecture, and development practices"
---

# Chapter 2: Fundamentals of Robot Operating System (ROS 2)

## Learning Objectives

By the end of this chapter, you should be able to:
- Understand the core concepts and architecture of ROS 2
- Create and manage ROS 2 packages and workspaces
- Implement nodes, topics, services, and actions
- Work with ROS 2 launch files and parameters
- Integrate ROS 2 with Physical AI systems

## Introduction

The Robot Operating System 2 (ROS 2) is a flexible framework for writing robot software. It's a collection of tools, libraries, and conventions that aim to simplify the task of creating complex and robust robot behavior across a wide variety of robot platforms.

Unlike traditional operating systems, ROS 2 is not an actual OS but rather a middleware framework that provides services designed for a heterogeneous computer cluster. It includes hardware abstraction, device drivers, libraries, visualizers, message-passing, package management, and more.

## ROS 2 Architecture

ROS 2 is built on the Data Distribution Service (DDS) standard, which provides a publish-subscribe communication model. This architecture enables:

- **Nodes**: Individual processes that perform computation
- **Topics**: Named buses over which nodes exchange messages
- **Services**: Synchronous request/response communication
- **Actions**: Asynchronous request/goal-based communication
- **Parameters**: Configuration values that can be set at runtime

## Creating Your First ROS 2 Package

To create a new ROS 2 package, you can use the `ros2 pkg create` command:

```bash
ros2 pkg create --build-type ament_python my_robot_package
```

This creates a basic package structure with the necessary files and directories for a Python-based ROS 2 package.

## Nodes, Topics, and Services

### Nodes

A node is an executable that uses ROS 2 to communicate with other nodes. Here's a simple example of a ROS 2 node in Python:

```python
import rclpy
from rclpy.node import Node

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World'
        self.publisher_.publish(msg)
```

### Topics and Message Types

Topics in ROS 2 are named buses over which nodes exchange messages. Common message types include:
- `std_msgs`: Standard message types like String, Int32, Float64
- `sensor_msgs`: Sensor data messages like LaserScan, Image, PointCloud2
- `geometry_msgs`: Geometric primitives like Pose, Twist, Vector3

## Exercises

1. Create a ROS 2 workspace and build a simple publisher-subscriber example
2. Implement a service server that calculates the distance between two points
3. Design a node that subscribes to sensor data and publishes motor commands
4. Create a launch file that starts multiple nodes simultaneously