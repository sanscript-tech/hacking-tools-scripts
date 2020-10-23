# Simpy
SimPy is a discrete-event simulation library. The behavior of active components (like vehicles, customers or messages) is modeled with processes. All processes live in an environment. They interact with the environment and with each other via events.

# Interrupts
Interrupts are thrown into process functions as Interrupt exceptions that can (should) be handled by the interrupted process. The process can then decide what to do next (e.g., continuing to wait for the original event or yielding a new event)

# About the Script
Here we have taken the example of a ticketing model. It has two processes namely ```run``` and ```request```. The ticketing system switches between the states 
collecting ticket requets and distributing tickets. It announces its new state by printing a message and the current simulation time (as returned by the Environment.now property). It then calls the Environment.timeout() factory function to create a Timeout event. By yielding the event, it signals the simulation that it wants to wait for the event to occur.
Both the processes take place alternately for 5 time stamps until interrupted by a high priority process(taking a break here). The driver process has a reference to the ticket’s action process. After waiting for 15 time steps, it interrupts that process.

# To run
```pip install simpy```</br>
```python ticketing_model.py```

# Sample output

![alt text](https://github.com/TaniaMalhotra/hacking-tools-scripts/blob/simpy/Python/simpy/simpy_1.png)
