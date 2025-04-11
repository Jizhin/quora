#!/bin/bash

# Exit on error
set -e

# Apply migrations
echo "Applying database migrations..."
python manage.py migrate
