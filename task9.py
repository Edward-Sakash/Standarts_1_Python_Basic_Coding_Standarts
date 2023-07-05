def my_custom_validation_function(
    one, two, three, four, five, six, seven, eight, nine, ten
):
    if all([one, two, three, four, five]) and\
            not any([six, seven, eight, nine, ten]):
        print("ok")


my_custom_validation_function(
    one=True,
    two=True,
    three=True,
    four=True,
    five=True,
    six=False,
    seven=False,
    eight=False,
    nine=False,
    ten=False,
)
