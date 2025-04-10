
import os
import sys

# Get the project root directory (parent of 'processador_web')
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from app import app

if __name__ == '__main__':
    app.run(debug=True)