#!/bin/bash

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setting up environment variables..."
echo "export API_KEY='your_api_key'" >> ~/.bashrc
echo "export SECRET_KEY='your_secret_key'" >> ~/.bashrc

echo "Running Python script..."

echo "Installation complete! Now run main.py with 'python3 main.py'"