def filter_underage_data(filename):
    # Initialize an empty list to store underage data
    underage_data = []
    
    try:
        # Open the text file
        with open(filename, 'r') as file:
            # Skip the header row
            file.readlines()
            
            # Process each line
            for line in file:
                # Remove whitespace and split by comma
                line = line.strip()
                
                # Skip empty lines
                if not line:
                    continue
                
                # Split the line into parts
                parts = line.split(',')
                
                # Ensure we have the expected number of parts
                if len(parts) >= 3:
                    name = parts[0]
                    email = parts[1]
                    
                    # Convert age to integer for comparison
                    try:
                        age = int(parts[2])
                        
                        # Check if age is less than 17
                        if age < 17:
                            underage_data.append({
                                'name': name,
                                'email': email,
                                'age': age
                            })
                    
                    except ValueError:
                        # Skip lines with invalid age
                        continue
    
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    
    # Check if underage_data is empty
    if not underage_data:
        print("Data is empty")
        return []
    
    # Print underage data
    for person in underage_data:
        print(f"Name: {person['name']}, Email: {person['email']}, Age: {person['age']}")
    
    return underage_data

# Usage
filename = './books_database.txt'
result = filter_underage_data(filename)