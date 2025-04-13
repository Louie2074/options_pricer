# Options Pricer App

This application retrieves the latest closing price of Bitcoin from InfluxDB.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Louie2074/options_pricer.git
   cd options_pricer_app
   ```
2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv

   source venv/bin/activate  # On macOS/Linux

   venv\Scripts\activate  # On Windows

   ```
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Set up your environment variables:

   Create a `.env` file in the root of your project and add your InfluxDB token:

   ```plaintext
   INFLUXDB_TOKEN=your_influxdb_token_here
   ```

## Running the App

To run the application, execute the following command:

```bash
python app.py
```

This will print the latest closing price of Bitcoin to the console.

## License

This project is licensed under the MIT License.
