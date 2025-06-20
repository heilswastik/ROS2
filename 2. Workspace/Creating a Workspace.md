# 🚀 Creation of a Workspace
A **ROS 2 workspace** is a structured directory where you develop, build, and manage multiple ROS packages. It helps keep your code organized, supports efficient builds using `colcon`, and allows you to isolate your custom packages from the system-wide ROS installation. Workspaces are essential for scaling robotics projects, running simulations, and collaborating with others.  
This guide will help you create a ROS 2 workspace from scratch, build packages, and source your environment. Works for distributions like `ROS 2 Humble` and `Jazzy`.  

Let's create a workspace called `arduinobot`
```
mkdir -p arduinobot/src
cd arduinobot # TO GO INSIDE WORKSPACE
``` 
Inside folder/workspace build it by using `colcon`  
`colcon` (short for collective construction) is the official build tool used in ROS 2 to build and manage multiple packages at once.   
```
colcon build
```
It will display something like
```
cyther@cyther-Dell-G15-5535:~/arduinobot$ colcon build
                     
Summary: 0 packages finished [0.25s]
```
The workspace will contain 4 folders
```
cyther@cyther-Dell-G15-5535:~/arduinobot$ ls
build  install  log  src
```
All the code you write will be be in `src` folder
