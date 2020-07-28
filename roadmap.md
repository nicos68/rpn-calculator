# Roadmap of NPR Calculator
* Make sure that chaining operators work and fix things if it doesn't.
* Implement more operators (pow, sqrt, sin, cos, tan, log, exp, ...)
* Generate a new calculator on user's demand, generate a uuid for it, and store it in a map in `server.py` script.
* Use the stack to define formulae and trace curves.
* Add buttons for operators in the UI.
* Define multiple calculator profiles with different sets of operators (simple, scientific, ...)
* Allow the user to rearange the stack at will, maybe using angular material's drag and drop capabilities.
* Store calculators in a persistence component, possibly in a NoSQL server.
* Add a debugger to let the user execute the stack step by step
* Check stack validity (cardinality, mathematical errors like 0-based divisions)
* Store user's current stack ID, maybe in a browser cookie.
* Add login, permissions, and possibly stack sharing between users
* Package the whole application (server and UI code) in a single docker image