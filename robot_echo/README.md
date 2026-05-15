# ROS2 Mini Project – Robot Echo Intelligent System

## Overview

This project is a ROS2-based robot command system that receives text commands, converts them into motion commands, and tracks execution history.

It demonstrates key ROS2 concepts:
- Topics (Publish/Subscribe)
- Services
- Node communication
- Launch files
- Multi-node architecture

---

## System Architecture

The system contains 3 nodes:

### 1. `cmd_parser`
| Direction | Topic | Message Type |
|-----------|-------|-------------|
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

---

### 2. `logger_node`
- Subscribes: `/cmd_text` (`std_msgs/String`)
- Logs all received commands to `commands.log`

---

### 3. `history_service`
- Service: `/get_history` (`example_interfaces/srv/Trigger`)
- Returns the list of last executed commands

---

## How to Build

From the workspace root:

```bash
cd ~/mini_project
colcon build
source install/setup.bash
```

---

## How to Launch

```bash
ros2 launch robot_echo echo.launch.py
```

---

## How to Test

### Send commands to the robot

Open a new terminal and source the workspace first:

```bash
source ~/mini_project/install/setup.bash
```

Then publish commands:

```bash
ros2 topic pub --once /cmd_text std_msgs/String "{data: 'avance 2'}"
ros2 topic pub --once /cmd_text std_msgs/String "{data: 'tourne_gauche 1.5'}"
ros2 topic pub --once /cmd_text std_msgs/String "{data: 'stop'}"
```

### Check robot output

```bash
ros2 topic echo /robot_response
```

### Get command history

```bash
ros2 service call /get_history example_interfaces/srv/Trigger {}
```

### Check logs

```bash
cat commands.log
```