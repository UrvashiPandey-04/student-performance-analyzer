def load_data(file_path):
    students = []

    with open(file_path, "r") as file:
        lines = file.readlines()

        
        for line in lines[1:]:
            line = line.strip()  
            parts = line.split(",") 

            student = {
                "Name": parts[0],
                "Maths": int(parts[1]),
                "Science": int(parts[2]),
                "English": int(parts[3])
            }

            students.append(student)

    return students