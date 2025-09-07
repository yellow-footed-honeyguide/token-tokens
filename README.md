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

1.  Clone the repository.
2.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Run

1.  Start the server from the project's root directory:
    ```bash
    uvicorn main:app --reload
    ```
2.  Open your browser and navigate to `http://127.0.0.1:8000`.
