shortmonth =sum(map(int, str(12345678910111213141516171819202122232425262728)))
defaultmonth =sum(map(int, str(123456789101112131415161718192021222324252627282930)))
longmonth =sum(map(int, str(12345678910111213141516171819202122232425262728293031)))
print(f"Сумма всех цифр: {7*longmonth+4*defaultmonth+shortmonth}")