#include <iostream>
#include <string>
#include <limits>

using namespace std;

class Player {
protected:
    string rank;
    string name;

public:
    void setDetails() {
        cout << "Enter your astronaut rank: ";
        cin >> rank;
        cout << "What is your name? ";
        cin >> name;
    }

    virtual void displayDetails() const {
        cout << "Astronaut Rank: " << rank << ", Name: " << name << endl;
    }
};

class Mission : public Player {
public:
    void startMission() {
        cout << "=== Welcome to Mission: Stellar Depth ===\n";
        cout << "After intercepting a mysterious signal from deep space, a crew of astronauts boards\n";
        cout << "the starship *Aurora Prime* to explore an uncharted star system near the edge of the galaxy.\n";
        cout << name << ", holding the rank of " << rank << ",  the crew awaits orders\n";
        cout << "that danger lurks beyond known space, and the mission could change humanity forever.\n";
    }

    int chooseDirection() {
        int direction;
        cout << "Choose your hyperspace jump direction (1 for Alpha Quadrant, 2 for Beta Quadrant, etc.): ";
        while (!(cin >> direction)) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Invalid input. Please enter a number: ";
        }
        return direction;
    }
};

class Starship {
private:
    int year;
    string type;
    int speed = 0;

public:
    void setDetails() {
        cout << "Enter the year your starship was built: ";
        cin >> year;
        cout << "Enter the starship model: ";
        cin >> type;
        cout << "Enter the warp speed capability: ";
        cin >> speed;
    }

    void setDetails2() const {
        cout << "Starship Year: " << year << ", Model: " << type << endl;
        cout << "Warp Speed: " << speed << endl;
    }
};

int main() {
    char again = 'Y';
    int Intcounter1 = 1;
    int Intcounter2 = 1;
    int Intcounter3 = 1;
    int Intcounter4 = 1;
    int obstacle = 0;

    while (again == 'Y' || again == 'y') {
        Mission mission;
        mission.setDetails();
        mission.startMission();

        Starship starship;
        starship.setDetails();
        starship.setDetails2();

        int direction = mission.chooseDirection();
        cout << "The crew jumps to hyperspace towards quadrant " << direction << "...\n";

        while (Intcounter1) {
            if (obstacle == 0) {
                cout << "You encounter a massive asteroid field! Choose your action:\n";
                cout << "0. Navigate carefully around it\n";
                cout << "1. Boost shields and push through\n";
                cout << "2. Fire weapons to clear a path\n";
                int choice;
                cin >> choice;

                if (choice == 0) {
                    cout << "You avoided the asteroid field successfully.\n";
                } else if (choice == 1) {
                    cout << "You made it through with minor damage.\n";
                } else if (choice == 2) {
                    cout << "Your ship was destroyed. MISSION FAILED.\n";
                    Intcounter1 = 0;
                } else {
                    cout << "Invalid choice. You lost precious time.\n";
                }
            }
            cout << "Continue the mission? (1 for Yes, 0 for No): ";
            cin >> Intcounter1;

            while (Intcounter2) {
                if (obstacle == 0) {
                    cout << "You detect a derelict alien vessel drifting in space:\n";
                    cout << "0. Dock and explore\n";
                    cout << "1. Scan from a distance\n";
                    cout << "2. Ignore and move on\n";
                    int choice;
                    cin >> choice;

                    if (choice == 0) {
                        cout << "You board the vessel and find advanced technology.\n";
                    } else if (choice == 1) {
                        cout << "Scans reveal strange life readings...\n";
                    } else if (choice == 2) {
                        cout << "You continue your journey.\n";
                        Intcounter2 = 0;
                    } else {
                        cout << "Invalid choice. The vessel vanishes.\n";
                    }
                }
                cout << "Continue the mission? (1 for Yes, 0 for No): ";
                cin >> Intcounter2;

                while (Intcounter3) {
                    if (obstacle == 0) {
                        cout << "A mysterious planet appears in your path:\n";
                        cout << "0. Land and investigate\n";
                        cout << "1. Scan for resources\n";
                        cout << "2. Attempt communication with the surface\n";
                        int choice;
                        cin >> choice;

                        if (choice == 0) {
                            cout << "You discover ancient alien ruins.\n";
                        } else if (choice == 1) {
                            cout << "You collect valuable resources.\n";
                        } else if (choice == 2) {
                            cout << "A friendly alien civilization welcomes you.\n";
                            Intcounter3 = 0;
                        } else {
                            cout << "Invalid choice. You drift aimlessly.\n";
                        }
                    }
                    cout << "Continue the mission? (1 for Yes, 0 for No): ";
                    cin >> Intcounter3;

                    while (Intcounter4) {
                        if (obstacle == 0) {
                            cout << "Final Challenge: An interstellar guardian blocks your way to the signal's source:\n";
                            cout << "0. Engage in a tactical space battle\n";
                            cout << "1. Attempt peaceful communication\n";
                            cout << "2. Retreat to safety\n";
                            int choice;
                            cin >> choice;

                            if (choice == 0) {
                                cout << "VICTORY! The guardian grants you access to the source — a new world for humanity.\n";
                            } else if (choice == 1) {
                                cout << "The guardian shares knowledge and lets you pass.\n";
                            } else if (choice == 2) {
                                cout << "Mission aborted.\n";
                                Intcounter4 = 0;
                            } else {
                                cout << "Invalid choice. The guardian attacks.\n";
                            }
                        }
                        cout << "MISSION COMPLETE.\n";
                        cin >> Intcounter4;

                        system("pause");
                        return 0;
                    }
                }
            }
        }
    }
}
