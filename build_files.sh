echo "BUILD START"
#!/bin/bash

# Install the dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files without user interaction
python manage.py collectstatic --noinput

# Run any necessary migrations
python manage.py migrate

echo "BUILD END"
