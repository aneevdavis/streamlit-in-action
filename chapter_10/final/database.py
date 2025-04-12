users = {
    1: {
        "first_name": "Alice",
        "last_name": "Johnson",
        "date_of_birth": "1990-05-14",
        "email_address": "alice.johnson@example.com"
    },
    2: {
        "first_name": "Bob",
        "last_name": "Smith",
        "date_of_birth": "1985-08-22",
        "email_address": "bob.smith@example.com"
    }
}

orders = {
    101: {
        "user_id": 1,
        "order_placed_date": "2025-02-10",
        "order_status": "Shipped",
        "tracking_number": "TRK123456789",
        "items_purchased": ["RoyalQuill", "RedPinner"],
        "quantity": [1, 1],
        "shipping_address": "123 Main St, Springfield, IL, 62701",
        "expected_delivery_date": "2025-02-18"
    },
    102: {
        "user_id": 2,
        "order_placed_date": "2025-02-12",
        "order_status": "Processing",
        "tracking_number": None,
        "items_purchased": ["GripLink", "ScribePad"],
        "quantity": [1, 2],
        "shipping_address": "456 Oak St, Denver, CO, 80203",
        "expected_delivery_date": "2025-02-26"
    },
    103: {
        "user_id": 1,
        "order_placed_date": "2025-02-15",
        "order_status": "Delivered",
        "tracking_number": "TRK987654321",
        "items_purchased": ["PaperCharm", "RoyalQuill"],
        "quantity": [1, 1],
        "shipping_address": "123 Main St, Springfield, IL, 62701",
        "expected_delivery_date": "2025-02-16"
    }
}
