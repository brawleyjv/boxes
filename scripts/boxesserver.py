import sys
import os

# Add the path to the boxesserver.py file
boxesserver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../boxes/boxes/scripts'))
print(f"Adding {boxesserver_path} to sys.path")
sys.path.append(boxesserver_path)

# Print sys.path for debugging
print("sys.path:", sys.path)

# Import the main function from boxesserver.py
try:
    from boxesserver import main
except ImportError as e:
    print(f"Error importing boxesserver: {e}")
    sys.exit(1)

if __name__ == "__main__":
    main()