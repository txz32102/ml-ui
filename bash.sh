#!/bin/bash

# Function to start web apps
start_apps() {
    # Start dodrio
    (cd dodrio && nvm use 20 && npm run dev)

    # Start frontend
    (cd frontend && nvm use 20 && npm run serve)

    # Start cnn-explainer
    (cd cnn-explainer && nvm use 20 && npm run dev)

    # Start wizmap
    (cd wizmap && nvm use 20 && npm run dev)
}

# Check if the first argument is 'run'
if [ "$1" = "run" ]; then
    start_apps
else
    echo "Invalid argument. Use 'run' to start the apps."
fi
