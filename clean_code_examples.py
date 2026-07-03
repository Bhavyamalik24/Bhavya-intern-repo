def calculate_average_score(scores: list, passing_threshold: float) -> dict:
    if not isinstance(scores, list):
        raise TypeError(f"Expected a list of scores, got {type(scores).__name__}")
    if not isinstance(passing_threshold, (int, float)):
        raise TypeError(f"passing_threshold must be a number")
    if not scores:
        raise ValueError("scores list cannot be empty")
    for i, score in enumerate(scores):
        if not isinstance(score, (int, float)):
            raise TypeError(f"Score at index {i} must be a number")
        if not 0 <= score <= 100:
            raise ValueError(f"Score at index {i} is {score} — scores must be between 0 and 100")
    if not 0 <= passing_threshold <= 100:
        raise ValueError(f"passing_threshold must be between 0 and 100, got {passing_threshold}")
    total = sum(scores)
    average = total / len(scores)
    passing = [s for s in scores if s >= passing_threshold]
    pass_rate = len(passing) / len(scores) * 100
    return {
        "average": round(average, 2),
        "pass_rate": round(pass_rate, 2),
        "highest": max(scores),
        "lowest": min(scores)
    }