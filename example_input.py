def main(value: int) -> int:
  num = str(value).replace('-','')
  rev = int(num[::-1])
  if value < 0:
    rev = rev * (-1)
  return rev

