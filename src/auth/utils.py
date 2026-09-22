from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"])


def generate_password_hash(password: str) -> str:
    """Generates a password hash.

    Args:
        password (str): raw password string.
    """
    return password_context.hash(password)


def verify_password(password: str, hash: str) -> bool:
    """Verifies a password against a hash.

    Args:
        password (str): raw password string.
        hash (str): hashed password string.
    """
    return password_context.verify(password, hash)
