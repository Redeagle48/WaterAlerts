# Water Alerts

Water Alerts is a Python-based application designed to scrape water outage information from a specified website, process the data using OpenAI's API, and publish the results to an MQTT broker.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Crontab Running Script](#crontab-Running-Script)
- [Testing](#testing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Redeagle48/WaterAlerts.git
    cd WaterAlerts
    ```

2. Create a virtual environment:

    ```sh
    python -m venv .venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```sh
        .venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source .venv/bin/activate
        ```

4. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Copy the `config.toml` file to the root directory of the project and update the configuration values as needed:

    ```toml
    [mqtt]
    broker = "<broker ip>" 
    port = "<broker port>"
    user = "<mqtt user>"
    password = "<mqtt pass>"
    topic = "<mqtt topic>"

    [openai]
    api_key = "<openai api key>"
    model = "<openai model>"
    ```

## Running the Application

To run the application, execute the following command:

```sh
python src/water_alerts.py
```

This will start the process of scraping water outage information, processing it with OpenAI, and publishing the results to the MQTT broker.

## Crontab Running Script

### Execution job
```console
*/30 * * * * /bin/bash -c 'source <path to>/venv/bin/activate && python <path to>/src/water_alerts.py' >> <path to>/logs/script.log 2>&1
```

### Truncate log file
```console
0 0 */7 * * truncate -s 0 <path to>/logs/script.log
```

## Testing

To run the unit tests, use the following command:

```sh
python -m unittest discover -s tests
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
