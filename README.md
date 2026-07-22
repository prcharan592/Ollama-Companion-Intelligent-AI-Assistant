# Ollama Companion — Intelligent AI Assistant

An AI-powered chatbot that leverages Ollama's locally running LLMs to deliver intelligent, context-aware responses. Completely offline and private — no data ever leaves your machine.

## Features

- **Local LLM Powered** — Runs entirely on your machine using Ollama.
- **Context-Aware Chat** — Maintains conversation history for coherent multi-turn dialogues.
- **Multiple Model Support** — Switch between any Ollama-supported model (Llama, Mistral, etc.).
- **Privacy First** — No API keys, no cloud, no data leaving your system.
- **Fast Responses** — Optimized for low-latency local inference.

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python |
| LLM Runtime | [Ollama](https://ollama.ai) |
| Interface | CLI / Python |

## Getting Started

### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai) installed and running
- At least one model pulled (e.g., `ollama pull llama3`)

### Installation

```bash
git clone https://github.com/prcharan592/Ollama-Companion-Intelligent-AI-Assistant.git
cd Ollama-Companion-Intelligent-AI-Assistant
pip install -r requirements.txt
```

### Running the Application

Make sure Ollama is running, then:

```bash
python main.py
```

## Usage

1. Start the assistant.
2. Type your question or prompt.
3. The local LLM generates a response.
4. Continue the conversation — context is preserved across turns.

## Contributing

Contributions are welcome! Please open an issue first to discuss what you'd like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Contact

**prcharan592** — [GitHub Profile](https://github.com/prcharan592)
