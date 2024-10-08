# MoviesProject

MoviesProject is a Django web application that allows users to browse and review movies.

## Prerequisites

Before you begin, ensure you have the following installed on your machine: 
- Python 3.x 
- pip 
- Git 

## Installation

1. **Clone the repository:** 
   Open your terminal and run the following command to clone the repository to your local machine: 
   `git clone https://github.com/yourusername/moviesProject.git` 
   (replace `yourusername` with your actual GitHub username).

2. **Navigate to the project directory:** 
   `cd moviesProject`

3. **Create a virtual environment (optional but recommended):** 
   `python -m venv venv`

4. **Activate the virtual environment:** 
   - On Windows: `venv\Scripts\activate` 
   - On macOS/Linux: `source venv/bin/activate`

5. **Install the required packages:** 
   `pip install -r requirements.txt`

## Running the Project

1. **Apply database migrations:** 
   `python manage.py migrate`

2. **Create a superuser (optional):** 
   If you want to access the admin panel, create a superuser account: 
   `python manage.py createsuperuser`

3. **Run the development server:** 
   `python manage.py runserver`

4. **Access the application:** 
   Open your web browser and go to `http://127.0.0.1:8000/` to view the application.

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
