def my_custom_validation_function(
    one, two, three, four, five, six, seven, eight, nine, ten
):
    if (
        one
        and two
        and three
        and four
        and five
        and not six
        and not seven
        and not eight
        and not nine
        and not ten
    ):
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
