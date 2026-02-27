from pathlib import Path


class ArgumentValidator:
    @staticmethod
    def validate_quality(quality: int) -> bool:
        return quality >= 1 and quality <= 100

    @staticmethod
    def validate_directory_strict(dirpath: str) -> bool:
        path = Path(dirpath)
        try:
            _ = path.resolve()
            return path.is_dir()
        except OSError:
            return False
    
    @staticmethod
    def validate_directory(dirpath: str) -> bool:
        path = Path(dirpath)
        try:
            _ = path.resolve()
            return True
        except OSError:
            return False
