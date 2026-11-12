def parse_replicas(value: str) -> int:
    """Parse a replica count between 1 and 5, inclusive."""
    replicas = int(value)
    if not 1 <= replicas < 5:
        raise ValueError("replicas must be between 1 and 5")
    return replicas
