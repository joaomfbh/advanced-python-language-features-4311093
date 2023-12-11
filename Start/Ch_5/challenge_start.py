from enum import Enum
# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for Structural Pattern Matching

# Dry Clean: [garment, size, starch, same_day]
#   garments are shirt, pants, jacket, dress
#   each item is 12.95, plus 2.00 for starch
#   same day service adds 10.00 per same-day item
# Wash and Fold: [description, weight]
#   4.95 per pound, with 10% off if more than 15 pounds
# Blankets: [type, dryclean, size]
#   type is "comforter" or "cover"
#   Flat fee of 25.00
# ---
# Output:
# Order Total Price

test_orders = [
    [
        ["shirt", "L", True, False],
        ["shirt", "M", True, False],
        ["shirt", "L", False, True],
        ["pants", "M", False, True],
        ["pants", "S", False, False],
        ["pants", "S", False, False],
        ["jacket", "M", False, False],
        ["jacket", "L", False, True]
    ],
    [
        ["dress", "M", False, True],
        ["whites", 5.25],
        ["darks", 12.5]
    ],
    [
        ["shirts and jeans", 28.0],
        ["comforter", False, "L"],
        ["cover", True, "L"],
        ["shirt", "L", True, True]
    ]
]

class Laundry(Enum):
    dry_clean = 12.95
    starch = 2.0
    same_day_svc = 10.0
    wash_and_fold = 4.95
    blankets = 25.0


for orders in test_orders:
    order_total = 0.0
    for order in orders:
        match order:
            # Wash and Fold
            case str() as desc, float() as weight:
                print(f"Wash and Fold: {desc}, weight: {weight}")
                order_total += weight * Laundry.wash_and_fold.value
                if weight >= 15.0:
                    order_total -= order_total * 0.1
            # Blankets        
            case str() as type, bool() as dryclean, str() as size:
                print(f"Blankets: ({size}) {type}", "Dry Clean" if dryclean else "")
                order_total += Laundry.blankets.value
            # Dry Clean
            case str() as garment, str() as size, bool() as starch, bool() as same_day:
                print(f"Dry Clean: ({size}) {garment}", "Starched" if starch else "",
                      "Same Day" if same_day else "")
                order_total += Laundry.dry_clean.value
                if starch:
                    order_total += Laundry.starch.value
                if same_day:
                    order_total += Laundry.same_day_svc.value

    print(f"Order total: {order_total:.2f}")
    print("-------------------")