Welcome to GenAI Portuguese Tutor, an immersive storytelling experience that blends Portuguese Learning, Sightseeing Tips, and Generative AI. Explore the beauty of Rio de Janeiro while learning Portuguese through engaging narratives and artistic visuals.

## Features
- Interactive storytelling with Generative AI
- Learn Portuguese through real-life scenarios set in Rio de Janeiro
- Visualize stories through images generated in the style of famous artists

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Streamlit
- OpenAI API Key

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/felipeyoshi/bod-portuguese-class.git
    cd genai-portuguese-tutor
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.streamlit` directory and add a `secrets.toml` file with your OpenAI API key:
    ```bash
    mkdir .streamlit
    echo "[open_ai]\noapi_key = \"YOUR_API_KEY\"" > .streamlit/secrets.toml
    ```

### Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Select the chapters and artist style in the sidebar, then click "Generate Story" to create your personalized learning experience.

## Files

- `app.py`: The main Streamlit app script.
- `llm_utils.py`: Contains the `LLM` class for interacting with OpenAI's API.
- `prompts.py`: Contains the chapter prompts used in the app.
- `requirements.txt`: Lists the Python packages required to run the app.

## Acknowledgements

- [OpenAI](https://www.openai.com/) for providing the API for text and image generation.
- [Streamlit](https://www.streamlit.io/) for making it easy to create interactive web applications.

## Disclaimer

This application uses AI to generate text and images. Please be aware that the content generated may not always be accurate or appropriate. If you encounter any issues, try adjusting your input or prompt.

---

Enjoy your journey through Rio de Janeiro with GenAI Portuguese Tutor!