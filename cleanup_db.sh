# Go to project dir
cd ~/django-restql-playground-backend

# Flush data
python3 manage.py flush --no-input

# Fill demo data
python3 manage.py loaddata \
api/fixtures/initial_genre_data.json \
api/fixtures/initial_book_data.json \
api/fixtures/initial_course_data.json \
api/fixtures/initial_student_data.json \
api/fixtures/initial_phone_data.json