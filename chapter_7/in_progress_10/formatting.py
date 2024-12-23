import humanize

def format_metric(value, metric_type):
  if metric_type == "dollars":
    return f'${humanize.metric(value)}'
  elif metric_type == "percent":
    return f'{round(value * 100, 1)}%'
  return f'{value}'

def format_dataframe(df, metrics):
  cols = df.columns
  for col in cols:
    if col in metrics:
      df[col] = df[col].apply(format_metric, metric_type=metrics[col].type)
  return df
