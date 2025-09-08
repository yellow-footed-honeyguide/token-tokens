# Token tokens
Web tool to see your OpenAI API costs before you spend a dime.

A web tool to see your OpenAI API costs *before* you spend a dime.
Built with FastAPI and Tiktoken, this tool visualizes token count, estimated cost, and the tokens themselves for text or PDF files.

## Core Features

*   **Count Tokens:** See the exact token count for any text.
*   **Estimate Cost:** Instantly see the estimated cost based on GPT-4 Turbo pricing.
*   **Visualize Tokens:** Understand how your text is broken down into individual tokens.
*   **PDF Support:** Upload a PDF to extract and analyze its entire text content.

## Setup

Setup
1. Install Poetry.
2. Clone the repository:
```bash
git clone https://github.com/your-username/token-tokens.git
cd token-tokens
```
3. Install the dependencies:
```bash
poetry install
```

Clone the repository:

## Run

1.  Start the server:
    ```bash
    poetry run uvicorn main:app --reload
    ```
2.  Open your browser and navigate to http://127.0.0.1:8000.

## Contributing

Contributions to the File Information Utility are welcome! Please feel free to submit a Pull Request.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Author

**Sergey Veneckiy**
- Email: s.venetsky@gmail.com
- GitHub: [@yellow-footed-honeyguide](https://github.com/yellow-footed-honeyguide)
