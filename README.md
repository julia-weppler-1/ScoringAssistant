
# Excel Processor Application -- Scoring Assistant

This Django application allows users to upload Excel files containing gymnastics scores, process the scores, and generate ranked results for different apparatus and all-around scores.

## Features

- **File Download**: Users can download a template Excel file to input details for a gymnastics competition.
- **File Upload**: Users can upload the filled-out template Excel files with gymnastics scores.
- **Data Processing**: The uploaded scores are processed to generate rankings for vault, bars, beam, floor, and all-around scores by level.
- **Results Generation**: Results are outputted in a formatted text file (.txt) with rankings and handling of ties.
- **Web Interface**: Simple web interface for uploading files and viewing/download results.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/julia-weppler-1/ScoringAssistant.git
   cd excel_processor
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**

   If using Django's default SQLite database, apply migrations:

   ```bash
   python manage.py migrate
   ```

4. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at `http://localhost:8000`.

## Usage

1. **Upload Excel File**

   - Navigate to the upload page (`/upload/`).
   - Choose an Excel file with gymnastics scores and submit the form.

2. **View and Download Results**

   - After uploading, the application processes the scores.
   - Results are displayed on the webpage with an option to download a text file containing the rankings.

## File Structure

- **excel_app/**: Django app directory containing views, models, and templates.
- **static/**: Static files (CSS, JS) for the web interface.
- **media/**: Directory for storing uploaded Excel files.

## Dependencies

- Django: Web framework for Python.
- pandas: Library for data manipulation and analysis.
- openpyxl: Library for reading and writing Excel files.
- Other dependencies listed in `requirements.txt`.

## Contributing

- Fork the repository, make changes, and submit a pull request.
- Report issues or suggest improvements by creating an issue.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---
