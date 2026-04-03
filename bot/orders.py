import logging
from binance.exceptions import BinanceAPIException
def place_and_report_order(client, symbol, side, order_type, quantity, price=None, logger=None):
    summary = {"symbol": symbol, "side": side, "type": order_type, "quantity": quantity, "price": price}
    if logger: logger.info(f"Order request: {summary}")
    try:
        response = client.place_order(symbol, side, order_type, quantity, price)
        if logger: logger.info(f"Order response: {response}")
        result = {"success": True, "orderId": response.get("orderId"), "status": response.get("status"), "executedQty": response.get("executedQty"), "avgPrice": response.get("avgPrice")}
    except BinanceAPIException as e:
        if logger: logger.error(f"BinanceAPIException: {e}")
        result = {"success": False, "error": str(e)}
    except Exception as e:
        if logger: logger.error(f"Unexpected error: {e}")
        result = {"success": False, "error": str(e)}
    return summary, result
