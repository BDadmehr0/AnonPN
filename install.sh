#!/bin/bash

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Set up environment variables
echo "Setting up environment variables..."
echo "export API_KEY='your_api_key'" >> ~/.bashrc
echo "export SECRET_KEY='your_secret_key'" >> ~/.bashrc

# Execute Python script
echo "Running Python script..."
#python main.py

echo "Installation complete! Now run main.py with 'python3 main.py'"
