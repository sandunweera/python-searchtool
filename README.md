
## Table of Content
* [The Problem Statement](#the-problem-statement)
* [The Solution](#the-solution)
* [Finite State Machine](#finite-state-machine)
* [Advantages of FSM](#advantages-of-fsm)
* [Install and run](#install-and-run)
* [Patterns used](#patterns-used)
* [Known Issues and Limitations](#known-issues-and-limitations)

## The Problem Statement
Given the information of Users, Organizations and Tickets, an efficient program should be developed to search information. The User entity has a relationship with Organization and the Ticket entity has multiple relationships with Organization as well as user.
The number of entities of each type can grow infinitely.

## The Solution
Basically there are 2 ways to solve the issue.
1. **Non Indexed Mode** - The JSON elements are iterated until the search information is found. This mode slow and required higher amount of computing power. The computational complexity is O(n<sup>2</sup>)

2. **Indexed Mode** - The JSON elements are converted into a search efficient tree structure and all search operations are done on the tree structure (a.k.a Index). This is very fast and requires less computing power once the index is created. The computational complexity is O(log n)

Given the fact that the number of entities can grow exponentially over the time the indexed mode has been selected.

Given that this capability is available with opensource libraries, Whoosh library has been used. [https://whoosh.readthedocs.io/en/latest/index.html](https://whoosh.readthedocs.io/en/latest/index.html)
Whoosh is a fast, pure python search engine widely adapted by the development community.

## Finite State Machine

A **finite state machine (FSM)** is a computation model that can be used to simulate sequential logic using the states. Given that the problem can be mapped with a finite state machine, the FSM approach has been used to implement the user input logic.

![FSM](https://i.ibb.co/CV5q6sB/FSM.png)

1. The state transitions occurs based on user inputs. The inputs are marked on the edges. 
2. From any state the user can type 'quit' and exit. The state is transited to Quit state and the transitions are marked with dotted lines.
3. When the input is invalid then the state is transited to Error and a error message is displayed.

The FSM can be simplified by eliminating the similar flows (Marked in same colour), however multiple flows has been developed to provide the flexibility to cater future changes. With this design any individual flow can be changed without affecting the others. (Ex : Adding a new State only to the Tickets flow)

## Advantages of FSM
Finite State Machine based implementation has following advantages therefore it is friendly with any future 
1. Easy to alter the transition map
2. Easy to add new states
3. Easy to debug and troubleshoot
4. Code is highly readable

## Install and run

Pre requisites:
- Python 3
- PIP

Install dependencies with :
```
# Linux/macOSinstall-and-run)
python3 -m pip install whoosh

# Windows (may require elevation)
python -m pip install whoosh
```

To run the app:
```
# Linux/macOS
python3 app.py

# Windows (may require elevation)
python app.py
```
When selecting each entity type for the first time an index will be created. This is a one time operation and may take few seconds if the input files are large. 

## Patterns Used
The schema of the each entity is different but the nature of operations performed on each entity type is quite similar. The similar functions have been included in a base class, and the appropriate object type is created using Factory Design pattern.

## Known Issues and Limitations
1. The dates are indexed as TEXT rather than DATETIME since the Date format in the JSON files are not compatible with Whoosh. Therefore the queries such as "Users who joined before 31st of December 2018" cannot be performed. The solution is to convert the dates in JSON to a Whoosh compatible format which hasn't been done yet.

2. The tags are indexed as TEXT rather than a LIST. Whoosh does not have a LIST type hence indexed as TEXT. However the search by a tag should still work (Whoosh performs a simple TEXT search on a flattened list)

3. When the data is required to be passed from one state to another, global variables has been used. This reduced the flexibility of the code when concerning a multi-threaded environment. The solution is to extend the current implementation to pass runtime parameters between the states when a state transition is occured.
