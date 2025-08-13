#include <iostream>
#include <string>
#include <limits>

using namespace std;

class Player {
protected:
    string name;
    int age;

public:
    void setDetails() {
        cout << "Enter your astronaut name: ";
        cin >> name;
        cout << "What is your age? ";
        while (!(cin >> age)) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Invalid input. Please enter a valid age: ";
        }
    }

    virtual void displayDetails() const {
        cout << "Astronaut Name: " << name << ", Age: " << age << endl;
    }
};

class Mission : public Player {
public:
    void startMission() {
        cout << "Welcome to Mission Galactic Quest\n";
        cout << "After detecting a mysterious signal from a distant galaxy, a team of astronauts\n";
        cout << "aboard the starship *Eclipse* embarks on a journey to uncover its origin.\n";
        cout << name << ", being " << age << " years old, leads the team and warns them\n";
        cout << "that this mission is fraught with unknown dangers and challenges.\n";
    }

    int chooseDirection() {
        int direction;
        cout << "Enter a direction (1 for Alpha Quadrant, 2 for Beta Quadrant, etc.): ";
        while (!(cin >> direction)) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Invalid input. Please enter a number: ";
        }
        return direction;
    }
};

class Spaceship {
private:
    int year;
    string model;
    int speed = 0;

public:
    void setDetails() {
        cout << "Enter the year of the spaceship: ";
        cin >> year;
        cout << "Enter the model of the spaceship: ";
        cin >> model;
        cout << "Enter the speed of your spaceship (in light-years per hour): ";
        cin >> speed;
    }

    void setDetails2() const {
        cout << "Spaceship Year: " << year << ", Model: " << model << endl;
        cout << "Spaceship Speed: " << speed << " light-years/hour" << endl;
    }
}; // Fixed missing semicolon

// Main function
int main() {
    char again = 'Y';
    int mission1 = 1; // Initialize mission1
    int mission2 = 1; // Initialize mission2
    int mission3 = 1; // Initialize mission3
    int mission4 = 1; // Initialize mission4
    int obstacle = 0; // Initialize obstacle

    while (again == 'Y' || again == 'y') {
        Mission mission;
        mission.setDetails();
        mission.startMission();

        Spaceship spaceship; // Create an instance of Spaceship
        spaceship.setDetails(); // Set spaceship details
        spaceship.setDetails2(); // Display spaceship details

        int direction = mission.chooseDirection();
        cout << "The team navigated to the " << direction << " quadrant and ventured deeper into space.\n";

        while (mission1) {
            if (obstacle == 0) {
                cout << "You have encountered a massive asteroid field! Choose your action:\n";
                cout << "0. Navigate through carefully\n";
                cout << "1. Use the ship's shields to push through\n";
                cout << "2. Attempt to destroy the asteroids\n";
                int choice;
                cin >> choice;

                if (choice == 0) {
                    cout << "You successfully navigated through the asteroid field.\n";
                } else if (choice == 1) {
                    cout << "You pushed through the field but sustained minor damage.\n";
                } else if (choice == 2) {
                    cout << "Your attempt failed. The ship is destroyed. MISSION FAILED.\n";
                    mission1 = 0; // End the loop if the mission fails
                } else {
                    cout << "Invalid choice. You lost valuable time.\n";
                }
            }
            // Ask the user if they want to continue
            cout << "Do you want to continue the mission? (1 for Yes, 0 for No): ";
            cin >> mission1;
        }

        while (mission2) {
            if (obstacle == 0) {
                cout << "You have discovered a derelict alien spacecraft:\n";
                cout << "0. Investigate the ship\n";
                cout << "1. Avoid it and continue\n";
                cout << "2. Attempt to salvage technology\n";
                int choice;
                cin >> choice;

                if (choice == 0) {
                    cout << "You found valuable data inside the alien ship.\n";
                } else if (choice == 1) {
                    cout << "You avoided the ship and continued your journey.\n";
                } else if (choice == 2) {
                    cout << "You salvaged advanced alien technology.\n";
                    mission2 = 0; // End the loop if the mission progresses
                } else {
                    cout << "Invalid choice. You lost valuable time.\n";
                }
            }
            // Ask the user if they want to continue
            cout << "Do you want to continue the mission? (1 for Yes, 0 for No): ";
            cin >> mission2;

            while (mission3) {
                if (obstacle == 0) {
                    cout << "You are exploring a mysterious nebula:\n";
                    cout << "0. Analyze the nebula's energy readings\n";
                    cout << "1. Attempt to navigate through blindly\n";
                    cout << "2. Follow a faint signal\n";
                    int choice;
                    cin >> choice;

                    if (choice == 0) {
                        cout << "You discovered a hidden wormhole leading to the signal's origin.\n";
                    } else if (choice == 1) {
                        cout << "You are lost in the nebula.\n";
                    } else if (choice == 2) {
                        cout << "You successfully navigated to the signal's source.\n";
                        mission3 = 0; // End the loop if the mission progresses
                    } else {
                        cout << "Invalid choice. You lost valuable time.\n";
                    }
                }
                // Ask the user if they want to continue
                cout << "Do you want to continue the mission? (1 for Yes, 0 for No): ";
                cin >> mission3;

                while (mission4) {
                    if (obstacle == 0) {
                        cout << "You have reached the source of the signal. An alien AI challenges you:\n";
                        cout << "0. Solve its riddle to gain access\n";
                        cout << "1. Retreat and abandon the mission\n";
                        cout << "2. Attempt to disable the AI\n";
                        int choice;
                        cin >> choice;

                        if (choice == 0) {
                            cout << "CONGRATULATIONS!!! You solved the riddle and uncovered the alien technology.\n";
                        } else if (choice == 1) {
                            cout << "MISSION FAILED. You retreated.\n";
                        } else if (choice == 2) {
                            cout << "You failed to disable the AI. MISSION FAILED.\n";
                            mission4 = 0; // End the loop if the mission fails
                        } else {
                            cout << "Invalid choice. You lost valuable time.\n";
                        }
                    }
                    // End of the mission
                    cout << "Your mission is complete.";
                    cin >> mission4;
                }
            }
        }

        cout << "Would you like to embark on another mission? (Y/N): ";
        cin >> again;
    }

    system("pause");
    return 0;
}