# Let's create a package in ROS2
In **ROS 2**, a `package` is the basic unit of software organization — it’s like a modular folder that contains everything needed for a specific feature or node.  
Go to `src` folder
```
cd arduinobot/src/
```
To create a package named `arduino_bot`
```
ros2 pkg  create --build-type ament_python arduino_bot
```
| --build-type | Build Type|
|----------|----------|
| ament_python    | Python based package   | 
| ament_cmake   | C++ based package   | 

## Output will be something like
```
going to create a new package
package name: arduino_bot
destination directory: /home/cyther/arduinobot/src
package format: 3
version: 0.0.0
description: TODO: Package description
maintainer: ['cyther <swastik.yash29052005@gmail.com>']
licenses: ['TODO: License declaration']
build type: ament_python
dependencies: []
creating folder ./arduino_bot
creating ./arduino_bot/package.xml
creating source folder
creating folder ./arduino_bot/arduino_bot
creating ./arduino_bot/setup.py
creating ./arduino_bot/setup.cfg
creating folder ./arduino_bot/resource
creating ./arduino_bot/resource/arduino_bot
creating ./arduino_bot/arduino_bot/__init__.py
creating folder ./arduino_bot/test
creating ./arduino_bot/test/test_copyright.py
creating ./arduino_bot/test/test_flake8.py
creating ./arduino_bot/test/test_pep257.py

[WARNING]: Unknown license 'TODO: License declaration'.  This has been set in the package.xml, but no LICENSE file has been created.
It is recommended to use one of the ament license identitifers:
Apache-2.0
BSL-1.0
BSD-2.0
BSD-2-Clause
BSD-3-Clause
GPL-3.0-only
LGPL-3.0-only
MIT
MIT-0

```
## Build your workspace again
⚠️MAKE SURE YOU ARE IN YOUR MAIN WORKSPACE FOLDER.  
All packages are built inside `src` folder but building is done inside main folder
```
cd ..
colcon build
```
Output will be:
```
cyther@cyther-Dell-G15-5535:~/arduinobot$ colcon build
Starting >>> arduino_bot
Finished <<< arduino_bot [0.63s]          

Summary: 1 package finished [0.83s]
```
## ⚠️ SOURCE YOUR WORKSPACE
You need to source your workspace everytime you **build/rebuild the workspace** and/or **open a terminal**.  
However it can be automated by:
```
cd # Be in the home directory of your ubuntu
gedit .bashrc
```
In the end, write:
```
source /home/cyther/arduinobot/install/setup.bash
```
Modify names according to your folders and save it.  
Now you need to only open the `.bashrc` by `gedit .bashrc` everytime you **build/rebuild the workspace**. No need to source it everytime you open a new terminal.
