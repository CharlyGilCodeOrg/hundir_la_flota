import logging

def configurar_logger(nombre: str = "servidor") -> logging.Logger:
    """
    Configura y devuelve un logger para el proyecto.

    Args:
        nombre (str): nombre del logger

    Returns:
        logging.Logger: logger configurado
    """

    logger = logging.getLogger(nombre)

    if not logger.handlers:

        logger.setLevel(logging.INFO)

        handler = logging.StreamHandler()

        formato = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s",
            datefmt="%H:%M:%S"
        )

        handler.setFormatter(formato)
        logger.addHandler(handler)

    return logger
