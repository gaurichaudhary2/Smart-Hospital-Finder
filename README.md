# Smart Hospital Finder (CLI Based AI Project)
##Project Description

Smart Hospital Finder is a Command Line Interface (CLI) based application that helps users find the nearest or cheapest hospital from a given location. It uses Artificial Intelligence search algorithms to provide efficient and optimal results. This project is useful in real-life situations, especially during emergencies where quick decision-making is important.

## Features
Find nearest hospital using Breadth First Search (BFS)<br>
Find cheapest hospital using Uniform Cost Search (UCS)<br>
Emergency mode for quick hospital access<br>
Filter hospitals by type (Government / Private / All)<br>
Simple CLI-based interaction<br>
Handles invalid inputs properly<br>
## AI Concepts Used
Breadth First Search (BFS)<br>
Uniform Cost Search (UCS)<br>
Graph-based problem solving<br>
## Technologies Used
Python<br>
JSON<br>
Command Line Interface (CLI)<br>
## Project Structure

Smart-Hospital-Finder/<br>
│
├── main.py (Main program)<br>
├── bfs.py (BFS algorithm)<br>
├── ucs.py (UCS algorithm)<br>
├── utils.py (Helper functions)
├── graph.py (Validation)<br>
├── data.json (Data storage)<br>
└── README.md<br>

## How to Run

Step 1: Clone the repository<br>
git clone https://github.com/gaurichaudhary2/smart-hospital-finder<br>

Step 2: Open the folder<br>
cd smart-hospital-finder<br>

Step 3: Run the program<br>
python main.py<br>

## How It Works
User selects current location<br>
User chooses an option (Nearest / Cheapest / Emergency)<br>
System applies AI algorithm (BFS or UCS)<br>
Displays hospital name and path (and cost in UCS)<br>
## Example Output

Smart Hospital Finder Menu<br>
<br>
Find Nearest Hospital<br>
Find Cheapest Hospital<br>
View Hospitals<br>
Emergency Mode<br>
Exit<br>

Nearest Hospital: Hamidia Hospital<br>
Path: MP Nagar → Habibganj → BHEL → Govindpura → Hamidia Hospital<br>

## Real-World Use
Emergency hospital search<br>
Healthcare assistance<br>
Smart city systems<br>
Decision support tools<br>
## Limitations
Uses static data<br>
Limited locations<br>
No real-time updates<br>
CLI only (no GUI)<br>
## Future Enhancements
Real-time hospital data integration<br>
GPS location detection<br>
GUI or mobile app version<br>
Distance and time calculation<br>
## Author

Gauri Chaudhary<br>

## Conclusion

This project shows how AI algorithms like BFS and UCS can solve real-world problems efficiently. It provides a simple and effective solution for hospital searching using a CLI-based system.
