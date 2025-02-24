from database import users, orders

def retrieve_user_id(email: str, dob: str) -> int:
  """
  Look up a user's user ID, given their email address and date of birth.

  If the user is not found, return None.

  Args:
    email (str): The email address of the user.
    dob (str): The date of birth of the user in the format "YYYY-MM-DD".

  Returns:
    int: The user ID of the user, or None if the user is not found.
  """
  for user_id, user_info in users.items():
    if (user_info["email_address"] == email and
        user_info["date_of_birth"] == dob):
      return user_id

def get_order_id(user_id: int, order_placed_date: str) -> int:
  """
  Look up an order ID, given a user ID and the order placed date.

  If the order is not found, return None.

  Args:
    user_id (int): The user ID of the user.
    order_placed_date (str): The date the order was placed in the format
      "YYYY-MM-DD".

  Returns:
    int: The order ID of the order, or None if the order is not found.
  """
  for order_id, order_info in orders.items():
    if (order_info["user_id"] == user_id and
        order_info["order_placed_date"] == order_placed_date):
      return order_id

def get_order_status(order_id: int) -> dict:
  """
  Look up an order's status info, given an order ID. The status info
  includes the order status, tracking number, and expected delivery date.

  If the order is not found, return None.

  Args:
    order_id (int): The order ID of the order.

  Returns:
    dict: The order status information, or None if the order is not found.
      The dictionary has three keys:
        - "order_status": The status of the order, which is one of:
          "Processing", "Shipped", "Delivered", or "Canceled".
        - "tracking_number": The tracking number of the order, if it has
          been shipped or delivered.
        - "expected_delivery_date": The expected delivery date of the order.
  """
  order_info = orders.get(order_id)
  if order_info:
    return {
      "order_status": order_info["order_status"],
      "tracking_number": order_info.get("tracking_number"),
      "expected_delivery_date": order_info["expected_delivery_date"]
    }

def cancel_order(order_id: int) -> str:
  """
  Cancel an order, given an order ID.

  If the order is successfully canceled, return "Order canceled.".
  If the order is not found, return "Order not found.".

  Args:
    order_id (str): The order ID of the order to cancel.

  Returns:
    str: The status message indicating whether the order was canceled.
  """
  if order_id in orders:
    orders[order_id]["order_status"] = "Canceled"
    return "Order canceled."
  else:
    return "Order not found."

tools = [retrieve_user_id, get_order_id, get_order_status, cancel_order]
