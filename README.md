## Idea

The idea is to enable the tracking of simulation data flow.
A common problem is that one has different input parameters, output data streams etc. which change over the course of a project.
Keeping track of all the changes, experiments and ways of analysing the resulting data is of utmost importance.
For these reasons, one needs a metadata tracker, database system and analysis flow tracker.
This project aims to do all that.

### First Usage Idea
It would be very nice to be able to register one "experiment", by something like
```python
exp = experiment_tracker.Experiment('Homogeneous System Simulation 1')
```
which creates a `exp` object.
The inputs to a specific experiment would then be registered by something like:
```python
exp.input(T= TEMPERATURE)
exp.input(N_PARTICLES=N_PARTICLES)
...
```
or
```python
exp.input_dict = {'T':TEMPERATURE, 'N_PARTICLES':N_PARTICLES}
```
and thereby register all the relevant meta-data.
It would also make a lot of sense to also include the commit hash of the simulation script at this point.

Outputs to a simulation could then be registered like this:
```python
exp.out(trajectories_type_1=trajectories, method='pickle')
```
e.g. to register the trajectories of all type 1 particles using pickle.

The tracker tool should then handle all the things in the background, saving the data to a specific location, keeping the metadata/simulation inputs readily available as well in a lookup table.
If everything works like it should, then one could use this system to also register a analysis object, which processes the data in some way, taking both the raw, large data and the inputs into account.
These analysis objects, could then be chained together, or interface with another experiment object which calls the simulation script again, making it clear which path the data took, which is very valuable for understanding the flow of data and tracing back final results to all relevant simulations/experiments.
It would be awesome, if this could be displayed as a flow graph.

## TODO List
 - [ ] Write flexible input parameter database
     - [ ] Think about making this interface with the click library, to get all the arguments.
     - [ ] Also add the capability of adding other options (e.g. commit hash)
 - [ ] Write flexible data management system
 - [ ] Write flexible analysis management
 - [ ] Include a graphical UI for displaying the various experiments and flows
