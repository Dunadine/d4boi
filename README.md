# Aspect Tracker Application

The Aspect Tracker Application is a command-line tool that allows users to track and manage aspects for different character classes in a role-playing game (RPG).

![Screenshot 2023-06-12 201033](https://github.com/Dunadine/d4boi/assets/68076384/b7031839-fe24-4fdd-90b5-fe1b8221c8a4)

![Screenshot 2023-06-12 201047](https://github.com/Dunadine/d4boi/assets/68076384/120acc15-ccdb-4fbf-be91-42657244142f)

![Screenshot 2023-06-12 201219](https://github.com/Dunadine/d4boi/assets/68076384/c883bee8-b4f7-477a-96c4-afae98d798d8)

## Setup

1. Clone the repository or download the source code files to your local machine.

2. Make sure you have Python 3.x installed on your system.

3. Install the required dependencies by running the following command:

```
To run the application, you will need to execute the following commands in the terminal:

1. Make sure you have Python installed on your system. You can check by running the command: `python --version`. If Python is not installed, you can download and install it from the official Python website: https://www.python.org/downloads/

2. Navigate to the directory where you have saved the `main.py` file using the `cd` command. For example, if the file is located in the "Documents" folder, you can use: `cd Documents` to navigate to that directory.

3. Install the necessary dependencies by running the command: `pip install pyfiglet`. This will install the `pyfiglet` package, which is used for ASCII art generation.

4. Once the dependencies are installed, you can run the application by executing the command: `python main.py`. This will start the program and display the initial prompt.

5. Follow the instructions provided by the application to select your class, enter aspect details, view aspects, delete aspects, and perform other actions.

6. When you choose to quit the application, the aspect details will be saved to a file, and the file path will be displayed in the terminal.

Note: Make sure you have write permissions for the directory where the application is located, as it will create and modify files in that directory.
```

## Usage

1. Open a terminal or command prompt and navigate to the directory where you cloned or downloaded the application.

2. Run the `main.py` script using Python:

4. Follow the prompts to select a character class, manage aspects, and add or delete entries for aspects.

4. The application will display the aspect table with the current entries after each modification.

## Features

- **Select Character Class**: Choose a character class from the available options.

- **Manage Aspects**: View and select aspects for the chosen character class. The aspects are categorized into "General Aspects" and "Class Aspects".

- **Add Entries**: Add new entries for selected aspects, including dynamic values.

- **Delete Entries**: Delete existing entries for aspects.

- **Search Aspects**: Search for aspects by name and view matching entries.

## Data Files

The application uses the following data files:

- `class_data.py`: Contains the class options and aspect names for each class.

- `user_class.txt`: Stores the user's selected character class.

- `aspects_<class_name>.txt`: Stores the aspect entries for each class.

## Contributing

Contributions to the Aspect Tracker Application are welcome! If you find any issues or have suggestions for improvements, please submit an issue or pull request on the project repository.

## License

The Aspect Tracker Application is open-source and released under the [MIT License](LICENSE).
