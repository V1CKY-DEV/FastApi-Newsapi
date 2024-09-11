# News API Project

This project is a FastAPI application that fetches and displays the latest news articles using the [News API](https://newsapi.org/). The application uses caching to improve performance and is Dockerized for easy deployment.


## Dependencies

The following Python packages are used in this project:

- `fastapi`: Web framework for building APIs.
- `uvicorn`: ASGI server for running FastAPI applications.
- `httpx`: HTTP client for making API requests.
- `jinja2`: Templating engine for rendering HTML.
- `python-dotenv`: For loading environment variables from a `.env` file.
- `cachetools`: Library for caching with TTL (Time-To-Live).

## Features

- Fetches news articles from the News API.
- Caches results to improve performance.
- Displays news articles with images, titles, and descriptions.
- Dockerized for deployment.

## Prerequisites

- Python 3.8 or higher
- Docker (for containerization)

## Setup

### Environment Variables

1. Create a `.env` file in the root directory of the project.
2. Add your News API key to the `.env` file with the following content:

    ```
    API_KEY=your_news_api_key
    ```

   Replace `your_news_api_key` with your actual API key obtained from the [News API](https://newsapi.org/).

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/news-api-project.git
    cd news-api-project
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

#### Locally

1. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

   The application will be accessible at `http://localhost:8000`.

2. Open your browser and navigate to `http://localhost:8000` to view the news feed.

#### Using Docker

1. Build the Docker image:

    ```bash
    docker build -t news-api-project .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 8000:8000 --env-file .env news-api-project
    ```

   The application will be accessible at `http://localhost:8000` in your browser.

## Project Structure

- `main.py`: The FastAPI application code.
- `templates/index.html`: The HTML template for displaying news articles.
- `.env`: Environment file containing the API key.
- `Dockerfile`: Docker configuration file.
- `requirements.txt`: Python dependencies.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [News API](https://newsapi.org/) for providing the news data.
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework.
- [Docker](https://www.docker.com/) for containerization.
