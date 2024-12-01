data "local_file" "input_file" {
  filename = "input.txt"
}

locals {
  rows = [
    for line in split("\n", data.local_file.input_file.content) :
    split("   ", trimspace(line))
    if length(split("   ", trimspace(line))) == 2
  ]

  left  = sort([for row in local.rows : tonumber(row[0])])
  right = sort([for row in local.rows : tonumber(row[1])])


  total  = sum([for idx in range(0, length(local.left)) : abs(local.left[idx] - local.right[idx])])
  total2 = sum([for num in local.left : length([for val in local.right : val if val == num]) * num])
}

output "total" {
  value = local.total
}

output "total2" {
  value = local.total2
}
