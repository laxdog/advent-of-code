data "local_file" "input_file" {
  filename = "input.txt"
}

locals {
  # Parse rows from the input file
  rows = [
    for line in split("\n", data.local_file.input_file.content) :
    [for val in split(" ", trimspace(line)) : tonumber(val)]
    if trimspace(line) != ""
  ]

  # Filter rows that are sorted (incrementing or decrementing)
  is_sorted = [
    for row in local.rows :
    row if formatlist("%05d", row) == [for val in sort(formatlist("%05d", row)) : tonumber(val)] || formatlist("%05d", row) == [for val in reverse(sort(formatlist("%05d", row))) : tonumber(val)]
  ]

  # Filter rows that are "safe" based on consecutive differences
  safe_checks = [
    for row in local.is_sorted :
    row if alltrue([
      for i in range(0, length(row) - 1) :
      abs(row[i] - row[i + 1]) >= 1 && abs(row[i] - row[i + 1]) <= 3
    ])
  ]

  # Filter rows that have sufficient length and pass safe checks
  is_safe = [
    for row in local.safe_checks :
    row if length(row) > 1
  ]

  # Final filtered rows that meet all conditions
  safe_rows = local.is_safe

  # Totals
  total = length(local.safe_rows)
  total2 = 0
}

output "debug" {
  value = {
    # rows        = local.rows,
    # is_sorted   = local.is_sorted,
    # safe_checks = local.safe_checks,
    # is_safe     = local.is_safe,
    # safe_rows   = local.safe_rows,
    l_rows        = length(local.rows),
    l_is_sorted   = length(local.is_sorted),
    l_safe_checks = length(local.safe_checks),
    l_is_safe     = length(local.is_safe),
    l_safe_rows   = length(local.safe_rows),
    d_sort_rows   = [for row in local.rows : sort(formatlist("%05d", row))]
    d_reverse_rows  = [for row in local.rows : reverse(sort(formatlist("%05d", row)))]
  }
}

output "total" {
  value = local.total
}
