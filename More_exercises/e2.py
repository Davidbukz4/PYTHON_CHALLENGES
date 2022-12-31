#Program performs conversion of human years to dog years
x = "Enter the human year(s) to see the approximate" \
    "dog year(s).\n Enter positive numbers: "
response = float(input(x))

if response > 0 and response <= 1:
    answer = (response*7)
    print("The approximate dog year is ",answer)
elif response > 0 and response <= 2:
    answer = (response * 10.5) / 2
    print("The approximate dog year is ",answer)
elif response > 2:
    answer1 = (2 * 10.5) / 2
    response -= 2
    answer2 = (response * 4) / 1
    print("The approximate dog year is ",answer1+answer2)