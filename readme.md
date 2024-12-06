# AI Coding Assistant

This project is an AI-powered coding assistant that uses OpenAI's GPT-3.5 and Google's Gemini AI to help with code generation, explanation, and modification.

## Setup

### Prerequisites

- Python 3.6 or higher
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/aayush-ojha/ai-coding-assistant.git
    cd ai-coding-assistant
    ```

2. Create and activate a virtual environment:

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up your API keys:

    - Open the `api_keys.py` file and add your API keys for OpenAI and Gemini:

    ```python
    gemini_api_key = 'your_gemini_api_key' # Your Gemini API key
    openai_api_key = 'your_openai_api_key' # Your OpenAI API key
    ```

## Usage

1. Run the main script:

    ```sh
    python3 main.py
    ```

2. Follow the prompts to choose between OpenAI and Gemini, and specify the action you want to perform (explain code, write code, or modify code).

## Example

```sh
Choose an option:
1. OpenAI
2. Gemini
2
What would you like Gemini to do:
1. Explain Code
2. Write Code
3. Modify Code
1
Enter the code you want to explain: import cv2
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
