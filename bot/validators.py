def validate_side(side: str) -> str:
    side = side.upper()
    if side not in ("BUY", "SELL"):
        raise ValueError("side must be BUY or SELL")
    return side

def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper()
    if order_type not in ("MARKET", "LIMIT"):
        raise ValueError("order_type must be MARKET or LIMIT")
    return order_type

def validate_quantity(qty_str: str) -> float:
    try:
        qty = float(qty_str)
    except ValueError:
        raise ValueError("quantity must be a number")
    if qty <= 0:
        raise ValueError("quantity must be positive")
    return qty

def validate_price(price_str: str | None, order_type: str) -> float | None:
    if order_type == "LIMIT":
        if price_str is None:
            raise ValueError("price is required for LIMIT")
        try:
            price = float(price_str)
        except ValueError:
            raise ValueError("price must be a number")
        if price <= 0:
            raise ValueError("price must be positive")
        return price
    return None
