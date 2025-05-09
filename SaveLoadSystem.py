
# NOTE: Import Section
# Imports required modules for the file
import os

# Save/Load System class that saves and loads all game data into and out of a text file.
class SaveLoadSystem:
    def __init__(self, file_extension, save_folder) -> None:
        """
        Initializes the variables for file saving and loading.
        Parameters:
            file_extension: Extension of the file to be saved. (.txt, .csv, etc.)
            save_folder: Folder to save the file to.
        """

        # Initializes the required file variables.
        self.file_extension = file_extension
        self.save_folder = save_folder

    def save_data(self, data, name) -> None:
        """
        Saves singular files and data.
        Parameters:
            data: Data to be saved.
            name: Name of the file.
        Returns:
            None
        """

        # Saves the data presented into a new overwritten file.
        data_file = open(self.save_folder + os.sep + name + self.file_extension, "w")
        for item in data:
            data_file.write(f"{item} ")

    def load_data(self, name) -> list:
        """
        Loads singular files and data.
        Parameters:
            name: Name of the file.
        Returns:
             list: List of data loaded.
        """

        # Loads the data from the named file presented and returns it as a list.
        data_file = open(self.save_folder + os.sep + name + self.file_extension, "r")
        data = [int(float(item)) for item in data_file.read().split()]
        return data

    def check_for_file(self, name) -> bool:
        """
        Checks if a file exists.
        Parameters:
            name: Name of the file.
        Returns:
             bool: True if the file exists, otherwise False.
        """

        return os.path.exists(self.save_folder + os.sep + name + self.file_extension)

    def load_game_data(self, files_to_load, default_data) -> tuple:
        """
        Loads more than one file of data.
        Parameters:
            files_to_load: List of files to load.
            default_data: Default data to be returned if no file is found.
        Returns:
            tuple: Tuple containing the loaded data.
        """

        # Loops to check if a file exists and loads it.
        variables = []
        for index, file in enumerate(files_to_load):
            if self.check_for_file(file):
                variables.append(self.load_data(file))
            else:
                variables.append(default_data[index])

        # Returns the data loaded.
        if len(variables) > 1:
            return tuple(variables)
        else:
            return variables[0]

    def save_game_data(self, data_to_save, file_names) -> None:
        """
        Saves multiple files of data.
        Parameters:
            data_to_save: Data to be saved.
            file_names: List of file names to be saved with data.
        Returns:
            None
        """

        # Saves each file with its associated name and data.
        for index, file in enumerate(data_to_save):
            self.save_data(file, file_names[index])