1. Create a `publisher.py` in `/home/cyther/arduinobot/src/py/py`
2. Write your code
3. Go to `setup.py` in `/home/cyther/arduinobot/src/py`
4. Add `'Publish= py.publisher:main'` in `entry_points`
   ```
   entry_points={
        'console_scripts': [
            'Publish= py.publisher:main',
        ],
    }
   ```
5. Go to `package.xml` in `/home/cyther/arduinobot/src/py`
6. Add
   ```
     <exec_depend>rclpy</exec_depend>
     <exec_depend>std_msgs</exec_depend>
   ```
   It will look like
   ```
    <license>TODO: License declaration</license>

    <exec_depend>rclpy</exec_depend>
    <exec_depend>std_msgs</exec_depend>

    <test_depend>ament_copyright</test_depend>
   ```
7. Build package again
8. Run the node by ```ros2 run py Publish```
---
## Explaination
There are are lot of publish. Here is a breakdown:  
`Publish` is the name of command to enter the node  
`py` is the name of the package  
`SimplePublisher` is the name of class  
`Node_Publisher` is the name of the node  
`publish` is an oblject of the class  
