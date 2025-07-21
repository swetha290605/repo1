#breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.
def main():
    time=input("What time is it? ")
    float_time=convert(time)
    if float_time>=7.0 and float_time<=8.0:
        print("breakfast time")
    elif float_time>=12.0 and float_time<=13.0:
        print("lunch time")
    elif float_time>=18.0 and float_time<=19.0:
        print("dinner time")
    
def convert(time):
    time=time.split(":")
    hours=time[0]
    minutes=time[1]
    hours=int(hours)
    minutes=int(minutes)
    totalmin=(hours*60) + (minutes)
    time_in_float=totalmin/60
    return time_in_float

if __name__ == "__main__":
    main()