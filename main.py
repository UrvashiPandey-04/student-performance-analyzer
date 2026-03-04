from utils.file_handler import load_data
from utils.analyzer import generate_report


def main():
    # Load student data from CSV file
    data = load_data("data/students.csv")

    # Generate analysis report
    generate_report(data)


# Run the program
if __name__ == "__main__":
    main()