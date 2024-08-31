import time

"""
"methode format, case : "{:,.4f}.format()":
   - ':' : Start marker for the format specification.
   - ',' : Use commas as thousands separators.
   - '.4' : Four digits after the decimal point.
   - 'f' : Value should be formatted as a floating-point number.
"""

second_since_epoch = time.time()
time_float_format = "{:,.4f}".format(second_since_epoch)
time_e_format = "{:.3e}".format(second_since_epoch)
time_formatted = time.strftime("%b %d %Y", time.gmtime())
result_string = (
    f"Seconds since January 1, 1970: {time_float_format} or "
    f"{time_e_format} in scientific notation\n{time_formatted}"
)

print(result_string)
