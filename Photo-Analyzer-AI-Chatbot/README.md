# Conversational Memory Bot

A sophisticated AI-powered conversational system with multimodal capabilities, image processing, and persistent memory management.

## 🌟 Project Overview

This project implements an advanced conversational AI system that can:
- Process and understand both text and images
- Maintain contextual memory of conversations
- Generate AI-powered descriptions and metadata
- Manage a gallery of processed images
- Provide real-time chat functionality with memory retention

## 🏗️ Project Structure

```
conversational_memory_bot/
├── backend/                 # Backend API and core logic
│   ├── db/                 # Database related files
│   ├── chat.py            # Chat functionality
│   ├── config.py          # Configuration settings
│   ├── data_loader.py     # Data loading utilities
│   ├── description_ai.py  # AI description generation
│   ├── embedings.py       # Embedding generation
│   ├── gallery.py         # Image gallery management
│   ├── home.py            # Home route handlers
│   ├── main.py            # Main FastAPI application
│   ├── metadata_ai.py     # Metadata generation
│   ├── multimodal_chat.py # Multimodal chat processing
│   ├── retriever.py       # Data retrieval utilities
│   ├── uploader.py        # File upload handling
│   ├── utility.py         # Utility functions
│   └── vectordb.py        # Vector database operations
├── frontend/              # Frontend assets
│   ├── static/           # Static files (CSS, JS, images)
│   └── templates/        # Jinja2 templates
├── research_notebooks/    # Jupyter notebooks for research
├── sample_gallery/       # Sample images and data
└── requirements.txt      # Python dependencies
```

## 🚀 Setup and Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)
- gemini api key in your .env file

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/yourusername/conversational_memory_bot.git
cd conversational_memory_bot
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```env
API_KEY=your_api_key
DATABASE_URL=your_database_url
VECTOR_DB_PATH=path_to_vector_db
MODEL_NAME=your_model_name
```

5. Start the application:
```bash
cd backend
uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`

## 🔌 API Endpoints

### Main Routes
- `GET /` - Home page
- `GET /gallery` - Image gallery view
- `POST /upload` - Upload new images
- `POST /chat` - Chat endpoint

### Chat API
- `POST /chat/start` - Start a new chat session
- `POST /chat/message` - Send a message
- `GET /chat/history` - Get chat history

### Gallery API
- `GET /gallery/images` - List all images
- `POST /gallery/upload` - Upload new image
- `GET /gallery/{image_id}` - Get specific image details

### AI Processing
- `POST /process/description` - Generate image description
- `POST /process/metadata` - Generate image metadata
- `POST /process/embedding` - Generate embeddings

## 🔧 Technologies Used

- **Backend Framework**: FastAPI
- **Database**: Vector Database (ChromaDB)
- **AI Models**: 
  - CLIP for image processing
  - LangChain for conversation management
  - Custom embedding models
- **Frontend**: Jinja2 Templates, Static Files
- **Development Tools**: Python, Jupyter Notebooks

## 📚 Dependencies

Key dependencies include:
- fastapi==0.115.8
- langchain==0.3.18
- chromadb==0.6.3
- torch==2.6.0
- transformers==4.48.3
- pillow==11.1.0
- python-multipart==0.0.20
- uvicorn==0.34.0

For a complete list, see `requirements.txt`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Thanks to all contributors and maintainers
- Special thanks to the open-source community

