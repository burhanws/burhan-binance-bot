import argparse
from bot.client import BinanceFuturesClient
from bot.orders import place_and_report_order
from bot.validators import validate_side, validate_order_type, validate_quantity, validate_price
from bot.logging_config import setup_logger
def parse_args():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True, dest="order_type")
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")
    return parser.parse_args()
def main():
    args = parse_args()
    logger = setup_logger()
    try:
        side = validate_side(args.side)
        order_type = validate_order_type(args.order_type)
        qty = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)
    except ValueError as e:
        print(f"Input error: {e}")
        return
    client = BinanceFuturesClient()
    summary, result = place_and_report_order(client, args.symbol, side, order_type, qty, price, logger)
    print("=== Request ===")
    for k,v in summary.items(): print(f"{k}: {v}")
    print("\n=== Result ===")
    if result["success"]:
        print(f"ID: {result['orderId']} Status: {result['status']}")
        print("SUCCESS")
    else:
        print(f"FAILED: {result['error']}")
if __name__ == "__main__": main()
