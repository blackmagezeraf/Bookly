from src.config import Config
from uvicorn import run

if __name__ == "__main__":
    run(
        app="src:app",
        host=Config.HOST,
        port=Config.PORT,
        reload=Config.RELOAD,
        reload_dirs=Config.RELOAD_DIRS,
        reload_includes=Config.RELOAD_INCLUDES,
    )
