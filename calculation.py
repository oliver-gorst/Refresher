import time


def time_conversion(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    seconds = str(round(seconds,3))
    hours = minutes // 60
    minutes = minutes % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(minutes), seconds))
    #Take the difference here and display how close the user was to getting the correct answer


print("After pressing Enter to start the timer, press Enter again once 5 seconds has passed.")

input("Press Enter to Start")
start_time = time.time()

print("______________________________________")

input("Press Enter to Stop")
end_time = time.time()

time_lapsed = end_time - start_time
time_conversion(time_lapsed)


