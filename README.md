# ROS2 Mini Projects

A collection of ROS2 mini projects demonstrating core robotics concepts including topics, services, simulation, and multi-node architectures.

---

## Projects

| # | Project | Description |
|---|---------|-------------|
| 1 | [Robot Echo Intelligent System](#1-robot-echo-intelligent-system) | Text command parser with motion output and history tracking |
| 2 | [TurtleBot3 Obstacle Avoidance](#2-turtlebot3-obstacle-avoidance-gazebo-simulation) | LiDAR-based autonomous obstacle avoidance in Gazebo |

---

## 1. Robot Echo Intelligent System

### Overview

A ROS2-based robot command system that receives text commands, converts them into motion commands, and tracks execution history.

ROS2 concepts demonstrated:
- Topics (Publish/Subscribe)
- Services
- Node communication
- Launch files
- Multi-node architecture

---

### System Architecture

The system contains 3 nodes:

#### `cmd_parser`

| Direction | Topic | Message Type |
|-----------|-------|--------------|
| Subscribes | `/cmd_text` | `std_msgs/String` |
| Publishes | `/robot_response` | `geometry_msgs/Twist` |
| Publishes | `/command_history` | `std_msgs/String` |

Supported commands:

| Command | Description |
|---------|-------------|
| `avance N` | Move forward by N |
| `recule N` | Move backward by N |
| `tourne_gauche A` | Turn left by angle A |
| `tourne_droite A` | Turn right by angle A |
| `stop` | Stop the robot |

#### `logger_node`

- Subscribes: `/cmd_text` (`std_msgs/String`)
- Logs all received commands to `commands.log`

#### `history_service`

- Service: `/get_history` (`example_interfaces/srv/Trigger`)
- Returns the list of last executed commands

---

### How to Build

```bash
cd ~/mini_project
colcon build
source install/setup.bash
```

### How to Launch

```bash
ros2 launch robot_echo echo.launch.py
```

### How to Test

**Send commands** — open a new terminal:

```bash
source ~/mini_project/install/setup.bash

ros2 topic pub --once /cmd_text std_msgs/String "{data: 'avance 2'}"
ros2 topic pub --once /cmd_text std_msgs/String "{data: 'tourne_gauche 1.5'}"
ros2 topic pub --once /cmd_text std_msgs/String "{data: 'stop'}"
```

**Check robot output:**

```bash
ros2 topic echo /robot_response
```

**Get command history:**

```bash
ros2 service call /get_history example_interfaces/srv/Trigger {}
```

**Check logs:**

```bash
cat commands.log
```

---

## 2. TurtleBot3 Obstacle Avoidance (Gazebo Simulation)

### Overview

A Gazebo simulation of a TurtleBot3 robot implementing simple autonomous obstacle avoidance. The robot uses LiDAR scan data to detect obstacles and adjust its movement to avoid collisions.

ROS2 concepts demonstrated:
- Topics (`/scan`, `/cmd_vel`)
- Sensor processing (LiDAR)
- Basic autonomous navigation logic
- Gazebo simulation integration

---

### System Behavior
Is path clear?
├── YES → Move forward
└── NO  → Obstacle detected
├── Close range  → Stop and reorient
└── Medium range → Turn left or right

### Topics Used

| Topic | Type | Direction | Description |
|-------|------|-----------|-------------|
| `/scan` | `sensor_msgs/LaserScan` | Subscribes | LiDAR sensor data |
| `/cmd_vel` | `geometry_msgs/Twist` | Publishes | Robot velocity commands |

---

### Required Dependencies

```bash
sudo apt install ros-jazzy-turtlebot3
sudo apt install ros-jazzy-turtlebot3-simulations
sudo apt install ros-jazzy-gazebo-ros-pkgs
```

> Replace `jazzy` with your ROS2 distro if different (e.g. `humble`).

---

### How to Launch

**Step 1 — Set the TurtleBot3 model:**

```bash
export TURTLEBOT3_MODEL=burger
```

**Step 2 — Launch the Gazebo world:**

```bash
ros2 launch turtlebot3_gazebo empty_world.launch.py
```

**Step 3 — Run the obstacle avoidance node** (new terminal):

```bash
source ~/mini_project/install/setup.bash
ros2 run turtlebot_obstacle_avoidance obstacle_avoidance
```

---

