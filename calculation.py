import time


def time_conversion(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    seconds = str(round(seconds,2))
    hours = minutes // 60
    minutes = minutes % 60
    #Need to make seconds value shorter on screen
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(minutes), seconds))


input("Press Enter to Start")
start_time = time.time()

print("________________________________________________________________")

input("Press Enter to Stop")
end_time = time.time()

time_lapsed = end_time - start_time
time_conversion(time_lapsed)

