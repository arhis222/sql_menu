# Interactive Waste Collection Management System

An interactive command-line application designed to optimize and manage municipal waste collection systems in **Pittsburgh, Pennsylvania**. This project utilizes a relational database to organize garbage collectors, specialized vehicle fleets, city districts, and real-time scheduling.

##  Features

* **Relational Database:** Robust SQLite schema managing Collectors, Districts, Trucks, Models, and Schedules.
* **Interactive CLI:** A user-friendly menu system for data visualization, modification, and deletion.
* **Real-time Validation:** Python-based triggers to ensure truck waste capacity is never exceeded during scheduling.
* **Advanced Analytics:** Custom queries to track active/inactive trucks, worker schedules, and remaining fleet capacity.
* **Data Integrity:** Enforces strict constraints on phone numbers (9 digits), IDs (2 digits), and scheduling hours (05:00 - 19:00).

## Database Schema (UML)

The system is built on a relational model including:
- **Collectors (Balayeurs):** ID, Pseudo, Phone, Assigned Truck.
- **Districts (Quartiers):** Code, Name, Population, Number of bins.
- **Trucks (CamionsOrdure):** License Plate, Team Capacity, Model, Center.
- **Schedules (Programmations):** District Code, Truck Plate, Collection Time.

##  Installation & Usage

### Prerequisites
- Python 3.x
- SQLite3

### Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/arhis222/sql_menu.git](https://github.com/arhis222/sql_menu.git)
   cd sql_menu
   ```
2. Install dependencies (if any, e.g., tabulate for pretty tables) in requirements.txt
3. Run the application:
   ```bash
   python main.py
   ```

## Menu Structure
The application features a structured command-line interface:
* **[a] Display**: List all information for each class or run custom filtered queries (e.g., finding which collector works at a specific hour).
* **[m] Modification**: Full CRUD capabilities including inserting, updating, or eliminating records across all tables.
* **[i] Project Info**: Displays a summary of the project's background regarding pollution issues in Pittsburgh.
* **[q] Quit**: Securely exit the application.

## License
This project is licensed under the **MIT License*.

## Author
* **Arhan UNAY**

