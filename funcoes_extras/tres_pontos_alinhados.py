# Verifica se três pontos estão alinhados
def tres_pontos_alinhados(p1, p2, p3):
    """
    Checks if three 2D points are aligned in a straight line.
    Each point should be a tuple or list of (x, y).
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    # Calculate the cross product of vectors (p2-p1) and (p3-p2)
    # Formula: (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
    cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
    
    # Use a small tolerance for floating-point numbers
    return abs(cross_product) < 1e-12