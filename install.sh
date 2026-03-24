#!/bin/bash

set -e  # stop on error

echo "📦 Downloading project..."

# Detect OS (optional but pro)
OS="$(uname)"

# Download repo
curl -L -o code.zip https://github.com/Hariom-Jaiswal/code/archive/refs/heads/main.zip

echo "📂 Extracting files..."
unzip -q code.zip

cd code-main

echo "⚙️ Running setup..."

# Example setup (customize this)
if [ -f requirements.txt ]; then
    echo "Installing Python dependencies..."
    pip install -r requirements.txt
fi

if [ -f package.json ]; then
    echo "Installing Node dependencies..."
    npm install
fi

echo "✅ Done! Your project is ready."