from metric import Metric

def margin_percent(df):
  total_sales = df["Sales"].sum()
  return df["Gross margin"].sum() / total_sales if total_sales > 0 else 0

def average_transaction_value(df):
  total_sales = df["Sales"].sum()
  return total_sales / df["Transactions"].sum() if total_sales > 0 else 0

metrics = {
  "Total sales": Metric(
    title="Total sales",
    func=lambda df: df["Sales"].sum(),
    type="dollars"
  ),
  "Gross margin": Metric(
    title="Gross margin",
    func=lambda df: df["Gross margin"].sum(),
    type="dollars"
  ),
  "Margin %": Metric(
    title="Margin %",
    func=margin_percent,
    type="percent"
  ),
  "ATV": Metric(
    title="Average transaction value",
    func=average_transaction_value,
    type="dollars"
  )
}

display_metrics = ["Total sales", "Gross margin", "Margin %", "ATV"]