# Description

The aim of this programming project was to produce an agent based model which shows the agents interacting with each other and the environment data. The final outcome includes a animation of the interactions in a GUI offering the opportunity to run the model through the menu.

## Running the software

Download the software from Github and open within a python interpreter or IDE such as Spyder. Select run from the menu to run ABM model.

## Files

```python 
ReadMe.txt - This file.

Agentframework.py - File containing the agent
class and necessary functions for moving, 
eating the environment and sharing distances.

Model.py - Main agent based model brining
together agents, GUI and webscrapping functionality.

In.txt - Environment data.
```

## Testing and Bugs 
1. Currently the model is working to produce an animated agents based model of agents interacting in the environment until an attempt at producing a stop function when environment is empty has failed.
2. Timers were added in certain sections of the code to ensure efficiency. 
3. An error when incorporating the GUI was resolved by changing "canvas.show" to "canvas.draw" allowing the animation to be carried out.
4. When running the code within the Mac OS the Ipython console had to be adjusted to using Tkinter via System preference> Graphics> Tkinter. and also making the following import "matplotlib.use('macosx')".


## License
[MIT](https://choosealicense.com/licenses/mit/)
