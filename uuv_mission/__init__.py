import pandas as pd

class Mission:
   
#creates a Mission object that can hold data about a mission's reference, cave height, and cave depth.   
    def __init__(self, reference, cave_height, cave_depth):
        self.reference = reference
        self.cave_height = cave_height
        self.cave_depth = cave_depth

    @classmethod
    def from_csv(cls, file_path):
        """
        Class method to create instances of the Mission class from a CSV file using pandas.
        """
        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)

        # Create a list to store Mission instances
        missions = []
        
        # Iterate over DataFrame rows and create Mission instances
        for _, row in df.iterrows():
            # Extract necessary data from the DataFrame row
            reference = row['reference']
            cave_height = row['cave_height']
            cave_depth = row['cave_depth']
            
            # Create an instance of the Mission class
            mission_instance = cls(reference, cave_height, cave_depth)
            missions.append(mission_instance)
        
        return missions

    def __repr__(self):
        return f"Mission(reference='{self.reference}', cave_height={self.cave_height}, cave_depth={self.cave_depth})"


# # Example usage
# file_path = '../data/mission.csv'
# mission_instances = Mission.from_csv(file_path)

# for mission in mission_instances:
#     print(mission)
