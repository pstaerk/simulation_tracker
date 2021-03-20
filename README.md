## Idea

The idea is to enable the tracking of simulation data flow.
A common problem is that one has different input parameters, output data streams etc. which change over the course of a project.
Keeping track of all the changes, experiments and ways of analysing the resulting data is of utmost importance.
For these reasons, one needs a metadata tracker, database system and analysis flow tracker.
This project aims to do all that.

### Updated Usage Idea
The idea is to be able to write what your simulation/analysis method should do in a function, were variable parameters are given as command line arguments.
I.e. you can use the `click` library for command line arguments, which will then automatically be associated with your simulation/analysis run.
This then could look like the following:

```python
@simulation_tracker.tracker_command()
@click.option('--temp', type=int, help='Temperature of the simulation.')
def main_sim(temp):
    sim.temp = temp # Or something like that
    ...
    return trajectories
```

Where the tracker tool now automatically notes the temperature used in the simulation.
Perhaps there is a way of using the return arguments as a way of specifying the stuff that should be saved to the file?

The tracker tool should then handle all the things in the background, saving the data to a specific location, keeping the metadata/simulation inputs readily available as well in a lookup table.
If everything works like it should, then one could use this system to also register a analysis object, which processes the data in some way, taking both the raw, large data and the inputs into account.
These analysis objects, could then be chained together, or interface with another experiment object which calls the simulation script again, making it clear which path the data took, which is very valuable for understanding the flow of data and tracing back final results to all relevant simulations/experiments.
It would be awesome, if this could be displayed as a flow graph.

## TODO List
 - [ ] Write flexible input parameter database
     - [x] Think about making this interface with the click library, to get all the arguments.
     - [ ] Save the input parameters from click
     - [ ] Also add the capability of adding other options (e.g. commit hash)
 - [ ] Write flexible data management system
 - [ ] Write flexible analysis management
 - [ ] Include a graphical UI for displaying the various experiments and flows
