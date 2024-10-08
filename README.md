# FastHTML App Template

This repository provides a template for developing FastHTML applications with a structured approach to frontend and backend development, containerization, and development environment setup.

## Project Structure

- `app/`: Contains frontend-related code
  - `components/`: Reusable FastHTML components
  - `public/`: Static assets. 
      - `data/` Example images to display.
  - `javascript/`: Client-side JavaScript files
  - `app.py`: Main FastHTML application file
- `package_name/`: Backend package (replace with your actual package name)
- `docker/`: Dockerfile for production and development
- `.devcontainer/`: VS Code development container configuration
- `config/`: Configuration files
- `tests/`: Test files
- `evaluation/`: Evaluation methods
- `scripts/`: scripts that can be called from command line

## Technologies Used

1. [FastHTML](https://docs.fastht.ml/): A Python library for creating server-rendered hypermedia applications
2. [Poetry](https://python-poetry.org/): Dependency management and packaging
3. [Docker](https://www.docker.com/): Containerization
4. [VSC/Cursor Remote - Containers](https://code.visualstudio.com/docs/remote/containers): Development environment

## Getting Started

### Prerequisites

- Docker
- VS Code with Remote - Containers extension (for development)

### Development Setup

1. Clone this repository:
   ```
   git clone <repository-url>
   cd <repository-name>
   ```

2. Open the project in VS Code:
   ```
   code .
   ```

3. When prompted, click "Reopen in Container" or use the command palette (F1) and select "Remote-Containers: Reopen in Container".

4. VS Code will build the development container and set up the environment. This may take a few minutes the first time.

5. Once the container is ready, you can start developing. 

### Running the Application

To run the application outside of the development container:

1. Ensure you have Docker and Docker Compose installed.

2. Build and run the application (`-d` in background):
   ```
   docker-compose up -d
   ```

3. Access the application at `http://localhost:5010`.

## Project Configuration

### Poetry

This project uses Poetry for dependency management. The `pyproject.toml` file defines the project dependencies and settings.

To add a new dependency:
```
poetry add <package-name>
```

### FastHTML

The main FastHTML application is defined in `app/app.py`. Components are stored in `app/components/` for reusability.

### Backend Package

The `package_name` directory contains the backend code. This is installed as a package, allowing easy imports throughout the project.

### Docker

- `docker/app.Dockerfile`: Production Docker image
- `docker/dev.Dockerfile`: Development Docker image
- `docker-compose.yml`: Defines the service for running the application

### VS Code Development Container

The `.devcontainer/devcontainer.json` file configures the development container for VS Code, ensuring a consistent development environment.

## Testing

Tests are located in the `tests/` directory. Run tests using your preferred Python testing framework.

## Evaluation

The `evaluation/` directory contains methods for evaluating the application's performance or other metrics.

## Contributing

[Add contribution guidelines here]

## License

[Add license information here]
